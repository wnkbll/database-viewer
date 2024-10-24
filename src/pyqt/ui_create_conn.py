# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_conn.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CreateConn(object):
    def setupUi(self, CreateConn):
        if not CreateConn.objectName():
            CreateConn.setObjectName(u"CreateConn")
        CreateConn.resize(600, 400)
        CreateConn.setMinimumSize(QSize(600, 400))
        CreateConn.setMaximumSize(QSize(800, 400))
        CreateConn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.verticalLayout_2 = QVBoxLayout(CreateConn)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(CreateConn)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.userEdit = QLineEdit(self.frame)
        self.userEdit.setObjectName(u"userEdit")
        sizePolicy.setHeightForWidth(self.userEdit.sizePolicy().hasHeightForWidth())
        self.userEdit.setSizePolicy(sizePolicy)
        self.userEdit.setMinimumSize(QSize(0, 50))
        self.userEdit.setMaximumSize(QSize(16777215, 50))
        self.userEdit.setBaseSize(QSize(0, 50))
        self.userEdit.setFont(font)

        self.verticalLayout.addWidget(self.userEdit)

        self.passEdit = QLineEdit(self.frame)
        self.passEdit.setObjectName(u"passEdit")
        sizePolicy.setHeightForWidth(self.passEdit.sizePolicy().hasHeightForWidth())
        self.passEdit.setSizePolicy(sizePolicy)
        self.passEdit.setMinimumSize(QSize(0, 50))
        self.passEdit.setMaximumSize(QSize(16777215, 50))
        self.passEdit.setBaseSize(QSize(0, 50))
        self.passEdit.setFont(font)

        self.verticalLayout.addWidget(self.passEdit)

        self.hostEdit = QLineEdit(self.frame)
        self.hostEdit.setObjectName(u"hostEdit")
        sizePolicy.setHeightForWidth(self.hostEdit.sizePolicy().hasHeightForWidth())
        self.hostEdit.setSizePolicy(sizePolicy)
        self.hostEdit.setMinimumSize(QSize(0, 50))
        self.hostEdit.setMaximumSize(QSize(16777215, 50))
        self.hostEdit.setBaseSize(QSize(0, 50))
        self.hostEdit.setFont(font)
        self.hostEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.verticalLayout.addWidget(self.hostEdit)

        self.portEdit = QLineEdit(self.frame)
        self.portEdit.setObjectName(u"portEdit")
        sizePolicy.setHeightForWidth(self.portEdit.sizePolicy().hasHeightForWidth())
        self.portEdit.setSizePolicy(sizePolicy)
        self.portEdit.setMinimumSize(QSize(0, 50))
        self.portEdit.setMaximumSize(QSize(16777215, 50))
        self.portEdit.setBaseSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.portEdit.setFont(font1)

        self.verticalLayout.addWidget(self.portEdit)

        self.dbNameEdit = QLineEdit(self.frame)
        self.dbNameEdit.setObjectName(u"dbNameEdit")
        sizePolicy.setHeightForWidth(self.dbNameEdit.sizePolicy().hasHeightForWidth())
        self.dbNameEdit.setSizePolicy(sizePolicy)
        self.dbNameEdit.setMinimumSize(QSize(0, 50))
        self.dbNameEdit.setMaximumSize(QSize(16777215, 50))
        self.dbNameEdit.setBaseSize(QSize(0, 50))
        self.dbNameEdit.setFont(font)

        self.verticalLayout.addWidget(self.dbNameEdit)

        self.createConnButton = QPushButton(self.frame)
        self.createConnButton.setObjectName(u"createConnButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.createConnButton.sizePolicy().hasHeightForWidth())
        self.createConnButton.setSizePolicy(sizePolicy1)
        self.createConnButton.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.createConnButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(CreateConn)

        QMetaObject.connectSlotsByName(CreateConn)
    # setupUi

    def retranslateUi(self, CreateConn):
        CreateConn.setWindowTitle(QCoreApplication.translate("CreateConn", u"Dialog", None))
        self.userEdit.setPlaceholderText(QCoreApplication.translate("CreateConn", u"User", None))
        self.passEdit.setPlaceholderText(QCoreApplication.translate("CreateConn", u"Password", None))
        self.hostEdit.setPlaceholderText(QCoreApplication.translate("CreateConn", u"Host", None))
        self.portEdit.setPlaceholderText(QCoreApplication.translate("CreateConn", u"Port", None))
        self.dbNameEdit.setPlaceholderText(QCoreApplication.translate("CreateConn", u"Database Name", None))
        self.createConnButton.setText(QCoreApplication.translate("CreateConn", u"Create Connection", None))
    # retranslateUi

