# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wafflefront.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Solidwaffle(object):
    def setupUi(self, Solidwaffle):
        Solidwaffle.setObjectName("Solidwaffle")
        Solidwaffle.resize(1014, 797)
        self.centralwidget = QtWidgets.QWidget(Solidwaffle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setAutoFillBackground(False)
        self.username.setInputMask("")
        self.username.setText("")
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setAutoFillBackground(False)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.twoFA = QtWidgets.QLineEdit(self.centralwidget)
        self.twoFA.setEnabled(False)
        self.twoFA.setAutoFillBackground(False)
        self.twoFA.setInputMask("")
        self.twoFA.setText("")
        self.twoFA.setObjectName("twoFA")
        self.horizontalLayout_5.addWidget(self.twoFA)
        self.checkFA = QtWidgets.QCheckBox(self.centralwidget)
        self.checkFA.setObjectName("checkFA")
        self.horizontalLayout_5.addWidget(self.checkFA)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.savePassword = QtWidgets.QCheckBox(self.centralwidget)
        self.savePassword.setEnabled(True)
        self.savePassword.setObjectName("savePassword")
        self.horizontalLayout_2.addWidget(self.savePassword)
        self.autoLogin = QtWidgets.QCheckBox(self.centralwidget)
        self.autoLogin.setEnabled(True)
        self.autoLogin.setObjectName("autoLogin")
        self.horizontalLayout_2.addWidget(self.autoLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn)
        self.logoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logoutBtn.setObjectName("logoutBtn")
        self.horizontalLayout.addWidget(self.logoutBtn)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout.addWidget(self.clearBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Solidwaffle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Solidwaffle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 26))
        self.menubar.setObjectName("menubar")
        self.menuLoginbox = QtWidgets.QMenu(self.menubar)
        self.menuLoginbox.setObjectName("menuLoginbox")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        Solidwaffle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Solidwaffle)
        self.statusbar.setObjectName("statusbar")
        Solidwaffle.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(Solidwaffle)
        self.actionLogin.setObjectName("actionLogin")
        self.actionSettings = QtWidgets.QAction(Solidwaffle)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtWidgets.QAction(Solidwaffle)
        self.actionAbout.setObjectName("actionAbout")
        self.menuLoginbox.addAction(self.actionLogin)
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionAbout)
        self.menubar.addAction(self.menuLoginbox.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(Solidwaffle)
        self.checkFA.toggled['bool'].connect(self.twoFA.setEnabled)
        self.checkFA.toggled['bool'].connect(self.label_3.setEnabled)
        self.checkFA.toggled['bool'].connect(self.twoFA.clear)
        self.clearBtn.clicked.connect(self.username.clear)
        self.clearBtn.clicked.connect(self.password.clear)
        self.clearBtn.clicked.connect(self.twoFA.clear)
        QtCore.QMetaObject.connectSlotsByName(Solidwaffle)

    def retranslateUi(self, Solidwaffle):
        _translate = QtCore.QCoreApplication.translate
        Solidwaffle.setWindowTitle(_translate("Solidwaffle", "Solidwaffle"))
        self.label.setText(_translate("Solidwaffle", "Username"))
        self.username.setToolTip(_translate("Solidwaffle", "Type username"))
        self.label_2.setText(_translate("Solidwaffle", "Password"))
        self.password.setToolTip(_translate("Solidwaffle", "Type password"))
        self.label_3.setText(_translate("Solidwaffle", "Twofactor"))
        self.twoFA.setToolTip(_translate("Solidwaffle", "Type 2FA (If set)"))
        self.checkFA.setText(_translate("Solidwaffle", "Use2FA"))
        self.savePassword.setText(_translate("Solidwaffle", "Save Password"))
        self.autoLogin.setText(_translate("Solidwaffle", "Auto Login"))
        self.loginBtn.setText(_translate("Solidwaffle", "Login"))
        self.logoutBtn.setText(_translate("Solidwaffle", "Logout"))
        self.clearBtn.setText(_translate("Solidwaffle", "Clear All"))
        self.menuLoginbox.setTitle(_translate("Solidwaffle", "Loginbox"))
        self.menuSettings.setTitle(_translate("Solidwaffle", "Settings"))
        self.actionLogin.setText(_translate("Solidwaffle", "Login"))
        self.actionSettings.setText(_translate("Solidwaffle", "Settings"))
        self.actionAbout.setText(_translate("Solidwaffle", "About"))
