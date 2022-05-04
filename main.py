from sys import *
from clr import *
from PySide6.QtWidgets import* # QApplication, QMainWindow
from PySide6.QtCore import* # QFile
from netHost import Ui_Dialog
AddReference('DLL/ansible_host') # Include Lib
from CSharpAnsible import AnsibleHost # Import C# DLL

class MainWindow(QMainWindow):
     def __init__(self):
        # Для отрисовки
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

# main functions
def set_host():
    AnsibleHost = AnsibleHost(ui.lineEdit.text(), ui.lineEdit_2.text(), \
                              ui.lineEdit_3.text(), ui.lineEdit_4.text())


# Create Application 
app = QApplication(argv)
ui = MainWindow()
ui.show()

# set host 
ui.pushButton.clicked.connect(set_host)

exit(app.exec())



# OS 
host = ''

# # check os host
# if platform == 'linux' or platform == 'linux2':
#     host = 'linux'
# else:
#     if platform == 'win32':
#         host = 'win32'

# add in ansible file - hosts
# AnsibleHost.WriteOnAnsibleHostFile()

# print all hosts 
#print(AnsibleHost.GetListHosts())

# test info
#print(AnsibleHost.PingHost('Artiom'))

# Print System Info
#print(AnsibleHost.PrintSystemInfo('Artiom'))

# My Command 
#print(AnsibleHost.MyCommand('Artiom', 'dir'))