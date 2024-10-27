# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.setWindowTitle(u"DBViewer")
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.left_layout = QVBoxLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.tables_list = QListWidget(self.main_widget)
        self.tables_list.setObjectName(u"tables_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tables_list.sizePolicy().hasHeightForWidth())
        self.tables_list.setSizePolicy(sizePolicy2)
        self.tables_list.setMinimumSize(QSize(120, 470))
        self.tables_list.setMaximumSize(QSize(120, 16777215))
        self.tables_list.setBaseSize(QSize(100, 400))
        font = QFont()
        font.setPointSize(12)
        self.tables_list.setFont(font)

        self.left_layout.addWidget(self.tables_list)

        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.add_button = QPushButton(self.main_widget)
        self.add_button.setObjectName(u"add_button")
        sizePolicy2.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy2)
        self.add_button.setMinimumSize(QSize(120, 0))

        self.buttons_layout.addWidget(self.add_button)

        self.edit_button = QPushButton(self.main_widget)
        self.edit_button.setObjectName(u"edit_button")
        sizePolicy2.setHeightForWidth(self.edit_button.sizePolicy().hasHeightForWidth())
        self.edit_button.setSizePolicy(sizePolicy2)
        self.edit_button.setMinimumSize(QSize(120, 0))

        self.buttons_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton(self.main_widget)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy2.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy2)
        self.delete_button.setMinimumSize(QSize(120, 0))

        self.buttons_layout.addWidget(self.delete_button)


        self.left_layout.addLayout(self.buttons_layout)


        self.main_layout.addLayout(self.left_layout)

        self.pages = QStackedWidget(self.main_widget)
        self.pages.setObjectName(u"pages")
        sizePolicy1.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy1)
        self.add_page = QWidget()
        self.add_page.setObjectName(u"add_page")
        self.layoutWidget_4 = QWidget(self.add_page)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 0, 654, 578))
        self.add_page_layout = QVBoxLayout(self.layoutWidget_4)
        self.add_page_layout.setObjectName(u"add_page_layout")
        self.add_page_layout.setContentsMargins(0, 0, 0, 0)
        self.add_page_label = QLabel(self.layoutWidget_4)
        self.add_page_label.setObjectName(u"add_page_label")
        self.add_page_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.add_page_label.sizePolicy().hasHeightForWidth())
        self.add_page_label.setSizePolicy(sizePolicy1)
        self.add_page_label.setMinimumSize(QSize(650, 50))
        self.add_page_label.setMaximumSize(QSize(650, 50))
        font1 = QFont()
        font1.setPointSize(28)
        self.add_page_label.setFont(font1)

        self.add_page_layout.addWidget(self.add_page_label)

        self.add_page_frame = QFrame(self.layoutWidget_4)
        self.add_page_frame.setObjectName(u"add_page_frame")
        sizePolicy1.setHeightForWidth(self.add_page_frame.sizePolicy().hasHeightForWidth())
        self.add_page_frame.setSizePolicy(sizePolicy1)
        self.add_page_frame.setMinimumSize(QSize(650, 520))
        self.add_page_frame.setMaximumSize(QSize(16777215, 16777215))
        self.add_page_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.add_page_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.add_page_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_page_frame_layout = QVBoxLayout()
        self.add_page_frame_layout.setObjectName(u"add_page_frame_layout")
        self.add_page_table_name_edit = QLineEdit(self.add_page_frame)
        self.add_page_table_name_edit.setObjectName(u"add_page_table_name_edit")
        sizePolicy1.setHeightForWidth(self.add_page_table_name_edit.sizePolicy().hasHeightForWidth())
        self.add_page_table_name_edit.setSizePolicy(sizePolicy1)
        self.add_page_table_name_edit.setMinimumSize(QSize(600, 50))
        self.add_page_table_name_edit.setMaximumSize(QSize(16777215, 50))
        self.add_page_table_name_edit.setBaseSize(QSize(0, 50))
        self.add_page_table_name_edit.setFont(font)

        self.add_page_frame_layout.addWidget(self.add_page_table_name_edit)

        self.add_page_scroll_area = QScrollArea(self.add_page_frame)
        self.add_page_scroll_area.setObjectName(u"add_page_scroll_area")
        self.add_page_scroll_area.setEnabled(True)
        self.add_page_scroll_area.setMinimumSize(QSize(630, 100))
        self.add_page_scroll_area.setMaximumSize(QSize(16777215, 16777215))
        self.add_page_scroll_area.setAutoFillBackground(False)
        self.add_page_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.add_page_scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.add_page_scroll_area.setWidgetResizable(True)
        self.add_page_scroll_area.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.add_page_scroll_area_widget = QWidget()
        self.add_page_scroll_area_widget.setObjectName(u"add_page_scroll_area_widget")
        self.add_page_scroll_area_widget.setGeometry(QRect(0, 0, 628, 382))
        self.gridLayout1 = QGridLayout(self.add_page_scroll_area_widget)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.add_page_scroll_area.setWidget(self.add_page_scroll_area_widget)

        self.add_page_frame_layout.addWidget(self.add_page_scroll_area)

        self.add_page_buttons_layout = QHBoxLayout()
        self.add_page_buttons_layout.setObjectName(u"add_page_buttons_layout")
        self.add_page_add_button = QPushButton(self.add_page_frame)
        self.add_page_add_button.setObjectName(u"add_page_add_button")
        self.add_page_add_button.setMinimumSize(QSize(100, 50))
        self.add_page_add_button.setMaximumSize(QSize(16777215, 16777215))

        self.add_page_buttons_layout.addWidget(self.add_page_add_button)

        self.add_page_remove_button = QPushButton(self.add_page_frame)
        self.add_page_remove_button.setObjectName(u"add_page_remove_button")
        self.add_page_remove_button.setMinimumSize(QSize(100, 50))
        self.add_page_remove_button.setMaximumSize(QSize(16777215, 16777215))

        self.add_page_buttons_layout.addWidget(self.add_page_remove_button)

        self.add_page_save_button = QPushButton(self.add_page_frame)
        self.add_page_save_button.setObjectName(u"add_page_save_button")
        self.add_page_save_button.setMinimumSize(QSize(100, 50))
        self.add_page_save_button.setMaximumSize(QSize(16777215, 16777215))

        self.add_page_buttons_layout.addWidget(self.add_page_save_button)


        self.add_page_frame_layout.addLayout(self.add_page_buttons_layout)


        self.verticalLayout_2.addLayout(self.add_page_frame_layout)


        self.add_page_layout.addWidget(self.add_page_frame)

        self.pages.addWidget(self.add_page)
        self.edit_page = QWidget()
        self.edit_page.setObjectName(u"edit_page")
        sizePolicy1.setHeightForWidth(self.edit_page.sizePolicy().hasHeightForWidth())
        self.edit_page.setSizePolicy(sizePolicy1)
        self.layoutWidget_2 = QWidget(self.edit_page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 654, 578))
        self.edit_page_layout = QVBoxLayout(self.layoutWidget_2)
        self.edit_page_layout.setObjectName(u"edit_page_layout")
        self.edit_page_layout.setContentsMargins(0, 0, 0, 0)
        self.edit_page_label = QLabel(self.layoutWidget_2)
        self.edit_page_label.setObjectName(u"edit_page_label")
        self.edit_page_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.edit_page_label.sizePolicy().hasHeightForWidth())
        self.edit_page_label.setSizePolicy(sizePolicy1)
        self.edit_page_label.setMinimumSize(QSize(650, 50))
        self.edit_page_label.setMaximumSize(QSize(650, 50))
        self.edit_page_label.setFont(font1)

        self.edit_page_layout.addWidget(self.edit_page_label)

        self.edit_page_frame = QFrame(self.layoutWidget_2)
        self.edit_page_frame.setObjectName(u"edit_page_frame")
        sizePolicy1.setHeightForWidth(self.edit_page_frame.sizePolicy().hasHeightForWidth())
        self.edit_page_frame.setSizePolicy(sizePolicy1)
        self.edit_page_frame.setMinimumSize(QSize(650, 520))
        self.edit_page_frame.setMaximumSize(QSize(16777215, 16777215))
        self.edit_page_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.edit_page_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.edit_page_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.edit_page_frame_layout = QVBoxLayout()
        self.edit_page_frame_layout.setObjectName(u"edit_page_frame_layout")
        self.edit_page_table_name_edit = QLineEdit(self.edit_page_frame)
        self.edit_page_table_name_edit.setObjectName(u"edit_page_table_name_edit")
        sizePolicy1.setHeightForWidth(self.edit_page_table_name_edit.sizePolicy().hasHeightForWidth())
        self.edit_page_table_name_edit.setSizePolicy(sizePolicy1)
        self.edit_page_table_name_edit.setMinimumSize(QSize(600, 50))
        self.edit_page_table_name_edit.setMaximumSize(QSize(16777215, 50))
        self.edit_page_table_name_edit.setBaseSize(QSize(0, 50))
        self.edit_page_table_name_edit.setFont(font)

        self.edit_page_frame_layout.addWidget(self.edit_page_table_name_edit)

        self.edit_page_scroll_area = QScrollArea(self.edit_page_frame)
        self.edit_page_scroll_area.setObjectName(u"edit_page_scroll_area")
        self.edit_page_scroll_area.setEnabled(True)
        self.edit_page_scroll_area.setMinimumSize(QSize(630, 100))
        self.edit_page_scroll_area.setMaximumSize(QSize(16777215, 16777215))
        self.edit_page_scroll_area.setAutoFillBackground(False)
        self.edit_page_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.edit_page_scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.edit_page_scroll_area.setWidgetResizable(True)
        self.edit_page_scroll_area.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.edit_page_scroll_area_widget = QWidget()
        self.edit_page_scroll_area_widget.setObjectName(u"edit_page_scroll_area_widget")
        self.edit_page_scroll_area_widget.setGeometry(QRect(0, 0, 628, 382))
        self.gridLayout1_3 = QGridLayout(self.edit_page_scroll_area_widget)
        self.gridLayout1_3.setObjectName(u"gridLayout1_3")
        self.gridLayout1_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.edit_page_scroll_area.setWidget(self.edit_page_scroll_area_widget)

        self.edit_page_frame_layout.addWidget(self.edit_page_scroll_area)

        self.edit_page_buttons_layout = QHBoxLayout()
        self.edit_page_buttons_layout.setObjectName(u"edit_page_buttons_layout")
        self.edit_page_add_button = QPushButton(self.edit_page_frame)
        self.edit_page_add_button.setObjectName(u"edit_page_add_button")
        self.edit_page_add_button.setMinimumSize(QSize(100, 50))
        self.edit_page_add_button.setMaximumSize(QSize(16777215, 16777215))

        self.edit_page_buttons_layout.addWidget(self.edit_page_add_button)

        self.edit_page_remove_button = QPushButton(self.edit_page_frame)
        self.edit_page_remove_button.setObjectName(u"edit_page_remove_button")
        self.edit_page_remove_button.setMinimumSize(QSize(100, 50))
        self.edit_page_remove_button.setMaximumSize(QSize(16777215, 16777215))

        self.edit_page_buttons_layout.addWidget(self.edit_page_remove_button)

        self.edit_page_save_button = QPushButton(self.edit_page_frame)
        self.edit_page_save_button.setObjectName(u"edit_page_save_button")
        self.edit_page_save_button.setMinimumSize(QSize(100, 50))
        self.edit_page_save_button.setMaximumSize(QSize(16777215, 16777215))

        self.edit_page_buttons_layout.addWidget(self.edit_page_save_button)


        self.edit_page_frame_layout.addLayout(self.edit_page_buttons_layout)


        self.verticalLayout_4.addLayout(self.edit_page_frame_layout)


        self.edit_page_layout.addWidget(self.edit_page_frame)

        self.pages.addWidget(self.edit_page)

        self.main_layout.addWidget(self.pages)


        self.verticalLayout.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.add_page_label.setText(QCoreApplication.translate("MainWindow", u"Add New Table", None))
        self.add_page_table_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Table Name", None))
        self.add_page_add_button.setText(QCoreApplication.translate("MainWindow", u"Add column", None))
        self.add_page_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove column", None))
        self.add_page_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.edit_page_label.setText(QCoreApplication.translate("MainWindow", u"Edit Table", None))
        self.edit_page_table_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Table Name", None))
        self.edit_page_add_button.setText(QCoreApplication.translate("MainWindow", u"Add column", None))
        self.edit_page_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove column", None))
        self.edit_page_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        pass
    # retranslateUi

