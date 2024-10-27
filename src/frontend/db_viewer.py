from typing import Callable

import psycopg
from PySide6.QtWidgets import QMainWindow, QDialog, QGridLayout

from src.backend.connection import DatabaseConnection
from src.backend.types import Field, Difference
from src.frontend.error_window import ErrorWindow
from src.frontend.pyqt.ui_create_conn import Ui_CreateConn
from src.frontend.pyqt.ui_field_widget import Ui_FieldWidget
from src.frontend.pyqt.ui_main import Ui_MainWindow


class DatabaseViewer(QMainWindow):
    def __init__(self):
        super(DatabaseViewer, self).__init__()

        self.connection: DatabaseConnection = DatabaseConnection()
        self.is_connected: bool = False

        self.add_page_fields: list[Ui_FieldWidget] = []
        self.edit_page_fields: list[Ui_FieldWidget] = []

        self.tables: list[str] = []

        self.current_table: str = ""
        self.current_fields: dict[Ui_FieldWidget, Field] = {}

        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.create_conn_window = QDialog()
        self.create_conn_window.window().setWindowTitle("Create Connection")
        self.ui_create_conn = Ui_CreateConn()
        self.ui_create_conn.setupUi(self.create_conn_window)
        self.ui_create_conn.createConnButton.clicked.connect(self.create_connection)

        self.ui_main.addButton.clicked.connect(self.add_button_clicked)
        self.ui_main.editButton.clicked.connect(self.edit_button_clicked)
        self.ui_main.deleteButton.clicked.connect(self.delete_button_clicked)

        self.ui_main.newFieldButtonPage1.clicked.connect(
            self.add_field_button_clicked(self.ui_main.gridLayout1, self.add_page_fields)
        )
        self.ui_main.newFieldButtonPage2.clicked.connect(
            self.add_field_button_clicked(self.ui_main.gridLayout2, self.edit_page_fields)
        )

        self.ui_main.saveButtonPage1.clicked.connect(self.save_button_clicked("add"))
        self.ui_main.saveButtonPage2.clicked.connect(self.save_button_clicked("edit"))

        self.ui_main.removeFieldButtonPage1.clicked.connect(
            self.remove_field_button_clicked(self.ui_main.gridLayout1, self.add_page_fields)
        )
        self.ui_main.removeFieldButtonPage2.clicked.connect(
            self.remove_field_button_clicked(self.ui_main.gridLayout2, self.edit_page_fields)
        )

        self.field_widget_id = Ui_FieldWidget()
        self.field_widget_id.setupUi(self)
        self.field_widget_id.fieldNameEdit.setText("id")
        self.field_widget_id.typeBox.setCurrentIndex(0)
        self.field_widget_id.primaryKeyBox.setChecked(True)
        self.add_page_fields.append(self.field_widget_id)

        self.ui_main.gridLayout1.addWidget(self.field_widget_id.layoutWidget)

    def show(self) -> None:
        if not self.is_connected:
            self.create_conn_window.show()
            return

        self.create_conn_window.close()
        super().show()

    def create_connection(self) -> None:
        # user = self.ui_create_conn.userEdit.text().strip()
        # password = self.ui_create_conn.passEdit.text().strip()
        # host = self.ui_create_conn.hostEdit.text().strip()
        # port = self.ui_create_conn.portEdit.text().strip()
        # name = self.ui_create_conn.dbNameEdit.text().strip()

        user = "postgres"
        password = "admin"
        host = "localhost"
        port = "5432"
        name = "test_db"

        if any((user == "", password == "", host == "", port == "", name == "")): return None

        try:
            self.connection.set_connection(user, password, host, port, name)
            self.is_connected = True
            self.show()
            self.update_list_of_tables()
        except psycopg.OperationalError as e:
            ErrorWindow().show_error(e)

    def update_list_of_tables(self) -> None:
        self.ui_main.tablesList.clear()

        self.tables = self.connection.get_tables()

        for table in self.tables:
            self.ui_main.tablesList.addItem(table)

    def add_button_clicked(self) -> None:
        if self.ui_main.gridLayout1.itemAt(0) is None:
            self.field_widget_id.setupUi(self)
            self.field_widget_id.fieldNameEdit.setText("id")
            self.field_widget_id.typeBox.setCurrentIndex(0)
            self.field_widget_id.primaryKeyBox.setChecked(True)
            self.ui_main.gridLayout1.addWidget(self.field_widget_id.layoutWidget)
            self.add_page_fields.append(self.field_widget_id)

        self.ui_main.stackedWidget.setCurrentIndex(0)

    def edit_button_clicked(self) -> None:
        if len(self.ui_main.tablesList.selectedItems()) != 0:
            for i in range(len(self.edit_page_fields)):
                widget_to_delete = self.edit_page_fields.pop()
                self.ui_main.gridLayout2.removeWidget(widget_to_delete.layoutWidget)
                widget_to_delete.layoutWidget.deleteLater()

            self.current_fields = {}

            table_name = self.ui_main.tablesList.selectedItems()[0].text()
            self.current_table = table_name

            fields = self.connection.get_fields(self.current_table)

            for field in fields:
                field_widget = Ui_FieldWidget()
                field_widget.setupUi(self)
                field_widget.fieldNameEdit.setText(field.name)
                field_widget.typeBox.setCurrentText(field.type_)
                field_widget.primaryKeyBox.setChecked(field.is_primary_key)
                self.ui_main.gridLayout2.addWidget(field_widget.layoutWidget)
                self.edit_page_fields.append(field_widget)
                self.current_fields[field_widget] = field

            self.ui_main.tableNameEditPage2.setText(table_name)
            self.ui_main.stackedWidget.setCurrentIndex(1)

    def delete_button_clicked(self) -> None:
        if len(self.ui_main.tablesList.selectedItems()) != 0:
            table = self.ui_main.tablesList.selectedItems()[0].text()
            self.connection.delete_table(table)
            self.update_list_of_tables()

    def add_field_button_clicked(self, grid_layout: QGridLayout, widgets: list[Ui_FieldWidget]) -> Callable:
        def wrapper() -> None:
            field_widget = Ui_FieldWidget()
            field_widget.setupUi(self)
            field_widget.typeBox.setCurrentIndex(0)
            field_widget.primaryKeyBox.setChecked(False)

            widgets.append(field_widget)
            grid_layout.addWidget(field_widget.layoutWidget)

        return wrapper

    def add_table(self) -> None:
        if self.ui_main.tableNameEditPage1.text() != "":
            table_name = self.ui_main.tableNameEditPage1.text()
            if table_name not in self.tables:
                fields = [
                    Field(name=widget.fieldNameEdit.text(), type_=widget.typeBox.currentText(),
                          is_primary_key=widget.primaryKeyBox.isChecked())
                    for widget in self.add_page_fields
                ]
                self.connection.create_table(table_name, fields)
                self.update_list_of_tables()

                for i in range(len(self.add_page_fields)):
                    widget_to_delete = self.add_page_fields.pop()
                    self.ui_main.gridLayout1.removeWidget(widget_to_delete.layoutWidget)
                    widget_to_delete.layoutWidget.deleteLater()

                self.ui_main.tableNameEditPage1.setText("")
                self.add_button_clicked()

    def update_table(self) -> None:
        if self.ui_main.tableNameEditPage2.text() != "":
            table_name = self.ui_main.tableNameEditPage2.text()
            differences: list[Difference] = []

            for widget in self.edit_page_fields:
                if widget in self.current_fields.keys():
                    difference = Difference(
                        self.current_fields[widget],
                        Field(name=widget.fieldNameEdit.text(), type_=widget.typeBox.currentText(),
                              is_primary_key=widget.primaryKeyBox.isChecked())
                    )
                else:
                    difference = Difference(
                        None,
                        Field(name=widget.fieldNameEdit.text(), type_=widget.typeBox.currentText(),
                              is_primary_key=widget.primaryKeyBox.isChecked())
                    )
                differences.append(difference)

            for key in self.current_fields.keys():
                if key not in self.edit_page_fields:
                    difference = Difference(self.current_fields[key], None)
                    differences.append(difference)

            try:
                self.connection.update_table(self.current_table, table_name, differences)
                self.update_list_of_tables()

                for i in range(len(self.edit_page_fields)):
                    widget_to_delete = self.edit_page_fields.pop()
                    self.ui_main.gridLayout2.removeWidget(widget_to_delete.layoutWidget)
                    widget_to_delete.layoutWidget.deleteLater()

                self.ui_main.tableNameEditPage2.setText("")
                self.add_button_clicked()
            except ValueError as e:
                ErrorWindow().show_error(e)

    def save_button_clicked(self, action: str) -> Callable:
        def wrapper() -> None:
            if action == "add":
                self.add_table()
                return None

            if action == "edit":
                self.update_table()

        return wrapper

    @staticmethod
    def remove_field_button_clicked(grid_layout: QGridLayout, widgets: list[Ui_FieldWidget]) -> Callable:
        def wrapper() -> None:
            if len(widgets) > 0:
                widget_to_delete = widgets.pop()
                grid_layout.removeWidget(widget_to_delete.layoutWidget)
                widget_to_delete.layoutWidget.deleteLater()

        return wrapper
