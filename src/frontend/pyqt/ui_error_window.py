# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_ErrorWindow(object):
    def setupUi(self, ErrorWindow):
        if not ErrorWindow.objectName():
            ErrorWindow.setObjectName(u"ErrorWindow")
        ErrorWindow.resize(400, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorWindow.sizePolicy().hasHeightForWidth())
        ErrorWindow.setSizePolicy(sizePolicy)
        ErrorWindow.setMinimumSize(QSize(400, 200))
        ErrorWindow.setMaximumSize(QSize(400, 200))
        self.verticalLayout_2 = QVBoxLayout(ErrorWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout = QVBoxLayout()
        self.layout.setObjectName(u"layout")
        self.text_browser = QTextBrowser(ErrorWindow)
        self.text_browser.setObjectName(u"text_browser")

        self.layout.addWidget(self.text_browser)

        self.button_box = QDialogButtonBox(ErrorWindow)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.layout.addWidget(self.button_box)


        self.verticalLayout_2.addLayout(self.layout)


        self.retranslateUi(ErrorWindow)
        self.button_box.rejected.connect(ErrorWindow.reject)
        self.button_box.accepted.connect(ErrorWindow.accept)

        QMetaObject.connectSlotsByName(ErrorWindow)
    # setupUi

    def retranslateUi(self, ErrorWindow):
        ErrorWindow.setWindowTitle(QCoreApplication.translate("ErrorWindow", u"Dialog", None))
    # retranslateUi

