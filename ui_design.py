# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(407, 518)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/calculator_24dp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entery = QLineEdit(self.centralwidget)
        self.le_entery.setObjectName(u"le_entery")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entery.sizePolicy().hasHeightForWidth())
        self.le_entery.setSizePolicy(sizePolicy1)
        self.le_entery.setStyleSheet(u"font-size: 40pt;\n"
"border:none;")
        self.le_entery.setMaxLength(20)
        self.le_entery.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.le_entery.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entery)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.Button_CE = QPushButton(self.centralwidget)
        self.Button_CE.setObjectName(u"Button_CE")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_CE.sizePolicy().hasHeightForWidth())
        self.Button_CE.setSizePolicy(sizePolicy2)
        self.Button_CE.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_CE, 1, 1, 1, 1)

        self.Button_ChangeSine = QPushButton(self.centralwidget)
        self.Button_ChangeSine.setObjectName(u"Button_ChangeSine")
        sizePolicy2.setHeightForWidth(self.Button_ChangeSine.sizePolicy().hasHeightForWidth())
        self.Button_ChangeSine.setSizePolicy(sizePolicy2)
        self.Button_ChangeSine.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_ChangeSine, 5, 0, 1, 1)

        self.Button_Result = QPushButton(self.centralwidget)
        self.Button_Result.setObjectName(u"Button_Result")
        sizePolicy2.setHeightForWidth(self.Button_Result.sizePolicy().hasHeightForWidth())
        self.Button_Result.setSizePolicy(sizePolicy2)
        self.Button_Result.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_Result, 5, 3, 1, 1)

        self.Button_3 = QPushButton(self.centralwidget)
        self.Button_3.setObjectName(u"Button_3")
        sizePolicy2.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy2)
        self.Button_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_3, 4, 2, 1, 1)

        self.Button_9 = QPushButton(self.centralwidget)
        self.Button_9.setObjectName(u"Button_9")
        sizePolicy2.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy2)
        self.Button_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_9, 2, 2, 1, 1)

        self.Button_Decimal = QPushButton(self.centralwidget)
        self.Button_Decimal.setObjectName(u"Button_Decimal")
        sizePolicy2.setHeightForWidth(self.Button_Decimal.sizePolicy().hasHeightForWidth())
        self.Button_Decimal.setSizePolicy(sizePolicy2)
        self.Button_Decimal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_Decimal, 5, 2, 1, 1)

        self.Button_4 = QPushButton(self.centralwidget)
        self.Button_4.setObjectName(u"Button_4")
        sizePolicy2.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy2)
        self.Button_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_4, 3, 0, 1, 1)

        self.Button_1 = QPushButton(self.centralwidget)
        self.Button_1.setObjectName(u"Button_1")
        sizePolicy2.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy2)
        self.Button_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_1, 4, 0, 1, 1)

        self.Button_2 = QPushButton(self.centralwidget)
        self.Button_2.setObjectName(u"Button_2")
        sizePolicy2.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy2)
        self.Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_2, 4, 1, 1, 1)

        self.Button_6 = QPushButton(self.centralwidget)
        self.Button_6.setObjectName(u"Button_6")
        sizePolicy2.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy2)
        self.Button_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_6, 3, 2, 1, 1)

        self.Button_Backspace = QPushButton(self.centralwidget)
        self.Button_Backspace.setObjectName(u"Button_Backspace")
        sizePolicy2.setHeightForWidth(self.Button_Backspace.sizePolicy().hasHeightForWidth())
        self.Button_Backspace.setSizePolicy(sizePolicy2)
        self.Button_Backspace.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/backspace_24dp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Backspace.setIcon(icon1)
        self.Button_Backspace.setIconSize(QSize(40, 50))

        self.layout_buttons.addWidget(self.Button_Backspace, 1, 2, 1, 1)

        self.Button_Divide = QPushButton(self.centralwidget)
        self.Button_Divide.setObjectName(u"Button_Divide")
        sizePolicy2.setHeightForWidth(self.Button_Divide.sizePolicy().hasHeightForWidth())
        self.Button_Divide.setSizePolicy(sizePolicy2)
        self.Button_Divide.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_Divide, 1, 3, 1, 1)

        self.Button_Substract = QPushButton(self.centralwidget)
        self.Button_Substract.setObjectName(u"Button_Substract")
        sizePolicy2.setHeightForWidth(self.Button_Substract.sizePolicy().hasHeightForWidth())
        self.Button_Substract.setSizePolicy(sizePolicy2)
        self.Button_Substract.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_Substract, 3, 3, 1, 1)

        self.Button_C = QPushButton(self.centralwidget)
        self.Button_C.setObjectName(u"Button_C")
        sizePolicy2.setHeightForWidth(self.Button_C.sizePolicy().hasHeightForWidth())
        self.Button_C.setSizePolicy(sizePolicy2)
        self.Button_C.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_C, 1, 0, 1, 1)

        self.Button_Add = QPushButton(self.centralwidget)
        self.Button_Add.setObjectName(u"Button_Add")
        sizePolicy2.setHeightForWidth(self.Button_Add.sizePolicy().hasHeightForWidth())
        self.Button_Add.setSizePolicy(sizePolicy2)
        self.Button_Add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_Add, 4, 3, 1, 1)

        self.Button_Multiple = QPushButton(self.centralwidget)
        self.Button_Multiple.setObjectName(u"Button_Multiple")
        sizePolicy2.setHeightForWidth(self.Button_Multiple.sizePolicy().hasHeightForWidth())
        self.Button_Multiple.setSizePolicy(sizePolicy2)
        self.Button_Multiple.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_Multiple, 2, 3, 1, 1)

        self.Button_5 = QPushButton(self.centralwidget)
        self.Button_5.setObjectName(u"Button_5")
        sizePolicy2.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy2)
        self.Button_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_5, 3, 1, 1, 1)

        self.Button_8 = QPushButton(self.centralwidget)
        self.Button_8.setObjectName(u"Button_8")
        sizePolicy2.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy2)
        self.Button_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_8, 2, 1, 1, 1)

        self.Button_0 = QPushButton(self.centralwidget)
        self.Button_0.setObjectName(u"Button_0")
        sizePolicy2.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy2)
        self.Button_0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_0, 5, 1, 1, 1)

        self.Button_7 = QPushButton(self.centralwidget)
        self.Button_7.setObjectName(u"Button_7")
        sizePolicy2.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy2)
        self.Button_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_buttons.addWidget(self.Button_7, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lbl_temp.setText("")
        self.le_entery.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.Button_ChangeSine.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.Button_Result.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.Button_Result.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.Button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.Button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.Button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Decimal.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.Button_Decimal.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.Button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.Button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.Button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.Button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Backspace.setText("")
        self.Button_Divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.Button_Divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Substract.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.Button_Substract.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.Button_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button_Add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.Button_Add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Multiple.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.Button_Multiple.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.Button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.Button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.Button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.Button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.Button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.Button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.Button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

