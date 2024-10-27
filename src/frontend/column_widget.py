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
        return self.ui.fieldNameEdit.text().strip()

    @name.setter
    def name(self, value: str) -> None:
        self.ui.fieldNameEdit.setText(value)

    @property
    def type(self) -> str:
        return self.ui.typeBox.currentText()

    @type.setter
    def type(self, value: str) -> None:
        self.ui.typeBox.setCurrentText(value)

    @property
    def is_checked(self) -> bool:
        return self.ui.primaryKeyBox.isChecked()

    @is_checked.setter
    def is_checked(self, value: bool) -> None:
        self.ui.primaryKeyBox.setChecked(value)

    @property
    def widget(self) -> QWidget:
        return self.ui.layoutWidget
