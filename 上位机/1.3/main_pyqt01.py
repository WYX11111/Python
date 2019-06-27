# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import serial 
import time

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_main_pyqt01 import Ui_MainWindow
from PyQt4 import QtCore, QtGui

ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1) 
print ser.isOpen() 

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print u'press'
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider.setProperty("value", self.lineEdit.text())
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_2.setProperty("value", self.lineEdit_2.text())
    
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_3.setProperty("value", self.lineEdit_3.text())
    
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_4.setProperty("value", self.lineEdit_4.text())
    
    @pyqtSignature("")
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_5.setProperty("value", self.lineEdit_5.text())
    
    @pyqtSignature("")
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_6.setProperty("value", self.lineEdit_6.text())
    
    @pyqtSignature("")
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_7.setProperty("value", self.lineEdit_7.text())
    
    @pyqtSignature("")
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_8.setProperty("value", self.lineEdit_8.text())
    
    @pyqtSignature("")
    def on_pushButton_10_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_9.setProperty("value", self.lineEdit_9.text())
    
    @pyqtSignature("")
    def on_pushButton_11_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_10.setProperty("value", self.lineEdit_10.text())
    
    @pyqtSignature("")
    def on_pushButton_12_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_11.setProperty("value", self.lineEdit_11.text())
    
    @pyqtSignature("")
    def on_pushButton_13_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_12.setProperty("value", self.lineEdit_12.text())
    
    @pyqtSignature("")
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_13.setProperty("value", self.lineEdit_13.text())
    
    @pyqtSignature("")
    def on_pushButton_15_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_14.setProperty("value", self.lineEdit_14.text())
    
    @pyqtSignature("")
    def on_pushButton_16_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_15.setProperty("value", self.lineEdit_15.text())
    
    @pyqtSignature("")
    def on_pushButton_17_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_16.setProperty("value", self.lineEdit_16.text())
    
    @pyqtSignature("")
    def on_pushButton_18_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_17.setProperty("value", self.lineEdit_17.text())

    @pyqtSignature("int")
    def on_horizontalSlider_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit.setText(str(value))
        ser.write("#016P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_2_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_2.setText(str(value))
        ser.write("#006P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_3_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_3.setText(str(value))
        ser.write("#007P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_4_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_4.setText(str(value))
        ser.write("#005P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_5_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_5.setText(str(value))
        ser.write("#015P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_6_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_6.setText(str(value))
        ser.write("#014P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_7_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_7.setText(str(value))
        ser.write("#013P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_8_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_8.setText(str(value))
        ser.write("#004P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_9_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_9.setText(str(value))
        ser.write("#012P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_10_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_10.setText(str(value))
        ser.write("#003P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_11_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_11.setText(str(value))
        ser.write("#011P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_12_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_12.setText(str(value))
        ser.write("#002P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_13_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_13.setText(str(value))
        ser.write("#010P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_14_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_14.setText(str(value))
        ser.write("#009P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_15_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_15.setText(str(value))
        ser.write("#001P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_16_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_16.setText(str(value))
        ser.write("#000P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("int")
    def on_horizontalSlider_17_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit_17.setText(str(value))
        ser.write("#008P")
        ser.write(str(value))
        ser.write("T0200!\n\r")
    
    @pyqtSignature("")
    def on_re_clicked(self):
        """
        Slot documentation goes here.
        """
        self.horizontalSlider_17.setProperty("value", 1500)
        self.horizontalSlider_16.setProperty("value", 1500)
        self.horizontalSlider_15.setProperty("value", 1500)
        self.horizontalSlider_14.setProperty("value", 1500)
        self.horizontalSlider_13.setProperty("value", 1500)
        self.horizontalSlider_12.setProperty("value", 1500)
        self.horizontalSlider_11.setProperty("value", 1500)
        self.horizontalSlider_10.setProperty("value", 1500)
        self.horizontalSlider_9.setProperty("value", 1500)
        self.horizontalSlider_8.setProperty("value", 1500)
        self.horizontalSlider_7.setProperty("value", 1500)
        self.horizontalSlider_6.setProperty("value", 1500)
        self.horizontalSlider_5.setProperty("value", 1500)
        self.horizontalSlider_4.setProperty("value", 1500)
        self.horizontalSlider_3.setProperty("value", 1500)
        self.horizontalSlider_2.setProperty("value", 1500)
        self.horizontalSlider.setProperty("value", 1500)
        self.lineEdit_17.setText('1500')
        self.lineEdit_16.setText('1500')
        self.lineEdit_15.setText('1500')
        self.lineEdit_14.setText('1500')
        self.lineEdit_13.setText('1500')
        self.lineEdit_12.setText('1500')
        self.lineEdit_11.setText('1500')
        self.lineEdit_10.setText('1500')
        self.lineEdit_9.setText('1500')
        self.lineEdit_8.setText('1500')
        self.lineEdit_7.setText('1500')
        self.lineEdit_6.setText('1500')
        self.lineEdit_5.setText('1500')
        self.lineEdit_4.setText('1500')
        self.lineEdit_3.setText('1500')
        self.lineEdit_2.setText('1500')
        self.lineEdit.setText('1500')
        ser.write("#000P1500T1000!#001P1500T1000!#002P1500T1000!#003P1500T1000!#004P1500T1000!#005P1500T1000!#006P1500T1000!#007P1500T1000!#008P1500T1000!#009P1500T1000!#010P1500T1000!#011P1500T1000!#012P1500T1000!#013P1500T1000!#014P1500T1000!#015P1500T1000!#016P1500T1000!\n\r")
		

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
