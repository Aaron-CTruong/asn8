# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblFrPerson = QGroupBox(self.centralwidget)
        self.lblFrPerson.setObjectName(u"lblFrPerson")
        self.lblFrPerson.setGeometry(QRect(30, 20, 451, 201))
        self.gridLayout = QGridLayout(self.lblFrPerson)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblLast = QLabel(self.lblFrPerson)
        self.lblLast.setObjectName(u"lblLast")
        self.lblLast.setStyleSheet(u"background-color: blue;\n"
"color: white;")

        self.gridLayout.addWidget(self.lblLast, 1, 0, 1, 1)

        self.lblFirst = QLabel(self.lblFrPerson)
        self.lblFirst.setObjectName(u"lblFirst")
        self.lblFirst.setStyleSheet(u"background-color: blue;\n"
"color: white;")

        self.gridLayout.addWidget(self.lblFirst, 0, 0, 1, 1)

        self.entLast = QLineEdit(self.lblFrPerson)
        self.entLast.setObjectName(u"entLast")

        self.gridLayout.addWidget(self.entLast, 1, 1, 1, 1)

        self.entPhone = QLineEdit(self.lblFrPerson)
        self.entPhone.setObjectName(u"entPhone")

        self.gridLayout.addWidget(self.entPhone, 3, 1, 1, 1)

        self.entFirst = QLineEdit(self.lblFrPerson)
        self.entFirst.setObjectName(u"entFirst")

        self.gridLayout.addWidget(self.entFirst, 0, 1, 1, 1)

        self.entEmail = QLineEdit(self.lblFrPerson)
        self.entEmail.setObjectName(u"entEmail")

        self.gridLayout.addWidget(self.entEmail, 2, 1, 1, 1)

        self.lblEmail = QLabel(self.lblFrPerson)
        self.lblEmail.setObjectName(u"lblEmail")

        self.gridLayout.addWidget(self.lblEmail, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lblPhone = QLabel(self.lblFrPerson)
        self.lblPhone.setObjectName(u"lblPhone")

        self.gridLayout.addWidget(self.lblPhone, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.fraButtons = QFrame(self.lblFrPerson)
        self.fraButtons.setObjectName(u"fraButtons")
        self.fraButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnS = QPushButton(self.fraButtons)
        self.btnS.setObjectName(u"btnS")
        self.btnS.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnS)

        self.btnR = QPushButton(self.fraButtons)
        self.btnR.setObjectName(u"btnR")
        self.btnR.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnR)

        self.btnQ = QPushButton(self.fraButtons)
        self.btnQ.setObjectName(u"btnQ")
        self.btnQ.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnQ)


        self.gridLayout.addWidget(self.fraButtons, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblFrPerson.setTitle(QCoreApplication.translate("MainWindow", u"Personal Information", None))
        self.lblLast.setText(QCoreApplication.translate("MainWindow", u"*Last Name:", None))
        self.lblFirst.setText(QCoreApplication.translate("MainWindow", u"*First Name:", None))
        self.lblEmail.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lblPhone.setText(QCoreApplication.translate("MainWindow", u"Phone:", None))
        self.btnS.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.btnR.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnQ.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

