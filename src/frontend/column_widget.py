from PySide6.QtWidgets import QWidget

from src.frontend.pyqt.ui_column_widget import Ui_ColumnWidget


class Widget(QWidget):
    @property
    def widget(self) -> QWidget:
        return self


class ColumnWidget(Widget):
    def __init__(self) -> None:
        super(ColumnWidget, self).__init__()

        self.ui = Ui_ColumnWidget()
        self.ui.setupUi(self)

    @property
    def name(self) -> str:
        return self.ui.name_edit.text().strip()

    @name.setter
    def name(self, value: str) -> None:
        self.ui.name_edit.setText(value)

    @property
    def type(self) -> str:
        return self.ui.type.currentText()

    @type.setter
    def type(self, value: str) -> None:
        self.ui.type.setCurrentText(value)

    @property
    def is_checked(self) -> bool:
        return self.ui.primary_key.isChecked()

    @is_checked.setter
    def is_checked(self, value: bool) -> None:
        self.ui.primary_key.setChecked(value)

    @property
    def widget(self) -> QWidget:
        return self.ui.layoutWidget
