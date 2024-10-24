import sys

from PySide6.QtWidgets import QApplication

from src.db_viewer import DatabaseViewer

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DatabaseViewer()
    window.show()

    sys.exit(app.exec())
