import psycopg
from PySide6.QtWidgets import QDialog

from src.backend.connection import DatabaseConnection
from src.frontend.error_window import ErrorWindow
from src.frontend.main_window import MainWindow
from src.frontend.pyqt.ui_create_conn import Ui_CreateConn


class ConnectionWindow(QDialog):
    def __init__(self):
        super(ConnectionWindow, self).__init__()

        self.ui = Ui_CreateConn()
        self.ui.setupUi(self)
        self.ui.createConnButton.clicked.connect(self.create_connection)

        self.window().setWindowTitle("Create Connection")

    def create_connection(self) -> None:
        self.ui.userEdit.setText("postgres")
        self.ui.passEdit.setText("admin")
        self.ui.hostEdit.setText("localhost")
        self.ui.portEdit.setText("5432")
        self.ui.dbNameEdit.setText("test_db")

        user = self.ui.userEdit.text().strip()
        password = self.ui.passEdit.text().strip()
        host = self.ui.hostEdit.text().strip()
        port = self.ui.portEdit.text().strip()
        name = self.ui.dbNameEdit.text().strip()

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
