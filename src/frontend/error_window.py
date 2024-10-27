from PySide6.QtWidgets import QDialog

from src.frontend.pyqt.ui_error import Ui_Error


class ErrorWindow(QDialog):
    def __init__(self):
        super(ErrorWindow, self).__init__()

        self.ui_error = Ui_Error()
        self.ui_error.setupUi(self)
        self.ui_error.buttonBox.buttons()[0].clicked.connect(lambda _: self.close_window())

        self.window().setWindowTitle("Error")

    def show_window(self, error: str) -> None:
        self.ui_error.textBrowser.setText(error)
        self.show()

    def close_window(self) -> bool:
        close_status = self.close()
        self.deleteLater()
        return close_status
