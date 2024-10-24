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

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(400, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Error.sizePolicy().hasHeightForWidth())
        Error.setSizePolicy(sizePolicy)
        Error.setMinimumSize(QSize(400, 200))
        Error.setMaximumSize(QSize(400, 200))
        self.verticalLayout_2 = QVBoxLayout(Error)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Error)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.buttonBox = QDialogButtonBox(Error)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Error)
        self.buttonBox.rejected.connect(Error.reject)
        self.buttonBox.accepted.connect(Error.accept)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Dialog", None))
    # retranslateUi

