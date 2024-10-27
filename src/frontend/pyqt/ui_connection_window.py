# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection_window.ui'
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

class Ui_ConnectionWindow(object):
    def setupUi(self, ConnectionWindow):
        if not ConnectionWindow.objectName():
            ConnectionWindow.setObjectName(u"ConnectionWindow")
        ConnectionWindow.resize(600, 400)
        ConnectionWindow.setMinimumSize(QSize(600, 400))
        ConnectionWindow.setMaximumSize(QSize(800, 400))
        ConnectionWindow.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.verticalLayout_2 = QVBoxLayout(ConnectionWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(ConnectionWindow)
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
        self.user_edit = QLineEdit(self.frame)
        self.user_edit.setObjectName(u"user_edit")
        sizePolicy.setHeightForWidth(self.user_edit.sizePolicy().hasHeightForWidth())
        self.user_edit.setSizePolicy(sizePolicy)
        self.user_edit.setMinimumSize(QSize(0, 50))
        self.user_edit.setMaximumSize(QSize(16777215, 50))
        self.user_edit.setBaseSize(QSize(0, 50))
        self.user_edit.setFont(font)

        self.verticalLayout.addWidget(self.user_edit)

        self.password_edit = QLineEdit(self.frame)
        self.password_edit.setObjectName(u"password_edit")
        sizePolicy.setHeightForWidth(self.password_edit.sizePolicy().hasHeightForWidth())
        self.password_edit.setSizePolicy(sizePolicy)
        self.password_edit.setMinimumSize(QSize(0, 50))
        self.password_edit.setMaximumSize(QSize(16777215, 50))
        self.password_edit.setBaseSize(QSize(0, 50))
        self.password_edit.setFont(font)

        self.verticalLayout.addWidget(self.password_edit)

        self.host_edit = QLineEdit(self.frame)
        self.host_edit.setObjectName(u"host_edit")
        sizePolicy.setHeightForWidth(self.host_edit.sizePolicy().hasHeightForWidth())
        self.host_edit.setSizePolicy(sizePolicy)
        self.host_edit.setMinimumSize(QSize(0, 50))
        self.host_edit.setMaximumSize(QSize(16777215, 50))
        self.host_edit.setBaseSize(QSize(0, 50))
        self.host_edit.setFont(font)
        self.host_edit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.verticalLayout.addWidget(self.host_edit)

        self.port_edit = QLineEdit(self.frame)
        self.port_edit.setObjectName(u"port_edit")
        sizePolicy.setHeightForWidth(self.port_edit.sizePolicy().hasHeightForWidth())
        self.port_edit.setSizePolicy(sizePolicy)
        self.port_edit.setMinimumSize(QSize(0, 50))
        self.port_edit.setMaximumSize(QSize(16777215, 50))
        self.port_edit.setBaseSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.port_edit.setFont(font1)

        self.verticalLayout.addWidget(self.port_edit)

        self.db_name_edit = QLineEdit(self.frame)
        self.db_name_edit.setObjectName(u"db_name_edit")
        sizePolicy.setHeightForWidth(self.db_name_edit.sizePolicy().hasHeightForWidth())
        self.db_name_edit.setSizePolicy(sizePolicy)
        self.db_name_edit.setMinimumSize(QSize(0, 50))
        self.db_name_edit.setMaximumSize(QSize(16777215, 50))
        self.db_name_edit.setBaseSize(QSize(0, 50))
        self.db_name_edit.setFont(font)

        self.verticalLayout.addWidget(self.db_name_edit)

        self.connection_button = QPushButton(self.frame)
        self.connection_button.setObjectName(u"connection_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.connection_button.sizePolicy().hasHeightForWidth())
        self.connection_button.setSizePolicy(sizePolicy1)
        self.connection_button.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.connection_button)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(ConnectionWindow)

        QMetaObject.connectSlotsByName(ConnectionWindow)
    # setupUi

    def retranslateUi(self, ConnectionWindow):
        ConnectionWindow.setWindowTitle(QCoreApplication.translate("ConnectionWindow", u"Dialog", None))
        self.user_edit.setPlaceholderText(QCoreApplication.translate("ConnectionWindow", u"User", None))
        self.password_edit.setPlaceholderText(QCoreApplication.translate("ConnectionWindow", u"Password", None))
        self.host_edit.setPlaceholderText(QCoreApplication.translate("ConnectionWindow", u"Host", None))
        self.port_edit.setPlaceholderText(QCoreApplication.translate("ConnectionWindow", u"Port", None))
        self.db_name_edit.setPlaceholderText(QCoreApplication.translate("ConnectionWindow", u"Database Name", None))
        self.connection_button.setText(QCoreApplication.translate("ConnectionWindow", u"Create Connection", None))
    # retranslateUi

