# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setWindowTitle(u"DatabaseViewer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tablesList = QListWidget(self.centralwidget)
        self.tablesList.setObjectName(u"tablesList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tablesList.sizePolicy().hasHeightForWidth())
        self.tablesList.setSizePolicy(sizePolicy2)
        self.tablesList.setMinimumSize(QSize(120, 470))
        self.tablesList.setMaximumSize(QSize(120, 16777215))
        self.tablesList.setBaseSize(QSize(100, 400))
        font = QFont()
        font.setPointSize(12)
        self.tablesList.setFont(font)

        self.verticalLayout_5.addWidget(self.tablesList)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        sizePolicy2.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy2)
        self.addButton.setMinimumSize(QSize(120, 0))

        self.verticalLayout.addWidget(self.addButton)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")
        sizePolicy2.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy2)
        self.editButton.setMinimumSize(QSize(120, 0))

        self.verticalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy2.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy2)
        self.deleteButton.setMinimumSize(QSize(120, 0))

        self.verticalLayout.addWidget(self.deleteButton)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.layoutWidget_4 = QWidget(self.page1)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 0, 654, 578))
        self.verticalLayoutPage1 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayoutPage1.setObjectName(u"verticalLayoutPage1")
        self.verticalLayoutPage1.setContentsMargins(0, 0, 0, 0)
        self.labelPage1 = QLabel(self.layoutWidget_4)
        self.labelPage1.setObjectName(u"labelPage1")
        self.labelPage1.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.labelPage1.sizePolicy().hasHeightForWidth())
        self.labelPage1.setSizePolicy(sizePolicy1)
        self.labelPage1.setMinimumSize(QSize(650, 50))
        self.labelPage1.setMaximumSize(QSize(650, 50))
        font1 = QFont()
        font1.setPointSize(28)
        self.labelPage1.setFont(font1)

        self.verticalLayoutPage1.addWidget(self.labelPage1)

        self.framePage1 = QFrame(self.layoutWidget_4)
        self.framePage1.setObjectName(u"framePage1")
        sizePolicy1.setHeightForWidth(self.framePage1.sizePolicy().hasHeightForWidth())
        self.framePage1.setSizePolicy(sizePolicy1)
        self.framePage1.setMinimumSize(QSize(650, 520))
        self.framePage1.setMaximumSize(QSize(16777215, 16777215))
        self.framePage1.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePage1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.framePage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayoutFramePage1 = QVBoxLayout()
        self.verticalLayoutFramePage1.setObjectName(u"verticalLayoutFramePage1")
        self.tableNameEditPage1 = QLineEdit(self.framePage1)
        self.tableNameEditPage1.setObjectName(u"tableNameEditPage1")
        sizePolicy1.setHeightForWidth(self.tableNameEditPage1.sizePolicy().hasHeightForWidth())
        self.tableNameEditPage1.setSizePolicy(sizePolicy1)
        self.tableNameEditPage1.setMinimumSize(QSize(600, 50))
        self.tableNameEditPage1.setMaximumSize(QSize(16777215, 50))
        self.tableNameEditPage1.setBaseSize(QSize(0, 50))
        self.tableNameEditPage1.setFont(font)

        self.verticalLayoutFramePage1.addWidget(self.tableNameEditPage1)

        self.fieldsAreaPage1 = QScrollArea(self.framePage1)
        self.fieldsAreaPage1.setObjectName(u"fieldsAreaPage1")
        self.fieldsAreaPage1.setEnabled(True)
        self.fieldsAreaPage1.setMinimumSize(QSize(630, 100))
        self.fieldsAreaPage1.setMaximumSize(QSize(16777215, 16777215))
        self.fieldsAreaPage1.setAutoFillBackground(False)
        self.fieldsAreaPage1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.fieldsAreaPage1.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.fieldsAreaPage1.setWidgetResizable(True)
        self.fieldsAreaPage1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContentsPage1 = QWidget()
        self.scrollAreaWidgetContentsPage1.setObjectName(u"scrollAreaWidgetContentsPage1")
        self.scrollAreaWidgetContentsPage1.setGeometry(QRect(0, 0, 628, 382))
        self.gridLayout1 = QGridLayout(self.scrollAreaWidgetContentsPage1)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.fieldsAreaPage1.setWidget(self.scrollAreaWidgetContentsPage1)

        self.verticalLayoutFramePage1.addWidget(self.fieldsAreaPage1)

        self.fieldButtonsLayoutPage1 = QHBoxLayout()
        self.fieldButtonsLayoutPage1.setObjectName(u"fieldButtonsLayoutPage1")
        self.newFieldButtonPage1 = QPushButton(self.framePage1)
        self.newFieldButtonPage1.setObjectName(u"newFieldButtonPage1")
        self.newFieldButtonPage1.setMinimumSize(QSize(100, 50))
        self.newFieldButtonPage1.setMaximumSize(QSize(16777215, 16777215))

        self.fieldButtonsLayoutPage1.addWidget(self.newFieldButtonPage1)

        self.removeFieldButtonPage1 = QPushButton(self.framePage1)
        self.removeFieldButtonPage1.setObjectName(u"removeFieldButtonPage1")
        self.removeFieldButtonPage1.setMinimumSize(QSize(100, 50))
        self.removeFieldButtonPage1.setMaximumSize(QSize(16777215, 16777215))

        self.fieldButtonsLayoutPage1.addWidget(self.removeFieldButtonPage1)

        self.saveButtonPage1 = QPushButton(self.framePage1)
        self.saveButtonPage1.setObjectName(u"saveButtonPage1")
        self.saveButtonPage1.setMinimumSize(QSize(100, 50))
        self.saveButtonPage1.setMaximumSize(QSize(16777215, 16777215))

        self.fieldButtonsLayoutPage1.addWidget(self.saveButtonPage1)


        self.verticalLayoutFramePage1.addLayout(self.fieldButtonsLayoutPage1)


        self.verticalLayout_2.addLayout(self.verticalLayoutFramePage1)


        self.verticalLayoutPage1.addWidget(self.framePage1)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        sizePolicy1.setHeightForWidth(self.page2.sizePolicy().hasHeightForWidth())
        self.page2.setSizePolicy(sizePolicy1)
        self.layoutWidget_2 = QWidget(self.page2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 652, 578))
        self.verticalLayoutPage2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayoutPage2.setObjectName(u"verticalLayoutPage2")
        self.verticalLayoutPage2.setContentsMargins(0, 0, 0, 0)
        self.labelPage2 = QLabel(self.layoutWidget_2)
        self.labelPage2.setObjectName(u"labelPage2")
        self.labelPage2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.labelPage2.sizePolicy().hasHeightForWidth())
        self.labelPage2.setSizePolicy(sizePolicy1)
        self.labelPage2.setMinimumSize(QSize(650, 50))
        self.labelPage2.setMaximumSize(QSize(650, 50))
        self.labelPage2.setFont(font1)

        self.verticalLayoutPage2.addWidget(self.labelPage2)

        self.framePage2 = QFrame(self.layoutWidget_2)
        self.framePage2.setObjectName(u"framePage2")
        sizePolicy1.setHeightForWidth(self.framePage2.sizePolicy().hasHeightForWidth())
        self.framePage2.setSizePolicy(sizePolicy1)
        self.framePage2.setMinimumSize(QSize(650, 520))
        self.framePage2.setMaximumSize(QSize(16777215, 16777215))
        self.framePage2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePage2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.framePage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableNameEditPage2 = QLineEdit(self.framePage2)
        self.tableNameEditPage2.setObjectName(u"tableNameEditPage2")
        sizePolicy1.setHeightForWidth(self.tableNameEditPage2.sizePolicy().hasHeightForWidth())
        self.tableNameEditPage2.setSizePolicy(sizePolicy1)
        self.tableNameEditPage2.setMinimumSize(QSize(600, 50))
        self.tableNameEditPage2.setMaximumSize(QSize(16777215, 50))
        self.tableNameEditPage2.setBaseSize(QSize(0, 50))
        self.tableNameEditPage2.setFont(font)

        self.verticalLayout_3.addWidget(self.tableNameEditPage2)

        self.fieldsAreaPage2 = QScrollArea(self.framePage2)
        self.fieldsAreaPage2.setObjectName(u"fieldsAreaPage2")
        self.fieldsAreaPage2.setEnabled(True)
        self.fieldsAreaPage2.setMinimumSize(QSize(630, 100))
        self.fieldsAreaPage2.setMaximumSize(QSize(16777215, 16777215))
        self.fieldsAreaPage2.setAutoFillBackground(False)
        self.fieldsAreaPage2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.fieldsAreaPage2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.fieldsAreaPage2.setWidgetResizable(True)
        self.fieldsAreaPage2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContentsPage2 = QWidget()
        self.scrollAreaWidgetContentsPage2.setObjectName(u"scrollAreaWidgetContentsPage2")
        self.scrollAreaWidgetContentsPage2.setGeometry(QRect(0, 0, 628, 98))
        self.gridLayout2 = QGridLayout(self.scrollAreaWidgetContentsPage2)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.fieldsAreaPage2.setWidget(self.scrollAreaWidgetContentsPage2)

        self.verticalLayout_3.addWidget(self.fieldsAreaPage2)

        self.fieldButtonsLayoutPage2 = QHBoxLayout()
        self.fieldButtonsLayoutPage2.setObjectName(u"fieldButtonsLayoutPage2")
        self.newFieldButtonPage2 = QPushButton(self.framePage2)
        self.newFieldButtonPage2.setObjectName(u"newFieldButtonPage2")
        self.newFieldButtonPage2.setMinimumSize(QSize(100, 50))
        self.newFieldButtonPage2.setMaximumSize(QSize(16777215, 16777215))

        self.fieldButtonsLayoutPage2.addWidget(self.newFieldButtonPage2)

        self.removeFieldButtonPage2 = QPushButton(self.framePage2)
        self.removeFieldButtonPage2.setObjectName(u"removeFieldButtonPage2")
        self.removeFieldButtonPage2.setMinimumSize(QSize(100, 50))
        self.removeFieldButtonPage2.setMaximumSize(QSize(16777215, 16777215))

        self.fieldButtonsLayoutPage2.addWidget(self.removeFieldButtonPage2)

        self.saveButtonPage2 = QPushButton(self.framePage2)
        self.saveButtonPage2.setObjectName(u"saveButtonPage2")
        self.saveButtonPage2.setMinimumSize(QSize(100, 50))
        self.saveButtonPage2.setMaximumSize(QSize(16777215, 16777215))

        self.fieldButtonsLayoutPage2.addWidget(self.saveButtonPage2)


        self.verticalLayout_3.addLayout(self.fieldButtonsLayoutPage2)


        self.verticalLayoutPage2.addWidget(self.framePage2)

        self.stackedWidget.addWidget(self.page2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.labelPage1.setText(QCoreApplication.translate("MainWindow", u"Add New Table", None))
        self.tableNameEditPage1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Table Name", None))
        self.newFieldButtonPage1.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.removeFieldButtonPage1.setText(QCoreApplication.translate("MainWindow", u"Remove field", None))
        self.saveButtonPage1.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.labelPage2.setText(QCoreApplication.translate("MainWindow", u"Edit Table", None))
        self.tableNameEditPage2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Table Name", None))
        self.newFieldButtonPage2.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.removeFieldButtonPage2.setText(QCoreApplication.translate("MainWindow", u"Remove field", None))
        self.saveButtonPage2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        pass
    # retranslateUi

