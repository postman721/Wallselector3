
#!/usr/bin/env python3

#Wallselector3 Copyright (c) 2019 JJ Posti <techtimejourney.net> 
#Wallselector3  comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")

#This is a simple wallpaper switching program. Coded with Python3 and Qt5. Requires feh.  



import os, sys, sys, subprocess, getpass
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setStyleSheet("*{color:#ffffff; background-color:#2f2e2d; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
"*:selected{background-color:#125c8c;}") 
        self.openFileNameDialog()
           
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose wallpaper", "/usr/share/wallpapers","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            subprocess.Popen(['feh', '--bg-scale', fileName])
            name=getpass.getuser()
            uhome="/home/"
            wall="/.wall/wall.sh"        
            combine=uhome + name + wall
            folder=uhome+name 
            fehcommand="feh --bg-scale "
            subprocess.Popen(['rm', '-r' , combine])
            subprocess.Popen(['touch', combine])
            os.chdir(folder)
            f = open(combine, 'a')
            f.write(fehcommand)
            f.write(fileName)
            f.write('\n')
            f.write('\n')
            f.close()
            sys.exit()
        else:
            sys.exit()			                 
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
