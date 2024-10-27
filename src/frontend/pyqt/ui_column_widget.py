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
        ColumnWidget.resize(338, 72)
        self.layoutWidget = QWidget(ColumnWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 326, 52))
        self.fieldLayout = QHBoxLayout(self.layoutWidget)
        self.fieldLayout.setObjectName(u"fieldLayout")
        self.fieldLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.fieldLayout.setContentsMargins(0, 0, 0, 0)
        self.fieldNameEdit = QLineEdit(self.layoutWidget)
        self.fieldNameEdit.setObjectName(u"fieldNameEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldNameEdit.sizePolicy().hasHeightForWidth())
        self.fieldNameEdit.setSizePolicy(sizePolicy)
        self.fieldNameEdit.setMinimumSize(QSize(0, 50))
        self.fieldNameEdit.setMaximumSize(QSize(16777215, 50))
        self.fieldNameEdit.setBaseSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(12)
        self.fieldNameEdit.setFont(font)

        self.fieldLayout.addWidget(self.fieldNameEdit)

        self.typeBox = QComboBox(self.layoutWidget)
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.setObjectName(u"typeBox")

        self.fieldLayout.addWidget(self.typeBox)

        self.primaryKeyBox = QCheckBox(self.layoutWidget)
        self.primaryKeyBox.setObjectName(u"primaryKeyBox")
        self.primaryKeyBox.setChecked(False)

        self.fieldLayout.addWidget(self.primaryKeyBox)


        self.retranslateUi(ColumnWidget)

        QMetaObject.connectSlotsByName(ColumnWidget)
    # setupUi

    def retranslateUi(self, ColumnWidget):
        ColumnWidget.setWindowTitle(QCoreApplication.translate("ColumnWidget", u"Form", None))
        self.fieldNameEdit.setText("")
        self.fieldNameEdit.setPlaceholderText(QCoreApplication.translate("ColumnWidget", u"Column Name", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("ColumnWidget", u"Integer", None))
        self.typeBox.setItemText(1, QCoreApplication.translate("ColumnWidget", u"Float", None))
        self.typeBox.setItemText(2, QCoreApplication.translate("ColumnWidget", u"Text", None))
        self.typeBox.setItemText(3, QCoreApplication.translate("ColumnWidget", u"Datetime", None))

        self.primaryKeyBox.setText(QCoreApplication.translate("ColumnWidget", u"Primary Key", None))
    # retranslateUi

