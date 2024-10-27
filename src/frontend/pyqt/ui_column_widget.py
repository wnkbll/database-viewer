# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'column_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLayout, QLineEdit, QSizePolicy, QWidget)

class Ui_ColumnWidget(object):
    def setupUi(self, ColumnWidget):
        if not ColumnWidget.objectName():
            ColumnWidget.setObjectName(u"ColumnWidget")
        ColumnWidget.resize(338, 70)
        self.layoutWidget = QWidget(ColumnWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 320, 52))
        self.column_layout = QHBoxLayout(self.layoutWidget)
        self.column_layout.setObjectName(u"column_layout")
        self.column_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.column_layout.setContentsMargins(0, 0, 0, 0)
        self.name_edit = QLineEdit(self.layoutWidget)
        self.name_edit.setObjectName(u"name_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy)
        self.name_edit.setMinimumSize(QSize(0, 50))
        self.name_edit.setMaximumSize(QSize(16777215, 50))
        self.name_edit.setBaseSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(12)
        self.name_edit.setFont(font)

        self.column_layout.addWidget(self.name_edit)

        self.type = QComboBox(self.layoutWidget)
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.setObjectName(u"type")

        self.column_layout.addWidget(self.type)

        self.primary_key = QCheckBox(self.layoutWidget)
        self.primary_key.setObjectName(u"primary_key")
        self.primary_key.setChecked(False)

        self.column_layout.addWidget(self.primary_key)


        self.retranslateUi(ColumnWidget)

        QMetaObject.connectSlotsByName(ColumnWidget)
    # setupUi

    def retranslateUi(self, ColumnWidget):
        ColumnWidget.setWindowTitle(QCoreApplication.translate("ColumnWidget", u"Form", None))
        self.name_edit.setText("")
        self.name_edit.setPlaceholderText(QCoreApplication.translate("ColumnWidget", u"Column Name", None))
        self.type.setItemText(0, QCoreApplication.translate("ColumnWidget", u"Integer", None))
        self.type.setItemText(1, QCoreApplication.translate("ColumnWidget", u"Float", None))
        self.type.setItemText(2, QCoreApplication.translate("ColumnWidget", u"Text", None))
        self.type.setItemText(3, QCoreApplication.translate("ColumnWidget", u"Datetime", None))

        self.primary_key.setText(QCoreApplication.translate("ColumnWidget", u"Primary Key", None))
    # retranslateUi

