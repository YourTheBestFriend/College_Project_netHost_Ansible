from sys import *
from clr import *
from PySide6.QtWidgets import* # QApplication, QMainWindow
from PySide6.QtCore import* # QFile
from netHost import *
AddReference('DLL/ansible_host') # Include Lib
from CSharpAnsible import AnsibleHost # Import C# DLL
from multiprocessing import Process

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
            self.host = AnsibleHost(str(self.ui.lineEdit.text()), str(self.ui.lineEdit_2.text()), str(self.ui.lineEdit_3.text())) # , str(self.ui.lineEdit_4.text())
            self.host.WriteOnAnsibleHostFile()
            self.ui.textEdit_2.setText('Set_host Complete')
        except:
            self.ui.textEdit_2.setText('Error Set_host')

    def ping_host(self):
        try:
            self.ui.textEdit.setText(self.host.PingHost(self.ui.lineEdit_5.text()))
            self.ui.textEdit_2.setText('ping_host Complete')
        except:
            self.ui.textEdit_2.setText('Error ping_host')

    def get_systeminfo(self):
        try:
            # print(self.host.PrintSystemInfo(self.ui.lineEdit_5.text()))
            self.ui.textEdit.setText(self.host.PrintSystemInfo(self.ui.lineEdit_5.text()))
            
            self.ui.textEdit_2.setText('get_systeminfo')
        except:
            self.ui.textEdit_2.setText('Error get_systeminfo')
    
    def get_program(self):
        try:
            # print(self.host.PrintSystemInfo(self.ui.lineEdit_5.text()))
            self.ui.textEdit.setText(self.host.PrintProgram(self.ui.lineEdit_5.text()))
            
            self.ui.textEdit_2.setText('get_program')
        except:
            self.ui.textEdit_2.setText('Error get_program')

# Create Application 
app = QApplication(argv)
x_window = MainWindow()
x_window.show()

# set host 
x_window.ui.pushButton.clicked.connect(x_window.set_host)
# ping 
x_window.ui.pushButton_2.clicked.connect(x_window.ping_host)
# info 
x_window.ui.pushButton_3.clicked.connect(x_window.get_systeminfo)
# program
x_window.ui.pushButton_4.clicked.connect(x_window.get_program)


# print all hosts 
#print(host.GetListHosts())

# test info


# host.WriteOnAnsibleHostFile()
# Print System Info
#print(host.PrintSystemInfo('Artiom'))

# My Command 
#print(host.MyCommand('Artiom', 'dir'))

exit(app.exec())