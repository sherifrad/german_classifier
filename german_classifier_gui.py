# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'german_classifier.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QListWidget::item {\n"
"padding: 10px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.main_tab)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.main_tab)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(48)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);\n"
"padding: 30px;\n"
"border: none;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.main_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.word_edit = QtWidgets.QLineEdit(self.main_tab)
        self.word_edit.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.word_edit.setFont(font)
        self.word_edit.setText("")
        self.word_edit.setObjectName("word_edit")
        self.verticalLayout_7.addWidget(self.word_edit)
        self.label_6 = QtWidgets.QLabel(self.main_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.category_combo = QtWidgets.QComboBox(self.main_tab)
        self.category_combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.category_combo.setObjectName("category_combo")
        self.verticalLayout_7.addWidget(self.category_combo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.submit_button = QtWidgets.QPushButton(self.main_tab)
        self.submit_button.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);")
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout.addWidget(self.submit_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.main_tab, "")
        self.articles_tab = QtWidgets.QWidget()
        self.articles_tab.setObjectName("articles_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.articles_tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.articles_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: crimson;\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.articles_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("text-decoration: underline;\n"
"color: rgb(255, 85, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.articles_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("text-decoration: underline;\n"
"color: rgb(0, 85, 127);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.articles_tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.die_list = QtWidgets.QListWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setItalic(True)
        self.die_list.setFont(font)
        self.die_list.setStyleSheet("color: crimson;")
        self.die_list.setObjectName("die_list")
        self.das_list = QtWidgets.QListWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setItalic(True)
        self.das_list.setFont(font)
        self.das_list.setStyleSheet("color: rgb(66, 141, 77);\n"
"color: rgb(255, 85, 0);")
        self.das_list.setObjectName("das_list")
        self.der_list = QtWidgets.QListWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setItalic(True)
        self.der_list.setFont(font)
        self.der_list.setStyleSheet("color: rgb(0, 85, 127);")
        self.der_list.setObjectName("der_list")
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout.setStretch(1, 1)
        self.tabWidget.addTab(self.articles_tab, "")
        self.animals_tab = QtWidgets.QWidget()
        self.animals_tab.setObjectName("animals_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.animals_tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.animal_list = QtWidgets.QListWidget(self.animals_tab)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.animal_list.setFont(font)
        self.animal_list.setStyleSheet("QListWidget::item {\n"
"padding: 10px;\n"
"}")
        self.animal_list.setObjectName("animal_list")
        self.verticalLayout_4.addWidget(self.animal_list)
        self.tabWidget.addTab(self.animals_tab, "")
        self.vegetabls_tab = QtWidgets.QWidget()
        self.vegetabls_tab.setObjectName("vegetabls_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.vegetabls_tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vegetable_list = QtWidgets.QListWidget(self.vegetabls_tab)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.vegetable_list.setFont(font)
        self.vegetable_list.setStyleSheet("QListWidget::item {\n"
"padding: 10px;\n"
"}")
        self.vegetable_list.setObjectName("vegetable_list")
        self.verticalLayout_5.addWidget(self.vegetable_list)
        self.tabWidget.addTab(self.vegetabls_tab, "")
        self.simple_tab = QtWidgets.QWidget()
        self.simple_tab.setObjectName("simple_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.simple_tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.simple_list = QtWidgets.QListWidget(self.simple_tab)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.simple_list.setFont(font)
        self.simple_list.setObjectName("simple_list")
        self.verticalLayout_2.addWidget(self.simple_list)
        self.tabWidget.addTab(self.simple_tab, "")
        self.phrasal_tab = QtWidgets.QWidget()
        self.phrasal_tab.setObjectName("phrasal_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.phrasal_tab)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.phrasal_list = QtWidgets.QListWidget(self.phrasal_tab)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.phrasal_list.setFont(font)
        self.phrasal_list.setStyleSheet("QListWidget::item {\n"
"padding: 10px;\n"
"}")
        self.phrasal_list.setObjectName("phrasal_list")
        self.verticalLayout_6.addWidget(self.phrasal_list)
        self.tabWidget.addTab(self.phrasal_tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.category_combo.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "German Classifier"))
        self.label_5.setText(_translate("MainWindow", "Classify"))
        self.label_6.setText(_translate("MainWindow", "in"))
        self.submit_button.setText(_translate("MainWindow", "&Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("MainWindow", "&Main"))
        self.label.setText(_translate("MainWindow", "Die"))
        self.label_2.setText(_translate("MainWindow", "Das"))
        self.label_3.setText(_translate("MainWindow", "Der"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.articles_tab), _translate("MainWindow", "&Articles"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.animals_tab), _translate("MainWindow", "A&nimals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vegetabls_tab), _translate("MainWindow", "&Vegetables"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.simple_tab), _translate("MainWindow", "S&imple Verbs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.phrasal_tab), _translate("MainWindow", "&Phrasal Verbs"))

