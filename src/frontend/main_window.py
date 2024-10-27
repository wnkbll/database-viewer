from typing import Callable

from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget

from src.backend.connection import DatabaseConnection
from src.backend.types import Column, Difference
from src.frontend.error_window import ErrorWindow
from src.frontend.pyqt.ui_column_widget import Ui_ColumnWidget
from src.frontend.column_widget import ColumnWidget
from src.frontend.pyqt.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.connection: DatabaseConnection = DatabaseConnection()

        self.add_page_fields: list[Ui_ColumnWidget] = []
        self.edit_page_fields: list[Ui_ColumnWidget] = []

        self.tables: list[str] = []

        self.current_table: str = ""
        self.current_fields: dict[Ui_ColumnWidget, Column] = {}

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window().setWindowTitle("DBViewer")

        self.ui.addButton.clicked.connect(self.add_button_clicked)
        self.ui.editButton.clicked.connect(self.edit_button_clicked)
        self.ui.deleteButton.clicked.connect(self.delete_button_clicked)

        self.ui.newFieldButtonPage1.clicked.connect(
            self.add_field_button_clicked(self.ui.gridLayout1, self.add_page_fields)
        )
        self.ui.newFieldButtonPage2.clicked.connect(
            self.add_field_button_clicked(self.ui.gridLayout2, self.edit_page_fields)
        )

        self.ui.saveButtonPage1.clicked.connect(self.save_button_clicked("add"))
        self.ui.saveButtonPage2.clicked.connect(self.save_button_clicked("edit"))

        self.ui.removeFieldButtonPage1.clicked.connect(
            self.remove_field_button_clicked(self.ui.gridLayout1, self.add_page_fields)
        )
        self.ui.removeFieldButtonPage2.clicked.connect(
            self.remove_field_button_clicked(self.ui.gridLayout2, self.edit_page_fields)
        )

        self.field_widget_id = Ui_ColumnWidget()
        self.field_widget_id.setupUi(self)
        self.field_widget_id.fieldNameEdit.setText("id")
        self.field_widget_id.typeBox.setCurrentIndex(0)
        self.field_widget_id.primaryKeyBox.setChecked(True)
        self.add_page_fields.append(self.field_widget_id)

        self.ui.gridLayout1.addWidget(self.field_widget_id.layoutWidget)

    def show(self) -> None:
        self.update_list_of_tables()
        super().show()

    def update_list_of_tables(self) -> None:
        self.ui.tablesList.clear()

        self.tables = self.connection.get_tables()

        for table in self.tables:
            self.ui.tablesList.addItem(table)

    def add_button_clicked(self) -> None:
        if self.ui.gridLayout1.itemAt(0) is None:
            self.field_widget_id.setupUi(self)
            self.field_widget_id.fieldNameEdit.setText("id")
            self.field_widget_id.typeBox.setCurrentIndex(0)
            self.field_widget_id.primaryKeyBox.setChecked(True)
            self.ui.gridLayout1.addWidget(self.field_widget_id.layoutWidget)
            self.add_page_fields.append(self.field_widget_id)

        self.ui.stackedWidget.setCurrentIndex(0)

    def edit_button_clicked(self) -> None:
        if len(self.ui.tablesList.selectedItems()) != 0:
            for i in range(len(self.edit_page_fields)):
                widget_to_delete = self.edit_page_fields.pop()
                self.ui.gridLayout2.removeWidget(widget_to_delete.layoutWidget)
                widget_to_delete.layoutWidget.deleteLater()

            self.current_fields = {}

            table_name = self.ui.tablesList.selectedItems()[0].text()
            self.current_table = table_name

            fields = self.connection.get_fields(self.current_table)

            for field in fields:
                field_widget = Ui_ColumnWidget()
                field_widget.setupUi(self)
                field_widget.fieldNameEdit.setText(field.name)
                field_widget.typeBox.setCurrentText(field.type_)
                field_widget.primaryKeyBox.setChecked(field.is_primary_key)
                self.ui.gridLayout2.addWidget(field_widget.layoutWidget)
                self.edit_page_fields.append(field_widget)
                self.current_fields[field_widget] = field

            self.ui.tableNameEditPage2.setText(table_name)
            self.ui.stackedWidget.setCurrentIndex(1)

    def delete_button_clicked(self) -> None:
        if len(self.ui.tablesList.selectedItems()) != 0:
            table = self.ui.tablesList.selectedItems()[0].text()
            self.connection.delete_table(table)
            self.update_list_of_tables()

    def add_field_button_clicked(self, grid_layout: QGridLayout, widgets: list[Ui_ColumnWidget]) -> Callable:
        def wrapper() -> None:
            field_widget = Ui_ColumnWidget()
            field_widget.setupUi(self)
            field_widget.typeBox.setCurrentIndex(0)
            field_widget.primaryKeyBox.setChecked(False)

            widgets.append(field_widget)
            grid_layout.addWidget(field_widget.layoutWidget)

        return wrapper

    def add_table(self) -> None:
        if self.ui.tableNameEditPage1.text() != "":
            table_name = self.ui.tableNameEditPage1.text()
            if table_name not in self.tables:
                fields = [
                    Column(name=widget.fieldNameEdit.text(), type_=widget.typeBox.currentText(),
                           is_primary_key=widget.primaryKeyBox.isChecked())
                    for widget in self.add_page_fields
                ]
                self.connection.create_table(table_name, fields)
                self.update_list_of_tables()

                for i in range(len(self.add_page_fields)):
                    widget_to_delete = self.add_page_fields.pop()
                    self.ui.gridLayout1.removeWidget(widget_to_delete.layoutWidget)
                    widget_to_delete.layoutWidget.deleteLater()

                self.ui.tableNameEditPage1.setText("")
                self.add_button_clicked()

    def update_table(self) -> None:
        if self.ui.tableNameEditPage2.text() != "":
            table_name = self.ui.tableNameEditPage2.text()
            differences: list[Difference] = []

            for widget in self.edit_page_fields:
                if widget in self.current_fields.keys():
                    difference = Difference(
                        self.current_fields[widget],
                        Column(name=widget.fieldNameEdit.text(), type_=widget.typeBox.currentText(),
                               is_primary_key=widget.primaryKeyBox.isChecked())
                    )
                else:
                    difference = Difference(
                        None,
                        Column(name=widget.fieldNameEdit.text(), type_=widget.typeBox.currentText(),
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
                    self.ui.gridLayout2.removeWidget(widget_to_delete.layoutWidget)
                    widget_to_delete.layoutWidget.deleteLater()

                self.ui.tableNameEditPage2.setText("")
                self.add_button_clicked()
            except ValueError as e:
                ErrorWindow().show_window(e.__repr__())

    def save_button_clicked(self, action: str) -> Callable:
        def wrapper() -> None:
            if action == "add":
                self.add_table()
                return None

            if action == "edit":
                self.update_table()

        return wrapper

    @staticmethod
    def remove_field_button_clicked(grid_layout: QGridLayout, widgets: list[Ui_ColumnWidget]) -> Callable:
        def wrapper() -> None:
            if len(widgets) > 0:
                widget_to_delete = widgets.pop()
                grid_layout.removeWidget(widget_to_delete.layoutWidget)
                widget_to_delete.layoutWidget.deleteLater()

        return wrapper
