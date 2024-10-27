from typing import Callable

from PySide6.QtWidgets import QMainWindow, QLayout

from src.backend.connection import DatabaseConnection
from src.backend.types import Column, Difference
from src.frontend.column_widget import Widget, ColumnWidget
from src.frontend.error_window import ErrorWindow
from src.frontend.pyqt.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.connection: DatabaseConnection = DatabaseConnection()

        self.add_page_fields: list[ColumnWidget] = []
        self.edit_page_fields: list[ColumnWidget] = []

        self.tables: list[str] = []

        self.current_table: str = ""
        self.current_fields: dict[ColumnWidget, Column] = {}

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
            column_widget = self.create_column_widget("id", "Integer", True)
            self.place_widget(column_widget, self.ui.gridLayout1, self.add_page_fields)

        self.ui.stackedWidget.setCurrentIndex(0)

    def edit_button_clicked(self) -> None:
        if len(self.ui.tablesList.selectedItems()) != 0:
            for i in range(len(self.edit_page_fields)):
                self.delete_widget(self.edit_page_fields[i], self.ui.gridLayout2, self.edit_page_fields)

            self.current_fields = {}

            table_name = self.ui.tablesList.selectedItems()[0].text()
            self.current_table = table_name

            fields = self.connection.get_fields(self.current_table)

            for field in fields:
                column_widget = self.create_column_widget(field.name, field.type_, field.is_primary_key)
                self.place_widget(column_widget, self.ui.gridLayout2, self.edit_page_fields)
                self.current_fields[column_widget] = field

            self.ui.tableNameEditPage2.setText(table_name)
            self.ui.stackedWidget.setCurrentIndex(1)

    def delete_button_clicked(self) -> None:
        if len(self.ui.tablesList.selectedItems()) != 0:
            table = self.ui.tablesList.selectedItems()[0].text()
            self.connection.delete_table(table)
            self.update_list_of_tables()

    def add_field_button_clicked(self, layout: QLayout, widgets: list[Widget]) -> Callable:
        def wrapper() -> None:
            column_widget = self.create_column_widget(None, "Integer", False)
            self.place_widget(column_widget, layout, widgets)

        return wrapper

    def add_table(self) -> None:
        if self.ui.tableNameEditPage1.text() != "":
            table_name = self.ui.tableNameEditPage1.text()
            if table_name not in self.tables:
                fields = [
                    Column(name=widget.name, type_=widget.type, is_primary_key=widget.is_checked)
                    for widget in self.add_page_fields
                ]
                self.connection.create_table(table_name, fields)
                self.update_list_of_tables()

                for i in range(len(self.add_page_fields)):
                    self.delete_widget(self.add_page_fields[i], self.ui.gridLayout1, self.add_page_fields)

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
                        Column(name=widget.name, type_=widget.type, is_primary_key=widget.is_checked)
                    )
                else:
                    difference = Difference(
                        None,
                        Column(name=widget.name, type_=widget.type, is_primary_key=widget.is_checked)
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
                    self.delete_widget(self.edit_page_fields[i], self.ui.gridLayout2, self.edit_page_fields)

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

    def remove_field_button_clicked(self, layout: QLayout, widgets: list[Widget]) -> Callable:
        def wrapper() -> None:
            if len(widgets) > 0:
                self.delete_widget(widgets[len(widgets) - 1], layout, widgets)

        return wrapper

    @staticmethod
    def create_column_widget(name: str | None, type_: str, is_checked: bool) -> ColumnWidget:
        column_widget = ColumnWidget()

        if name is not None:
            column_widget.name = name

        column_widget.type = type_
        column_widget.is_checked = is_checked

        return column_widget

    @staticmethod
    def place_widget(widget: Widget, layout: QLayout, widgets: list[Widget]) -> None:
        layout.addWidget(widget.widget)
        widgets.append(widget)

    @staticmethod
    def delete_widget(widget: Widget, layout: QLayout, widgets: list[Widget]) -> None:
        widgets.remove(widget)
        layout.removeWidget(widget.widget)
        widget.widget.deleteLater()
