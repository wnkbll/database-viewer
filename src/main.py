import sys

from PySide6.QtWidgets import QApplication

from src.frontend.connection_window import ConnectionWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ConnectionWindow()
    window.show()

    sys.exit(app.exec())
