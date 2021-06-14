from PyQt5 import QtCore, QtGui, QtWidgets
import glob
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QThread ,  pyqtSignal,  QDateTime
import socket
import json
import time
import threading
import pyperclip
import os

class Ui_upload(QtWidgets.QWidget):
    signal=pyqtSignal(dict)
    def __init__(self) -> None:
        super().__init__()
        self.question=""
        self.answer=""         
        self.author=""       
        self.contact_details={"type":"","val":""}
        self.description=""    
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(550, 750)
        self.setMinimumSize(QtCore.QSize(550, 750))
        self.setMaximumSize(QtCore.QSize(550, 750))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 690, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Label_message = QtWidgets.QLabel(self)
        self.Label_message.setGeometry(QtCore.QRect(120, 20, 391, 31))
        self.Label_message.setObjectName("Label_message")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 690, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 90, 501, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 340, 501, 211))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(30, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(30, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(80, 610, 451, 71))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(30, 570, 61, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(80, 570, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(30, 600, 61, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(220, 570, 91, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 570, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(300, 570, 71, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 60, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(160, 60, 61, 31))
        self.label_13.setObjectName("label_13")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "上传"))
        self.label.setText(_translate("self", "上传"))
        self.pushButton_2.setText(_translate("self", "上传"))
        self.Label_message.setText(_translate("self", "消息框"))
        self.pushButton_3.setText(_translate("self", "清空"))
        self.label_8.setText(_translate("self", "题目"))
        self.label_9.setText(_translate("self", "答案"))
        self.label_10.setText(_translate("self", "作者"))
        self.label_11.setText(_translate("self", "备注"))
        self.label_12.setText(_translate("self", "联系方式"))
        self.comboBox.setItemText(0, _translate("self", "无"))
        self.comboBox.setItemText(1, _translate("self", "手机号"))
        self.comboBox.setItemText(2, _translate("self", "QQ"))
        self.comboBox.setItemText(3, _translate("self", "微信"))
        self.comboBox.setItemText(4, _translate("self", "邮箱"))
        self.comboBox.setItemText(5, _translate("self", "其他"))
        self.comboBox_2.setItemText(0, _translate("self", "C"))
        self.comboBox_2.setItemText(1, _translate("self", "C++"))
        self.comboBox_2.setItemText(2, _translate("self", "python"))
        self.comboBox_2.setItemText(3, _translate("self", "c#"))
        self.comboBox_2.setItemText(4, _translate("self", "java"))
        self.comboBox_2.setItemText(5, _translate("self", "PHP"))
        self.comboBox_2.setItemText(6, _translate("self", "JavaScript"))
        self.comboBox_2.setItemText(7, _translate("self", "其他"))
        self.label_13.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:12pt;\">类型</span></p></body></html>"))
        
        self.pushButton_2.clicked.connect(self.upload)
        self.pushButton_3.clicked.connect(self.clear_all)
    
    def clear_all(self):
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.plainTextEdit_3.clear()
        self.comboBox.setCurrentIndex(0)
    
    def upload(self):
        self.question = self.plainTextEdit.toPlainText()
        self.answer = self.plainTextEdit_2.toPlainText()
        self.author = self.lineEdit.text()
        self.type_=self.comboBox.currentText()
        self.contact_details = {"type":self.comboBox.currentText(),"val":self.lineEdit_2.text()}
        self.description = self.plainTextEdit_3.toPlainText()
        if self.question and self.answer:
            data_dict={"Request":"040","username":main_window.username,"type":self.type_,"author":self.author,"question":self.question,"answer":self.answer,"description":self.description,"contact_details":self.contact_details}
            self.signal.emit(data_dict)
            self.pushButton_2.setEnabled(False)
        else:
            self.Label_message.setText("好事成双！")
    
    def processing_signal(self,data_dict):
        '''
        处理接收到的信号
        '''
        key=data_dict["state"]
        if key=="041":
            self.pushButton_2.setEnabled(True)
            self.Label_message.setText("上传成功\n%s"%data_dict["message"])
            self.plainTextEdit. clear()       
            self.plainTextEdit_2.clear()
            self.plainTextEdit_3.clear()
        elif key=="042":
            self.pushButton_2.setEnabled(True)
            self.Label_message.setText("上传失败\n%s"%data_dict["message"])
            
class Ui_setting(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setObjectName("self")
        self.resize(550, 280)
        self.setMinimumSize(QtCore.QSize(550, 280))
        self.setMaximumSize(QtCore.QSize(550, 280))
        self.setMouseTracking(False)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(120, 20, 391, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(200, 70, 311, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(120, 60, 61, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(120, 90, 61, 41))
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 100, 91, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(120, 150, 91, 41))
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 160, 241, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(120, 180, 91, 41))
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 190, 241, 21))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(120, 130, 121, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 130, 121, 19))
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "设置"))
        self.label.setText(_translate("self", "设置"))
        self.pushButton_2.setText(_translate("self", "恢复默认"))
        self.label_7.setText(_translate("self", "消息框"))
        
        self.pushButton_3.setText(_translate("self", "保存"))
        self.pushButton_3.clicked.connect(self.save)
        
        self.label_8.setText(_translate("self", "服务器IP"))
        self.label_9.setText(_translate("self", "端口"))
        self.label_10.setText(_translate("self", "默认登陆账号"))
        self.label_11.setText(_translate("self", "默认登陆密码"))
        self.checkBox.setText(_translate("self", "记住账号密码"))
        self.checkBox_2.setText(_translate("self", "自动复制答案"))
        self.new()
    def new(self):
        self.config_dic=starting_program()
        #self.server_IP=config_dic["server_IP"]
        #self.server_PORT=config_dic["server_PORT"]
        self.remember_u_p=config_dic["remember"]
        self.rememberd_username=config_dic["username"]
        self.rememberd_password=config_dic["password"]
        self.auto_copy=main_window.checkBox.checkState()
        #self.lineEdit.setText(self.server_IP)   #不把ip暴露所以不显示
        #self.lineEdit_2.setText(self.server_PORT)
        self.checkBox_2.stateChanged.connect(main_window.checkBox.setCheckState)
        if self.remember_u_p:
            self.lineEdit_3.setText(self.rememberd_username)
            self.lineEdit_4.setText(self.rememberd_password)
            self.checkBox.setCheckState(True)
        self.label_7.setText("服务器地址和端口基本不变所以不展示了，不能更改\n有变动时会提醒")
    def save(self):
        self.config_dic["remember"]=bool(self.checkBox.checkState())
        self.config_dic["username"]=self.lineEdit_3.text()
        self.config_dic["password"]=self.lineEdit_4.text()
        save_config(self.config_dic,config_address)
        self.pushButton_3.setText("保存成功")
        self.label_7.setText("保存成功")
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.pushButton_3.setText("保存")
        self.label_7.setText("")
        return super().closeEvent(a0)
            
class Ui_login(QtWidgets.QWidget):
    signal=pyqtSignal(dict)
    def __init__(self) -> None:
        super().__init__()
        #可以通过登录界面进入以下两个界面
        global main_window
        global regist_window
        self.remember=False
        self.re_username=""
        self.re_password=""
        self.username=""
        self.password=""
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(550, 280)
        self.setMinimumSize(QtCore.QSize(550, 280))
        self.setMaximumSize(QtCore.QSize(550, 280))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(120, 80, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(220, 80, 251, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 130, 251, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(120, 20, 381, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(220, 170, 161, 19))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "登录"))
        self.label.setText(_translate("self", "登录"))
        self.label_2.setText(_translate("self", "用户名"))
        self.label_3.setText(_translate("self", "密码"))
        self.pushButton_2.setText(_translate("self", "登录"))
        self.pushButton_2.clicked.connect(self.login)
        self.label_7.setText(_translate("self", "消息框"))
        self.pushButton_3.setText(_translate("self", "注册"))
        self.pushButton_3.clicked.connect(self.regist)
        self.checkBox.setText(_translate("self", "记住账号密码"))
        self.pushButton_2.setShortcut('Return')


    def check_remember(self):
        if self.remember:
            self.lineEdit.setText(self.re_username)
            self.lineEdit_2.setText(self.re_password)
            self.checkBox.setCheckState(True)

    def processing_signal(self,data_dict):
        '''
        处理接收到的信号
        '''
        key=data_dict["state"]
        if key=="011":
            if self.checkBox.checkState():
                config_dic["remember"]=True
                config_dic["username"]=self.username
                config_dic["password"]=self.password
            else:
                config_dic["remember"]=False
            threading.Thread(target=save_config(config_dic,config_address)).start()
            print("配置保存成功")
            self.close()
            main_window.username=self.username
            main_window.label.setText(self.username)
            main_window.show()

        elif key=="012000":
            self.label_7.setText("登录失败：IP受限，请联系管理员")
            self.pushButton_2.setEnabled(True)
        elif key=="012001":
            self.label_7.setText("登录失败：账号不存在")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.checkBox.setChecked(False)
            self.pushButton_2.setEnabled(True)
        elif key=="012002":
            self.label_7.setText("登录失败：密码错误")
            self.lineEdit_2.clear()
            self.checkBox.setChecked(False)
            self.pushButton_2.setEnabled(True)
        elif key=="012003":
            self.label_7.setText("登录失败：重复登陆失败次数过多")
            self.checkBox.setChecked(False)
            self.pushButton_2.setEnabled(True)
        elif key=="012004":
            self.label_7.setText("登录失败：账号冻结")
            self.pushButton_2.setEnabled(True)
    
    def login(self):
        '''
        点击登录按钮
        '''
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        self.username=username
        self.password=password
        if username!="" and password!="":
            dict_to_be_sent={"Request":"010","username":username,"password":password}
            self.signal.emit(dict_to_be_sent)#发送数据
            self.pushButton_2.setEnabled(False)
            #self.checkBox.checkState()
        else:
            self.label_7.setText("请检查账号密码是否输入正确")
    
    def regist(self):
        regist_window.show()

class Ui_regist(QtWidgets.QWidget):
    signal=pyqtSignal(dict)
    def __init__(self) -> None:
        super().__init__()
        self.setupUi()
        self.regist_username=""
        self.regist_password=""
        self.regist_email=""
        self.regist_yzm=""
        self.regist_yzm_true=""
        self.checked={"username1":True,"username2":False}
        self.easyregist=False
    def setupUi(self):
        self.setObjectName("self")
        self.resize(550, 280)
        self.setMinimumSize(QtCore.QSize(550, 280))
        self.setMaximumSize(QtCore.QSize(550, 280))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(120, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(120, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(120, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 171, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 100, 251, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 180, 251, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(400, 60, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(120, 10, 381, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "注册"))
        self.label.setText(_translate("self", "注册"))
        self.label_2.setText(_translate("self", "用户名"))
        self.label_3.setText(_translate("self", "密码"))
        self.label_4.setText(_translate("self", "确认密码"))
        self.label_5.setText(_translate("self", "邮箱"))
        self.label_6.setText(_translate("self", "验证码"))
        self.pushButton.setText(_translate("self", "检查是否可用"))
        self.pushButton.clicked.connect(self.check_username)
        self.pushButton_2.setText(_translate("self", "注册"))
        self.pushButton_2.clicked.connect(self.regist)
        self.label_7.setText(_translate("self", "消息框"))
        self.pushButton_3.setText(_translate("self", "获取验证码"))
        self.pushButton_3.clicked.connect(self.accept_yzm)
        
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        
        self.lineEdit.textChanged.connect(self.check_password)
        self.lineEdit_2.textChanged.connect(self.check_password)
        self.lineEdit_2.textChanged.connect(self.check_username)
        self.lineEdit_3.textChanged.connect(self.check_password)
        self.lineEdit_4.textChanged.connect(self.check_password)
        self.lineEdit_5.textChanged.connect(self.check_password)
    
    def processing_signal(self,data_dict):
        key=data_dict["state"]
        if key=="094":
            self.easyregist=True
        elif key=="072":
            self.label_7.setText("用户名可用")
            #self.lineEdit.setStyleSheet()
            self.lineEdit.setStyleSheet("background:#7fffd4;")
            self.checked[data_dict["checkname"]]=True
        elif key=="071":
            self.label_7.setText("用户名不可用")
            self.lineEdit.setStyleSheet("background:#f08080;")
            self.checked[data_dict["checkname"]]=False
        elif key=="081":
            self.label_7.setText("注册成功")
            reply=QtWidgets.QMessageBox.question(self,"注册成功","立即登录？",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            if reply==QtWidgets.QMessageBox.Yes:
                self.close()
                login_window.lineEdit.setText(data_dict["checkname"])
                login_window.lineEdit_2.setText(self.regist_password)
                login_window.show()
            else:
                self.close()
        elif key=="082":
            self.label_7.setText("注册失败\n%s"%data_dict["reason"])
        
        elif key=="091":
            self.label_7.setText("验证码已发送请注意查收")
            self.regist_yzm_true=data_dict["verification_code"]
            self.lineEdit_4.setStyleSheet("background:#7fffd4;")
            self.lineEdit_5.setEnabled(True)
        
        elif key=="092":
            self.label_7.setText("验证码发送过频繁，请稍后再试")
        
        elif key=="093":
            self.label_7.setText("验证码发送失败:邮箱错误")
            self.lineEdit_4.setStyleSheet("background:#f08080;")
    
    def regist(self):
        '''
        点击注册按钮
        '''
        self.regist_password=self.lineEdit_2.text()
        self.regist_username=self.lineEdit.text()
        self.regist_email=self.lineEdit_4.text()
        self.regist_yzm=self.lineEdit_5.text()
        dict_to_be_sent={"Request":"080","checkname":self.regist_username,"password":self.regist_password,"email":self.regist_email,"yzm":str(self.regist_yzm)}
        self.signal.emit(dict_to_be_sent)
        self.pushButton_2.setEnabled(False)
        
    def check_username(self):
        '''
        检查用户名是否可用
        '''
        self.regist_username=self.lineEdit.text()
        if self.regist_username in self.checked.keys():
            if self.checked[self.regist_username]:
                self.label_7.setText("用户名可用")
            else:
                self.label_7.setText("用户名不可用")
        else:
            dict_to_be_sent={"Request":"070","username":"unkown","checkname":self.regist_username}
            self.signal.emit(dict_to_be_sent)

    def check_password(self):                                                                        
        self.regist_password_1=self.lineEdit_2.text()
        self.regist_password_2=self.lineEdit_3.text()
        self.regist_username=self.lineEdit.text()
        self.regist_email=self.lineEdit_4.text()
        self.regist_yzm=self.lineEdit_5.text()
        
        if self.regist_username:
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            if self.regist_password_1 and self.regist_password_2:
                if self.regist_password_1==self.regist_password_2:
                    self.lineEdit_2.setStyleSheet("background:#7fffd4;")
                    self.lineEdit_3.setStyleSheet("background:#7fffd4;")
                    self.label_7.setText("密码一致")
                    self.lineEdit_4.setEnabled(True)
                    self.pushButton_3.setEnabled(True)
                    if self.easyregist==True:
                        self.pushButton_2.setEnabled(True)
                        self.pushButton_3.setEnabled(False)
                        self.lineEdit_4.setEnabled(False)
                        self.label_7.setText("简单注册，无需邮箱")
                    
                
                else:
                    self.lineEdit_2.setStyleSheet("background:#f08080")
                    self.lineEdit_3.setStyleSheet("background:#f08080")
                    self.label_7.setText("请检查密码是否一致")
                    self.lineEdit_4.setEnabled(False)
                    self.pushButton_3.setEnabled(False)
                    self.pushButton_2.setEnabled(False)

        else:
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
        
            #self.lineEdit_5.setStyleSheet("background:#7fffd4;")
            #self.lineEdit_5.setStyleSheet("background:#f08080;")
            #self.label_7.setText("请输入正确的验证码")
            #self.pushButton_2.setEnabled(False)

    def accept_yzm(self):
        '''
        发送请求获取验证码
        '''
        self.regist_email=self.lineEdit_4.text()
        data_dict={"Request":"090","username":"unknown","checkname":self.regist_username,"password":self.regist_password,"email":self.regist_email}
        self.signal.emit(data_dict)
        self.lineEdit_5.setEnabled(True)
        #self.pushButton_2.setEnabled(True)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        return super().closeEvent(a0)

class Ui_MainWindow(QtWidgets.QMainWindow):
    signal=pyqtSignal(dict)
    
    def __init__(self) -> None:
        super().__init__()
        self.answer_list=[]
        self.question=""
        self.auto_copy=False
        self.username=""
        self.serched=0
        self.uploaded=0
        self.useable=0
        self.type_="C"
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("self")
        self.resize(940, 590)
        self.setMinimumSize(QtCore.QSize(940, 590))
        self.setMaximumSize(QtCore.QSize(940, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Final/photo/serch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 40, 341, 401))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(380, 40, 341, 401))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 450, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 450, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 450, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 450, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 450, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(790, 120, 121, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(790, 200, 121, 71))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 60, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 210, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(490, 10, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(790, 280, 121, 71))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 290, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 510, 701, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(760, 390, 131, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(760, 450, 131, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(760, 510, 131, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 10, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "代码助手4.0"))
        
        self.pushButton.setText(_translate("self", "清空"))
        self.pushButton.clicked.connect(self.clear_all)
        
        self.pushButton_2.setText(_translate("self", "在线查询"))
        self.pushButton_2.clicked.connect(self.search)

        self.pushButton_3.setText(_translate("self", "上传题目"))
        self.pushButton_3.clicked.connect(self.upload)

        self.pushButton_4.setText(_translate("self", "粘贴到题目"))
        self.pushButton_4.clicked.connect(self.paste)

        self.pushButton_5.setText(_translate("self", "复制答案"))
        self.pushButton_5.clicked.connect(self.copy_answer)

        self.pushButton_6.setText(_translate("self", "设置"))
        self.pushButton_6.clicked.connect(self.setting)
        
        self.pushButton_7.setText(_translate("self", "反馈"))
        self.pushButton_8.setText(_translate("self", "关于本工具"))
        
        self.label.setText(_translate("self", "用户名"))
        self.label_2.setText(_translate("self", "查询"))
        self.label_3.setText(_translate("self", "上传"))
        self.checkBox.setText(_translate("self", "自动复制"))
        self.label_4.setText(_translate("self", "题目"))
        self.label_5.setText(_translate("self", "答案"))
        self.label_6.setText(_translate("self", "可用"))
        
        self.comboBox_2.setItemText(0, _translate("self", "C"))
        self.comboBox_2.setItemText(1, _translate("self", "C++"))
        self.comboBox_2.setItemText(2, _translate("self", "python"))
        self.comboBox_2.setItemText(3, _translate("self", "c#"))
        self.comboBox_2.setItemText(4, _translate("self", "java"))
        self.comboBox_2.setItemText(5, _translate("self", "PHP"))
        self.comboBox_2.setItemText(6, _translate("self", "JavaScript"))
        self.comboBox_2.setItemText(7, _translate("self", "其他"))
        #self.checkBox.stateChanged.connect(setting_window.checkBox_2.setCheckState)
    
    def processing_signal(self,data_dict):
        key=data_dict["state"]
        if key=="031":
            self.textBrowser.setText("成功找到 %d个"%(data_dict["quantity"]))
            self.answer_list=data_dict["answers"]
            if self.checkBox.checkState():
                self.copy_answer()
            
            for i in range(len(self.answer_list)):
                self.plainTextEdit_2.appendPlainText("答案%d\n"%(i+1))
                self.plainTextEdit_2.appendPlainText(self.answer_list[i])
                self.plainTextEdit_2.appendPlainText("\n-------------------------\n")
                
            #self.serched=data_dict["down"]
            #self.uploaded=data_dict["up"]
            #self.useable=data_dict["can"]
            #self.refresh()
        elif key=="032":
            self.textBrowser.setText("搜索失败:%s"%(data_dict["reason"]))

        elif key=="050":
            self.textBrowser.setText("收到消息:%s"%(data_dict["message"]))
        elif key=="100":
            self.lcdNumber.display(data_dict["down"])
            self.lcdNumber_2.display(data_dict["up"])
            self.lcdNumber_3.display(data_dict["can"])
    
    def copy_answer(self):
        if self.answer_list:
            pyperclip.copy(self.answer_list[-1])
            self.textBrowser.setText("答案已经复制")
    
    def paste(self):
        self.plainTextEdit.setPlainText(pyperclip.paste())
        self.textBrowser.setText("题目已经粘贴")
    
    def clear_all(self):
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.textBrowser.clear()

    def search(self):
        
        self.type_=self.comboBox_2.currentText()
        self.question=self.plainTextEdit.toPlainText().strip()#删除空白符
        if self.question!="":
            #self.answer=self.plainTextEdit_2.toPlainText()
            data_dict={"Request":"030","username":self.username,"type":self.type_,"question":self.question}
            self.signal.emit(data_dict)
        
    def setting(self):
        self.checkBox.stateChanged.connect(setting_window.checkBox_2.setCheckState)
        setting_window.show()
    
    def upload(self):
        upload_window.show()
    
    def refresh(self):
        self.lcdNumber.display(self.serched)
        self.lcdNumber_2.display(self.uploaded)
        self.lcdNumber_3.display(self.useable)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        reply=QMessageBox.question(self,"标题","你确定要退出吗？",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)#最后一个是默认选项，
        if reply==QMessageBox.Yes:
            self.logoff()
            a0.accept()
            os._exit()

        elif reply==QMessageBox.No:
            a0.ignore()
        #return super().closeEvent(a0)

    def logoff(self):
        data={"Request":"020","username":self.username}
        self.signal.emit(data)

class Receive_signal_thread(QThread):
    '''
    接收信号线程，该线程接收信号，将信号发送到对应窗口
    '''
    
    signal_all=pyqtSignal(dict)
    def __init__(self) -> None:
        super().__init__()
        
        global skt,addr
        data_dict={"Request":"000"}
        binary_data=data2byte(data_dict)
        skt.sendto(binary_data,addr)


    def run(self):
        global skt,addr
        while True:
            binary_data,addr=skt.recvfrom(1024*200)
            object_data=byte2data(binary_data)
            print("接收成功",object_data)
            #数据预先处理
            key=object_data["state"]
            #全局指令部分
            if key=="060":
                '''
                被服务器强制退出
                '''
                os._exit()
            #窗口指令部分
            self.signal_all.emit(object_data)

def data2byte(data)->bytes:
    '''
    根据 xfb传输协议1
    将python数据类型转化为二进制数据
    '''
    str_data=json.dumps(data)
    byte_data=str_data.encode("utf-8")
    return byte_data

def byte2data(bytess)->object:
    '''
    根据 xfb传输协议1
    将二进制数据转化为python数据类型
    '''
    str_data=bytess.decode("utf-8")
    data=json.loads(str_data)
    return data

def send_signal_func(dict_to_send):
    '''
    发送信号函数，所有窗口的信号都通过这一个函数发送
    '''
    global skt,addr
    binary_data=data2byte(dict_to_send)
    skt.sendto(binary_data,addr)
    print("发送成功",dict_to_send)

def read_config(address):
    '''
    读取文件
    :param address :文件地址
    :return :python数据(object)
    '''
    with open(address,'r',encoding='utf-8') as json_file:
        dic=json.load(json_file)
    return dic

def save_config(dic,address):
    '''
    将变量变为json数据储存
    :param dic :带储存的变量
    :param address :储存的文件地址
    '''
    with open(address,'w',encoding='utf-8') as json_file:
        json.dump(dic,json_file,ensure_ascii=False)

def starting_program()->dict:
    '''
    初始化程序
    1读取配置文件
    :return :配置字典
    '''
    global config_address
    #dir_address=os.getcwd()
    config_address="D:"+"\\code_helper\\"+"config.json"#创建配置储存文件
    if not os.path.exists("D:"+"\\code_helper"):
        os.makedirs("D:"+"\\code_helper")
    try:
        config_dic=read_config(config_address)
        print("读取成功")
    except:
        config_dic={ "server_IP": "xxx.xxxx.xxx.xxx", "server_PORT": xxxx, "remember": True, "username": "xxxxx", "password": "xxxxx", "auto_copy": True}
        save_config(config_dic,config_address)
        print("新建成功")
    return config_dic

if __name__ == "__main__":
    import sys
    
    config_dic=starting_program()
    server_IP=config_dic["server_IP"]
    server_PORT=config_dic["server_PORT"]
    remember_u_p=config_dic["remember"]
    rememberd_username=config_dic["username"]
    rememberd_password=config_dic["password"]
    auto_copy=password=config_dic["auto_copy"]

    ip=server_IP
    port=server_PORT
    addr = (ip,port)
    skt  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    app = QtWidgets.QApplication(sys.argv)
    
    main_window = Ui_MainWindow()
    regist_window=Ui_regist()
    login_window=Ui_login()
    login_window.remember=remember_u_p
    login_window.re_username=rememberd_username
    login_window.re_password=rememberd_password
    login_window.check_remember()
    
    setting_window=Ui_setting()
    upload_window=Ui_upload()
    
    login_window.signal.connect(send_signal_func)
    regist_window.signal.connect(send_signal_func)
    main_window.signal.connect(send_signal_func)
    upload_window.signal.connect(send_signal_func)

    thread1=Receive_signal_thread()
    
    thread1.signal_all.connect(login_window.processing_signal)
    thread1.signal_all.connect(regist_window.processing_signal)
    thread1.signal_all.connect(main_window.processing_signal)
    thread1.signal_all.connect(upload_window.processing_signal)
    
    thread1.start()
    
    #upload_window.show()   
    #setting_window.show() 
    login_window.show()
    #regist_window.show()
    #main_window.show()
    
    sys.exit(app.exec_())

