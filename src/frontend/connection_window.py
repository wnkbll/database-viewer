import psycopg
from PySide6.QtWidgets import QDialog

from src.backend.connection import DatabaseConnection
from src.frontend.error_window import ErrorWindow
from src.frontend.main_window import MainWindow
from src.frontend.pyqt.ui_create_conn import Ui_CreateConn


class ConnectionWindow(QDialog):
    def __init__(self):
        super(ConnectionWindow, self).__init__()

        self.ui_create_conn = Ui_CreateConn()
        self.ui_create_conn.setupUi(self)
        self.ui_create_conn.createConnButton.clicked.connect(self.create_connection)

        self.window().setWindowTitle("Create Connection")

    def create_connection(self) -> None:
        self.ui_create_conn.userEdit.setText("postgres")
        self.ui_create_conn.passEdit.setText("admin")
        self.ui_create_conn.hostEdit.setText("localhost")
        self.ui_create_conn.portEdit.setText("5432")
        self.ui_create_conn.dbNameEdit.setText("test_db")

        user = self.ui_create_conn.userEdit.text().strip()
        password = self.ui_create_conn.passEdit.text().strip()
        host = self.ui_create_conn.hostEdit.text().strip()
        port = self.ui_create_conn.portEdit.text().strip()
        name = self.ui_create_conn.dbNameEdit.text().strip()

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
