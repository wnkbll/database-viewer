from PySide6.QtWidgets import QWidget

from src.frontend.pyqt.ui_column_widget import Ui_ColumnWidget


class ColumnWidget(QWidget):
    def __init__(self) -> None:
        super(ColumnWidget, self).__init__()

        self.ui = Ui_ColumnWidget()
        self.ui.setupUi(self)

    @property
    def widget(self) -> QWidget:
        return self.ui.layoutWidget
