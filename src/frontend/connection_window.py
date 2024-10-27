import psycopg
from PySide6.QtWidgets import QDialog

from src.backend.connection import DatabaseConnection
from src.frontend.error_window import ErrorWindow
from src.frontend.main_window import MainWindow
from src.frontend.pyqt.ui_connection_window import Ui_ConnectionWindow


class ConnectionWindow(QDialog):
    def __init__(self):
        super(ConnectionWindow, self).__init__()

        self.ui = Ui_ConnectionWindow()
        self.ui.setupUi(self)
        self.ui.connection_button.clicked.connect(self.create_connection)

        self.window().setWindowTitle("Create Connection")

    def create_connection(self) -> None:
        self.ui.user_edit.setText("postgres")
        self.ui.password_edit.setText("admin")
        self.ui.host_edit.setText("localhost")
        self.ui.port_edit.setText("5432")
        self.ui.db_name_edit.setText("test_db")

        user = self.ui.user_edit.text().strip()
        password = self.ui.password_edit.text().strip()
        host = self.ui.host_edit.text().strip()
        port = self.ui.port_edit.text().strip()
        name = self.ui.db_name_edit.text().strip()

        if any((user == "", password == "", host == "", port == "", name == "")):
            ErrorWindow().show_window("Fields must be filled")
            return None

        try:
            connection = DatabaseConnection()
            connection.set_connection(user, password, host, port, name)

            main_window = MainWindow()
            main_window.connection = connection

            self.close()
            self.deleteLater()

            main_window.show()
        except psycopg.OperationalError as e:
            ErrorWindow().show_window(e.__repr__())
