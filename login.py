import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
#from auth import *
#from capture import *
#import picamera

import Qrc_files.login_rc

class WelcomePage(QMainWindow):
    def __init__(self):
        super(WelcomePage,self).__init__()
        loadUi("Ui_files/loginbtn.ui",self)
        self.login.clicked.connect(self.goToLogin)

    def goToLogin(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Ui_files/loginpage.ui",self)
        #self.login.clicked.connect(self.loginfunction)
        self.login.clicked.connect(self.GoToCommonWin)
        self.back.clicked.connect(self.goBack)

    # def loginfunction(self):
    #     email=self.email.text()
    #     password=self.password.text()
    #     loginStatus=login(email,password)
    #     if loginStatus==1:
    #         widget.setCurrentIndex(widget.currentIndex()+1)

    def GoToCommonWin(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class Common(QMainWindow):
    def __init__(self):
        super(Common,self).__init__()
        loadUi("Ui_files/commonwin.ui",self)
        self.samplecol.clicked.connect(self.goToSampleCol)
        self.defectcol.clicked.connect(self.goToModwin)
        self.back.clicked.connect(self.goBack)
        
    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def goToSampleCol(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goToModwin(self):
        widget.setCurrentIndex(widget.currentIndex()+4)


class ClassWin(QMainWindow):
    def __init__(self):
        super(ClassWin,self).__init__()
        loadUi("Ui_files/classwin.ui",self)
        self.defect_samples.clicked.connect(self.goToDefectCol)
        self.non_defective_samples.clicked.connect(self.goToNonDefectCol)
        self.back.clicked.connect(self.goBack)

    # def cam(self):
    #     self.camera=picamera.PiCamera()
    #     self.camera.start_preview(fullscreen=False,window=(21,21,600,440))

    def goToDefectCol(self):
        # self.path="defective_images"
        # self.cam()
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToNonDefectCol(self):
        # self.cam()
        # self.path="non_defective_images"
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class CaptureWin(QMainWindow):
    def __init__(self):
        super(CaptureWin,self).__init__()
        loadUi("Ui_files/capture.ui",self)
        self.capture.clicked.connect(self.goToImageWork)

    def goToImageWork(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    # def capture_img(self):
    #      file = open("data.bin", "r")
    #      i=int(file.read())
        
    #      self.img_name="images/sample_images/"+classwin.path+"/img" + str(i)+'.jpg'
    #      print(self.img_name)
    #      classwin.camera.capture(self.img_name)
    #      classwin.camera.stop_preview()
    #      imgwrk.display_img()
    #      f = open("data.bin", "w")
    #      i=i+1
    #      f.write(str(i))
    #      f.close()
         
    #      widget.setCurrentIndex(widget.currentIndex()+1)

class ImageWork(QMainWindow):
    def __init__(self):
        super(ImageWork,self).__init__()
        loadUi("Ui_files/image_work.ui",self)
        self.retakebtn.clicked.connect(self.reTake)
        
    def reTake(self):
        file = open("data.bin", "r")
        i=int(file.read())
        
        f = open("data.bin", "w")
        i=i-1
        f.write(str(i))
        f.close()
        widget.setCurrentIndex(widget.currentIndex()-1)
        
    def display_img(self):
        self.capture_img.setScaledContents(True)
        pixmap = QPixmap(capturewin.img_name)
        self.capture_img.setPixmap(pixmap)
        self.capture_img.repaint()
        QApplication.processEvents()
        
class DefectDetection(QMainWindow):
    def __init__(self):
        super(DefectDetection,self).__init__()
        loadUi("Ui_files/modwin.ui",self)
        self.selectmodelbtn.clicked.connect(self.ShowDriveFolder)
        self.deploymodelbtn.clicked.connect(self.DeployModel)
        self.continuebtn.clicked.connect(self.goToPredWin)
        self.back.clicked.connect(self.goBack)
        
    def ShowDriveFolder(self):
        pass
    
    def DeployModel(self):
        pass
        
    def goToPredWin(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-4)
        
class PredictionWin(QMainWindow):
    def __init__(self):
        super(PredictionWin,self).__init__()
        loadUi("Ui_files/Predictionwin.ui",self)
        self.back.clicked.connect(self.goBack)

    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        
app=QApplication(sys.argv)
mainwindow=WelcomePage()
log=Login()
common=Common()
classwin=ClassWin()
capturewin=CaptureWin()
imgwrk=ImageWork()
defectdetection=DefectDetection()
predictionwin=PredictionWin()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(log)
widget.addWidget(common)
widget.addWidget(classwin)
widget.addWidget(capturewin)
widget.addWidget(imgwrk)
widget.addWidget(defectdetection)
widget.addWidget(predictionwin)
widget.setFixedWidth(800)
widget.setFixedHeight(480)
widget.show()
app.exec_()

