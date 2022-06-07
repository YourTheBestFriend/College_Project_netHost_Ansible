from concurrent.futures import thread
# import multiprocessing
from sys import *
from threading import Thread
from clr import *
from PySide6.QtWidgets import* # QApplication, QMainWindow
from PySide6.QtCore import* # QFile
from netHost import *
AddReference('DLL/ansible_host') # Include Lib
from CSharpAnsible import AnsibleHost # Import C# DLL

class MainWindow(QMainWindow):
    # create empty host
    host = AnsibleHost('none', 'none','none') # 'none' 
    def __init__(self):
       # For driwing
       super(MainWindow, self).__init__()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self)
    
    # main functions
    def set_host(self):
        try:
            if len(str(self.ui.lineEdit.text())) == 0 or len(str(self.ui.lineEdit_2.text())) == 0 or len(str(self.ui.lineEdit_3.text())) == 0:
                self.ui.textEdit_2.setText('Error Set_host')
            else:
                self.host = AnsibleHost(str(self.ui.lineEdit.text()), str(self.ui.lineEdit_2.text()), str(self.ui.lineEdit_3.text())) # , str(self.ui.lineEdit_4.text())
                self.host.WriteOnAnsibleHostFile()
                self.ui.textEdit_2.setText('Set_host Complete')
        except:
            self.ui.textEdit_2.setText('Error Set_host')
    
    def get_list_hosts(self):
        self.ui.textEdit.setText(self.host.GetListHosts())
    
    def ping_host(self):
        try:
            if len(str(self.ui.lineEdit_5.text())) != 0:
                self.ui.textEdit.setText(self.host.PingHost(self.ui.lineEdit_5.text())) # functionMultiProcessing()
                self.ui.textEdit_2.setText('ping_host Complete') 
            else:
                self.ui.textEdit_2.setText('Error ping_host')
        except:
            self.ui.textEdit_2.setText('Error ping_host')

    def get_systeminfo(self):
        try:
            if len(str(self.ui.lineEdit_5.text())) != 0:
                self.ui.textEdit.setText(self.host.PrintSystemInfo(self.ui.lineEdit_5.text()))
                self.ui.textEdit_2.setText('get_systeminfo')
            else:
                self.ui.textEdit_2.setText('Error get_systeminfo')
        except:
            self.ui.textEdit_2.setText('Error get_systeminfo')
    
    def get_program_x32(self):
        try:
            if len(str(self.ui.lineEdit_5.text())) != 0:
                self.ui.textEdit.setText(self.host.PrintProgram_x32(self.ui.lineEdit_5.text()))
                self.ui.textEdit_2.setText('get_program_x32')
            else:
                self.ui.textEdit_2.setText('Error get_program_x32')
        except:
            self.ui.textEdit_2.setText('Error get_program_x32')
    
    def get_program_x64(self):
        try:
            if len(str(self.ui.lineEdit_5.text())) != 0:
                self.ui.textEdit.setText(self.host.PrintProgram_x64(self.ui.lineEdit_5.text()))
                self.ui.textEdit_2.setText('get_program_x64')
            else:
                self.ui.textEdit_2.setText('Error get_program_x64')
        except:
            self.ui.textEdit_2.setText('Error get_program_x64')
    
    def get_proccesses(self):
        try:
            if len(str(self.ui.lineEdit_5.text())) != 0:
                self.ui.textEdit.setText(self.host.Proccess_(self.ui.lineEdit_5.text()))
                self.ui.textEdit_2.setText('get_proccesses')
            else:
                self.ui.textEdit_2.setText('Error get_proccesses')
        except:
            self.ui.textEdit_2.setText('Error get_proccesses')

    def get_use_whatever(self):
        try:
            if len(str(self.ui.lineEdit_5.text())) != 0:
                self.ui.textEdit.setText(self.host.MyCommand(self.ui.lineEdit_6.text()))
                self.ui.textEdit_2.setText('get_use_whatever')
            else:
                self.ui.textEdit_2.setText('Error get_use_whatever')
        except:
            self.ui.textEdit_2.setText('Error get_use_whatever')

    def get_settings(self):
        self.ui.textEdit_2.setText('')
        self.ui.groupBox_3.setVisible(True)
        self.ui.pushButton_13.setEnabled(False)
        self.ui.textEdit_2.setEnabled(False)
        self.ui.label_7.setVisible(False)
    
    def out_settings(self):
        self.ui.groupBox_3.setVisible(False)
        self.ui.pushButton_13.setEnabled(True)
        self.ui.textEdit_2.setEnabled(True)
        self.ui.label_7.setVisible(True)
        
# Create Application 
app = QApplication(argv)
x_window = MainWindow()
x_window.show()
x_window.ui.groupBox_3.setVisible(False)
x_window.ui.groupBox.setVisible(True)

# set host 
x_window.ui.pushButton_6.clicked.connect(x_window.set_host)
# check hosts 
x_window.ui.pushButton.clicked.connect(x_window.get_list_hosts)
# ping 
x_window.ui.pushButton_2.clicked.connect(x_window.ping_host)
# info 
x_window.ui.pushButton_3.clicked.connect(x_window.get_systeminfo)
# program x_32
x_window.ui.pushButton_5.clicked.connect(x_window.get_program_x32)
# program x_64
x_window.ui.pushButton_11.clicked.connect(x_window.get_program_x64)
# processes
x_window.ui.pushButton_12.clicked.connect(x_window.get_proccesses)
# use your personal command (try...)
x_window.ui.pushButton_4.clicked.connect(x_window.get_use_whatever)
# open settings
x_window.ui.pushButton_13.clicked.connect(x_window.get_settings)
# close settings
x_window.ui.pushButton_14.clicked.connect(x_window.out_settings)

exit(app.exec())