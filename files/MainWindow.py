# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setMaximumSize(QtCore.QSize(900, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_13.addWidget(self.label_11, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 0, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMinimumSize(QtCore.QSize(50, 0))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: red")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_14.addWidget(self.label_13, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(415, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_14.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_14, 1, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_8, 2, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setMinimumSize(QtCore.QSize(475, 35))
        self.label_46.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.gridLayout_11.addWidget(self.label_46, 0, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setMinimumSize(QtCore.QSize(60, 0))
        self.label_47.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.gridLayout_11.addWidget(self.label_47, 0, 1, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setMinimumSize(QtCore.QSize(20, 0))
        self.label_48.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.gridLayout_11.addWidget(self.label_48, 0, 2, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_10.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_10.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_10.setFont(font)
        self.doubleSpinBox_10.setDecimals(3)
        self.doubleSpinBox_10.setMinimum(-16777215.0)
        self.doubleSpinBox_10.setMaximum(16777215.0)
        self.doubleSpinBox_10.setSingleStep(0.001)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_11.addWidget(self.doubleSpinBox_10, 0, 3, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setMinimumSize(QtCore.QSize(60, 0))
        self.label_49.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.gridLayout_11.addWidget(self.label_49, 0, 4, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.gridLayout_11.addWidget(self.label_50, 0, 5, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 8, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(475, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(60, 0))
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(20, 0))
        self.label_8.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_2.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMinimum(-16777215.0)
        self.doubleSpinBox_2.setMaximum(16777215.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_2.addWidget(self.doubleSpinBox_2, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(35, 0))
        self.label_9.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 5, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.gridLayout_9.addWidget(self.label_40, 0, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setMinimumSize(QtCore.QSize(475, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_9.addWidget(self.label_33, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_9.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_9, 7, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setMinimumSize(QtCore.QSize(475, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setMinimumSize(QtCore.QSize(60, 0))
        self.label_23.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setMinimumSize(QtCore.QSize(20, 0))
        self.label_24.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 0, 2, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_5.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_5.setFont(font)
        self.doubleSpinBox_5.setDecimals(0)
        self.doubleSpinBox_5.setMinimum(-16777215.0)
        self.doubleSpinBox_5.setMaximum(16777215.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_5.addWidget(self.doubleSpinBox_5, 0, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setMinimumSize(QtCore.QSize(60, 0))
        self.label_25.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 0, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 0, 5, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_5, 6, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setMinimumSize(QtCore.QSize(475, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_7.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.gridLayout_7.addWidget(self.label_36, 0, 5, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_7.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_7.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_7.setFont(font)
        self.doubleSpinBox_7.setDecimals(0)
        self.doubleSpinBox_7.setMinimum(-16777215.0)
        self.doubleSpinBox_7.setMaximum(16777215.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_7.addWidget(self.doubleSpinBox_7, 0, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setMinimumSize(QtCore.QSize(20, 0))
        self.label_38.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout_7.addWidget(self.label_38, 0, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setMinimumSize(QtCore.QSize(35, 0))
        self.label_35.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 0, 4, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setMinimumSize(QtCore.QSize(60, 0))
        self.label_34.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 0, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_7, 4, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setMinimumSize(QtCore.QSize(475, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setMinimumSize(QtCore.QSize(60, 0))
        self.label_28.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setMinimumSize(QtCore.QSize(20, 0))
        self.label_29.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 0, 2, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_6.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_6.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_6.setFont(font)
        self.doubleSpinBox_6.setDecimals(2)
        self.doubleSpinBox_6.setMinimum(-16777215.0)
        self.doubleSpinBox_6.setMaximum(16777215.0)
        self.doubleSpinBox_6.setSingleStep(0.01)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_6.addWidget(self.doubleSpinBox_6, 0, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setMinimumSize(QtCore.QSize(35, 0))
        self.label_30.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 0, 4, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 0, 5, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_6, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(20, 0))
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMinimum(-16777215.0)
        self.doubleSpinBox.setMaximum(16777215.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(475, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setMinimumSize(QtCore.QSize(475, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setMinimumSize(QtCore.QSize(60, 0))
        self.label_18.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setMinimumSize(QtCore.QSize(20, 0))
        self.label_19.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 2, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_4.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setDecimals(2)
        self.doubleSpinBox_4.setMinimum(-16777215.0)
        self.doubleSpinBox_4.setMaximum(16777215.0)
        self.doubleSpinBox_4.setSingleStep(0.01)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_4.addWidget(self.doubleSpinBox_4, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setMinimumSize(QtCore.QSize(35, 0))
        self.label_20.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 0, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 5, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_4, 3, 0, 1, 1)
        self.gridLayout_12.setRowStretch(0, 1)
        self.gridLayout_12.setRowStretch(1, 1)
        self.gridLayout_12.setRowStretch(2, 2)
        self.gridLayout_12.setRowStretch(3, 1)
        self.gridLayout_12.setRowStretch(4, 1)
        self.gridLayout_12.setRowStretch(5, 1)
        self.gridLayout_12.setRowStretch(6, 1)
        self.gridLayout_12.setRowStretch(7, 1)
        self.gridLayout_12.setRowStretch(8, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_13.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout_13.setRowStretch(0, 1)
        self.gridLayout_13.setRowStretch(1, 12)
        self.gridLayout_13.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчет сечения кабеля для всех участков электросети"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Расчет сечения кабеля для всех участков электросети</p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p>Заполните исходные данные по участкам: </p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Ввести таблицу"))
        self.label_46.setText(_translate("MainWindow", "<html><head/><body><p>Введите удельное сопротивление проводника:</p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p>ρ</p></body></html>"))
        self.label_48.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p>Ом.м.</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Введите количество участков:</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>m</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p>Введите материал проводника:</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p>Введите мощность вырабатываемую КПД:</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">кпд</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p>кВт</p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p>Введите % потери напряжения:</p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p>%</p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p>Введите коэффициент (потери) мощности: </p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p>cos φ</p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>n</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Введите количество домов в СНТ: </p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>Введите напряжение сети: </p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>U</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p>B</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
