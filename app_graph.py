import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
import cv2 as cv
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QCalendarWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess 
import pandas as pd
#from splash import SplashScreen
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QDate

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
import random, datetime
from PyQt5.Qt import  *
from PyQt5.QtGui import QPixmap, QImage, QPen, QPainter

class getColorLabel(QLabel):
    def __init__(self, widget):
        super(getColorLabel, self).__init__(widget)
        self.main = widget

    def mousePressEvent(self, event):
        self.main.get(event.pos())

class stackedExample(QWidget):

   def __init__(self):
      super(stackedExample, self).__init__()
      self._image_name = ""
      self._temp = []
      self.pix_image_pricipale=QPixmap()
      self.pix_image_res=QPixmap()
      self.centralwidget = QWidget()
      self.image_crop=QLabel()
      self.logo_label=QLabel()
      self.logo_label1=QLabel()
      self.logo_label2=QLabel()
      self.loading_label = QLabel()
      self.selected_image=QLabel()
      self.exit_button = QPushButton('Exit')
      self.exit_button.setStyleSheet("QPushButton#evilButton {background-color: red;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}QPushButton#evilButton:pressed {background-color: rgb(224, 0, 0);border-style: inset;}")
      self.prev_button = QPushButton('Previous')
      
      self.movie = QMovie("loader.gif")

      self.select_button = QPushButton('Select Image')
      self.process_button = QPushButton('Process')

      self.select_button.setStyleSheet("QPushButton#evilButton {background-color: red;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}QPushButton#evilButton:pressed {background-color: rgb(224, 0, 0);border-style: inset;}")
      self.process_button.setStyleSheet("QPushButton#evilButton {background-color: red;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}")

        # Display
      self.displayLabel = QLabel(self)
      #self.displayLabel.setGeometry(500, 200, 300, 100)

      self.first_image=QLabel()
      self.res_image=getColorLabel(self)
      self.component_name=QLabel("component : ")
      self.pix=QPixmap()
      self.temperature_name=QLabel("T(C) : ")
      self.state_name=QLabel("current state : ")
      self.component=QLabel()
      self.temperature=QLabel()
      self.state=QLabel()

      self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self)

      font = QFont()
      font.setFamily(u"Segoe UI")
      font.setPointSize(10)
      font1 = QFont()
      font1.setFamily(u"Roboto Thin")
      font1.setPointSize(30)

      font2 = QFont()
      font2.setFamily(u"Segoe UI")
      font2.setPointSize(8)

      self.circularProgressBar_Main_3 = QFrame()
      self.circularProgressBar_Main_3.setObjectName(u"circularProgressBar_Main_3")
      self.circularProgressBar_Main_3.setGeometry(QRect(510, 80, 240, 240))
      self.circularProgressBar_Main_3.setStyleSheet(u"background-color: none;")
      self.circularProgressBar_Main_3.setFrameShape(QFrame.NoFrame)
      self.circularProgressBar_Main_3.setFrameShadow(QFrame.Raised)
      self.circularProgressRAM = QFrame(self.circularProgressBar_Main_3)
      self.circularProgressRAM.setObjectName(u"circularProgressRAM")
      self.circularProgressRAM.setGeometry(QRect(10, 10, 220, 220))
      self.circularProgressRAM.setStyleSheet(u"QFrame{\n"
"  border-radius: 110px;   \n"
"  background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(255, 0, 127, 255), stop:0.745 rgba(255, 255, 255, 0));\n"
"}")
      self.circularProgressRAM.setFrameShape(QFrame.StyledPanel)
      self.circularProgressRAM.setFrameShadow(QFrame.Raised)
      self.circularBg_3 = QFrame(self.circularProgressBar_Main_3)
      self.circularBg_3.setObjectName(u"circularBg_3")
      self.circularBg_3.setGeometry(QRect(10, 10, 220, 220))
      self.circularBg_3.setStyleSheet(u"QFrame{\n"
"  border-radius: 110px;   \n"
"  background-color: rgba(77, 85, 127, 100);\n"
"}")
      self.circularBg_3.setFrameShape(QFrame.StyledPanel)
      self.circularBg_3.setFrameShadow(QFrame.Raised)
      self.circularContainer_3 = QFrame(self.circularProgressBar_Main_3)
      self.circularContainer_3.setObjectName(u"circularContainer_3")
      self.circularContainer_3.setGeometry(QRect(25, 25, 190, 190))
      self.circularContainer_3.setBaseSize(QSize(0, 0))
      self.circularContainer_3.setStyleSheet(u"QFrame{\n"
"  border-radius: 95px; \n"
"  background-color: rgb(58, 58, 102);\n"
"}")
      self.circularContainer_3.setFrameShape(QFrame.StyledPanel)
      self.circularContainer_3.setFrameShadow(QFrame.Raised)
      self.layoutWidget_3 = QWidget(self.circularContainer_3)
      self.layoutWidget_3.setObjectName(u"layoutWidget_3")
      self.layoutWidget_3.setGeometry(QRect(10, 40, 171, 125))
      self.infoLayout_3 = QGridLayout(self.layoutWidget_3)
      self.infoLayout_3.setObjectName(u"infoLayout_3")
      self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
      self.labelAplicationName_3 = QLabel(self.layoutWidget_3)
      self.labelAplicationName_3.setObjectName(u"labelAplicationName_3")
      self.labelAplicationName_3.setFont(font)
      self.labelAplicationName_3.setStyleSheet(u"color: #FFFFFF; background-color: none;")
      self.labelAplicationName_3.setAlignment(Qt.AlignCenter)

      self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)

      self.labelPercentageRAM = QLabel(self.layoutWidget_3)
      self.labelPercentageRAM.setObjectName(u"labelPercentageRAM")
      self.labelPercentageRAM.setFont(font1)
      self.labelPercentageRAM.setStyleSheet(u"color: rgb(255, 44, 174); padding: 0px; background-color: none;")
      self.labelPercentageRAM.setAlignment(Qt.AlignCenter)
      self.labelPercentageRAM.setIndent(-1)

      self.infoLayout_3.addWidget(self.labelPercentageRAM, 1, 0, 1, 1)

      self.circularBg_3.raise_()
      self.circularProgressRAM.raise_()
      self.circularContainer_3.raise_()
      self.labelAplicationName_3.setText(QCoreApplication.translate("MainWindow", u"<strong>Temperature</strong>", None))
      #self.labelPercentageRAM.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">25</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))

      #second
      self.circularProgressBar_Main_2 = QFrame()
      self.circularProgressBar_Main_2.setObjectName(u"circulalayoutWidgetrProgressBar_Main_2")
      self.circularProgressBar_Main_2.setGeometry(QRect(260, 80, 240, 240))
      self.circularProgressBar_Main_2.setStyleSheet(u"background-color: none;")
      self.circularProgressBar_Main_2.setFrameShape(QFrame.NoFrame)
      self.circularProgressBar_Main_2.setFrameShadow(QFrame.Raised)
      self.circularProgressGPU = QFrame(self.circularProgressBar_Main_2)
      self.circularProgressGPU.setObjectName(u"circularProgressGPU")
      self.circularProgressGPU.setGeometry(QRect(10, 10, 220, 220))
      self.circularProgressGPU.setStyleSheet(u"QFrame{\n"
"  border-radius: 110px;   \n"
"  background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.600 rgba(85, 255, 127, 255), stop:0.595 rgba(255, 255, 255, 0));\n"
"}")
      self.circularProgressGPU.setFrameShape(QFrame.StyledPanel)
      self.circularProgressGPU.setFrameShadow(QFrame.Raised)
      self.circularBg_2 = QFrame(self.circularProgressBar_Main_2)
      self.circularBg_2.setObjectName(u"circularBg_2")
      self.circularBg_2.setGeometry(QRect(10, 10, 220, 220))
      self.circularBg_2.setStyleSheet(u"QFrame{\n"
"  border-radius: 110px;   \n"
"  background-color: rgba(85, 85, 127, 100);\n"
"}")
      self.circularBg_2.setFrameShape(QFrame.StyledPanel)
      self.circularBg_2.setFrameShadow(QFrame.Raised)
      self.circularContainer_2 = QFrame(self.circularProgressBar_Main_2)
      self.circularContainer_2.setObjectName(u"circularContainer_2")
      self.circularContainer_2.setGeometry(QRect(25, 25, 190, 190))
      self.circularContainer_2.setBaseSize(QSize(0, 0))
      self.circularContainer_2.setStyleSheet(u"QFrame{\n"
"  border-radius: 95px; \n"
"  background-color: rgb(58, 58, 102);\n"
"}")
      self.circularContainer_2.setFrameShape(QFrame.StyledPanel)
      self.circularContainer_2.setFrameShadow(QFrame.Raised)
      self.layoutWidget_2 = QWidget(self.circularContainer_2)
      self.layoutWidget_2.setObjectName(u"layoutWidget_2")
      self.layoutWidget_2.setGeometry(QRect(10, 40, 171, 127))
      self.infoLayout_2 = QGridLayout(self.layoutWidget_2)
      self.infoLayout_2.setObjectName(u"infoLayout_2")
      self.infoLayout_2.setContentsMargins(0, 0, 0, 0)
      self.labelAplicationName_2 = QLabel(self.layoutWidget_2)
      self.labelAplicationName_2.setObjectName(u"labelAplicationName_2")
      self.labelAplicationName_2.setFont(font)
      self.labelAplicationName_2.setStyleSheet(u"color: #FFFFFF; background-color: none;")
      self.labelAplicationName_2.setAlignment(Qt.AlignCenter)

      self.infoLayout_2.addWidget(self.labelAplicationName_2, 0, 0, 1, 1)

      self.labelPercentageGPU = QLabel(self.layoutWidget_2)
      self.labelPercentageGPU.setObjectName(u"labelPercentageGPU")
      self.labelPercentageGPU.setFont(font1)
      self.labelPercentageGPU.setStyleSheet(u"color: rgb(115, 255, 171); padding: 0px; background-color: none;")
      self.labelPercentageGPU.setAlignment(Qt.AlignCenter)
      self.labelPercentageGPU.setIndent(-1)

      self.infoLayout_2.addWidget(self.labelPercentageGPU, 1, 0, 1, 1)

      self.labelCredits_2 = QLabel(self.layoutWidget_2)
      self.labelCredits_2.setObjectName(u"labelCredits_2")
      self.labelCredits_2.setFont(font2)
      self.labelCredits_2.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
      self.labelCredits_2.setAlignment(Qt.AlignCenter)

      self.infoLayout_2.addWidget(self.labelCredits_2, 2, 0, 1, 1)
      self.labelAplicationName_2.setText(QCoreApplication.translate("MainWindow", u"<strong>Equipement</strong>", None))
      #self.labelCredits_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">60\u00ba</span></p></body></html>", None))

      self.circularBg_2.raise_()
      self.circularProgressGPU.raise_()
      self.circularContainer_2.raise_()




      self.circularProgressBar_Main = QFrame()
      self.circularProgressBar_Main.setObjectName(u"circularProgressBar_Main")
      self.circularProgressBar_Main.setGeometry(QRect(10, 80, 240, 240))
      self.circularProgressBar_Main.setStyleSheet(u"background-color: none;")
      self.circularProgressBar_Main.setFrameShape(QFrame.NoFrame)
      self.circularProgressBar_Main.setFrameShadow(QFrame.Raised)
      self.circularProgressCPU = QFrame(self.circularProgressBar_Main)
      self.circularProgressCPU.setObjectName(u"circularProgressCPU")
      self.circularProgressCPU.setGeometry(QRect(10, 10, 220, 220))
      self.circularProgressCPU.setStyleSheet(u"QFrame{\n"
"  border-radius: 110px;   \n"
"  background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
      self.circularProgressCPU.setFrameShape(QFrame.StyledPanel)
      self.circularProgressCPU.setFrameShadow(QFrame.Raised)
      self.circularBg = QFrame(self.circularProgressBar_Main)
      self.circularBg.setObjectName(u"circularBg")
      self.circularBg.setGeometry(QRect(10, 10, 220, 220))
      self.circularBg.setStyleSheet(u"QFrame{\n"
"  border-radius: 110px;   \n"
"  background-color: rgba(85, 85, 127, 100);\n"
"}")
      self.circularBg.setFrameShape(QFrame.StyledPanel)
      self.circularBg.setFrameShadow(QFrame.Raised)
      self.circularContainer = QFrame(self.circularProgressBar_Main)
      self.circularContainer.setObjectName(u"circularContainer")
      self.circularContainer.setGeometry(QRect(25, 25, 190, 190))
      self.circularContainer.setBaseSize(QSize(0, 0))
      self.circularContainer.setStyleSheet(u"QFrame{\n"
"  border-radius: 95px; \n"
"  background-color: rgb(58, 58, 102);\n"
"}")
      self.circularContainer.setFrameShape(QFrame.StyledPanel)
      self.circularContainer.setFrameShadow(QFrame.Raised)
      self.layoutWidget = QWidget(self.circularContainer)
      self.layoutWidget.setObjectName(u"layoutWidget")
      self.layoutWidget.setGeometry(QRect(10, 40, 171, 125))
      self.infoLayout = QGridLayout(self.layoutWidget)
      self.infoLayout.setObjectName(u"infoLayout")
      self.infoLayout.setContentsMargins(0, 0, 0, 0)
      self.labelAplicationName = QLabel(self.layoutWidget)
      self.labelAplicationName.setObjectName(u"labelAplicationName")
      font = QFont()
      font.setFamily(u"Segoe UI")
      font.setPointSize(10)
      self.labelAplicationName.setFont(font)
      self.labelAplicationName.setStyleSheet(u"color: #FFFFFF; background-color: none;")
      self.labelAplicationName.setAlignment(Qt.AlignCenter)

      self.infoLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)

      self.labelPercentageCPU = QLabel(self.layoutWidget)
      self.labelPercentageCPU.setObjectName(u"labelPercentageCPU")
      font1 = QFont()
      font1.setFamily(u"Roboto Thin")
      font1.setPointSize(30)
      self.labelPercentageCPU.setFont(font1)
      self.labelPercentageCPU.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
      self.labelPercentageCPU.setAlignment(Qt.AlignCenter)
      self.labelPercentageCPU.setIndent(-1)

      self.infoLayout.addWidget(self.labelPercentageCPU, 1, 0, 1, 1)

      self.labelCredits = QLabel(self.layoutWidget)
      self.labelCredits.setObjectName(u"labelCredits")
      font2 = QFont()
      font2.setFamily(u"Segoe UI")
      font2.setPointSize(8)
      self.labelCredits.setFont(font2)
      self.labelCredits.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
      self.labelCredits.setAlignment(Qt.AlignCenter)

      self.infoLayout.addWidget(self.labelCredits, 2, 0, 1, 1)
      self.labelAplicationName.setText(QCoreApplication.translate("MainWindow", u"<strong>Current State</strong>", None))
      
      self.circularBg.raise_()
      self.circularProgressCPU.raise_()
      self.circularContainer.raise_()


      #graph and calendar

      self.cal = QCalendarWidget()
      self.cal.setGridVisible(True)
      self.date = self.cal.selectedDate()

      self.plot = QChart()
      self.chart_view = QChartView(self.plot)
      self.chart_view.setRenderHint(QPainter.Antialiasing)

      self.series = QSplineSeries()
      self.candle_series = QCandlestickSeries()
      self.plot.addSeries(self.series)
      self.plot.addSeries(self.candle_series)
      self.plot.setAnimationOptions(QChart.SeriesAnimations)
      self.plot.setTitle("Evolution of global temperature ")

      self.plot.legend().setVisible(True)
      self.plot.legend().setAlignment(Qt.AlignBottom)
      self.plot.legend().hide()
      self.candle_series.setDecreasingColor(Qt.green)
      self.candle_series.setIncreasingColor(Qt.red)

      self.axis_x =QDateTimeAxis()
      self.axis_x.setTickCount(24)
      self.axis_x.setLabelsAngle(0)
      self.axis_x.setFormat("h")
      self.axis_x.setTitleText("Hour")
      self.axis_x.setMax(datetime.datetime.strptime('2020050723','%Y%m%d%H'))
      self.axis_x.setMin(datetime.datetime.strptime('2020050700','%Y%m%d%H'))
      self.axis_y = QValueAxis()
      self.axis_y.setTickCount(6)
      self.axis_y.setLabelFormat("%i")
      self.axis_y.setTitleText("Temperature [celcious]")
      self.axis_y.setMax(70)
      self.axis_y.setMin(10)
      self.plot.setAxisX(self.axis_x, self.series)
      self.plot.setAxisY(self.axis_y, self.series)
      self.plot.setAxisX(self.axis_x,self.candle_series)
      self.plot.setAxisY(self.axis_y,self.candle_series)      





      self.stack1 = QWidget()
      self.stack2 = QWidget()

      
      self.stack1UI()
      
      self.stack2UI()

      self.exit_button.clicked.connect(self.display_1)
      self.prev_button.clicked.connect(self.display_2)
      self.select_button.clicked.connect(self.display_image_first)
      self.process_button.clicked.connect(self.process_game)


      self.Stack = QStackedWidget (self)
      self.Stack.addWidget (self.stack1)
      self.Stack.addWidget (self.stack2)
        
      hbox = QHBoxLayout()
      hexit = QVBoxLayout()
      vbox = QVBoxLayout(self)

      a="logo_FS.png"
      pix=QPixmap(a)
      self.logo_label.setAlignment(Qt.AlignLeft)
      self.logo_label.setPixmap(pix)
      self.logo_label.resize(pix.width(),pix.height())
      a="logo_limiarf.png"
      pix=QPixmap(a)
      self.logo_label1.setAlignment(Qt.AlignRight)
      self.logo_label1.setPixmap(pix)
      self.logo_label1.resize(pix.width(),pix.height())
      a="p_m_logo.png"
      pix=QPixmap(a)
      self.logo_label2.setAlignment(Qt.AlignCenter)
      self.logo_label2.setPixmap(pix)
      self.logo_label2.resize(pix.width(),pix.height())

      hexit.addWidget(self.logo_label2)
      hexit.addWidget(self.exit_button)
      hbox.addWidget(self.logo_label)
      #hbox.addWidget(self.logo_label2)
      hexit.setAlignment(Qt.AlignRight )
      hbox.addLayout(hexit)

      #hbox.addWidget(self.prev_button)
      #hbox.addWidget(self.logo_label1)
      vbox.addLayout(hbox)

      vbox.addWidget(self.Stack)
      self.exit_button.setHidden(True)
      self.setLayout(vbox)
     
      self.setGeometry(300, 50, 1200,800)
      self.setStyleSheet(u"background-color: rgb(192, 192, 192);")
      self.setWindowTitle('Predictive Maintenance')
      self.show()



   def get(self, pos):

      csv_name=self.get_image_name()

      csv_name=csv_name.split("data/rgb/")
      csv_name=csv_name[1].split(".")
      csv_name='data/csv/'+csv_name[0]+'.csv'
      df = pd.read_csv(csv_name, index_col=False)
      list_of_lists = []
      with open('save.txt') as f:
         for line in f:
               inner_list = [elt.strip() for elt in line.split(' ')]
               list_of_lists.append(inner_list)
      names=['circuit_breaker', 'contactor', 'motor_pump', 'motor_starter', 'relay', 'tansformer', 'thermal_relay', 'transformer']

      xmin_arr=[]
      ymin_arr=[]
      xmax_arr=[]
      ymax_arr=[]
      labels_arr=[]
      for line in list_of_lists:
         labels_arr.append(int(line[0]))
         xmin_arr.append(int(line[1]))
         ymin_arr.append(int(line[2]))
         xmax_arr.append(int(line[3]))
         ymax_arr.append(int(line[4])) 
             
      label_name=""

      
      croped_image=QLabel()
      a=self.get_image_name()
      pixx=QPixmap(a)
      croped_image.setPixmap(pixx)
      
      croped_image.resize(pixx.width(),pixx.height())
      for x in range(len(xmax_arr)):

         # Cropping an image



         mask = (df['x'] >= ymin_arr[x]) & (df['x'] <= ymax_arr[x] )
         mask2 = (df['y'] >= xmin_arr[x]) & (df['y'] <= xmax_arr[x] )
         df2 = df.loc[mask]
         df3 = df2.loc[mask2]

         
         position="pos "+str(pos.x())+" "+str(pos.y())
         #print(position)
         if(pos.x()>xmin_arr[x] and pos.x()<xmax_arr[x] and (pos.y()>ymin_arr[x] and pos.y()<ymax_arr[x] ) ):
            self.set_temp(df3['temp (c)'].values)
            temp=df3['temp (c)'].mean()
         
            etat=""
            labels_arr = ["Normal", "Defect", "Dangerous defect"] 
            
            if equipment == "Circuit breaker":
                if temp <= 60:
                    etat = labels_arr[0]
                elif 60 < temp <= 85:
                    etat = labels_arr[1]
                else:
                    etat = labels_arr[2]
            elif equipment == "Contactor":
                if temp <= 45:
                    etat = labels_arr[0]
                elif 45 < temp <= 60:
                    etat = labels_arr[1]
                else:
                    etat = labels_arr[2]
            elif equipment == "Motor starter":
                if 40 <= temp <= 50:
                    etat = labels_arr[0]
                elif 50 < temp <= 70:
                    etat = labels_arr[1]
                else:
                    etat = labels_arr[2]
            elif equipment == "Relay":
                if temp <= 35:
                    etat = labels_arr[0]
                elif 35 < temp <= 80:
                    etat = labels_arr[1]
                else:
                    etat = labels_arr[2]
            elif equipment == "Transformer":
                if temp <= 40:
                    etat = labels_arr[0]
                elif 40 < temp <= 65:
                    etat = labels_arr[1]
                else:
                    etat = labels_arr[2]
            elif equipment == "Motor pump":
                if temp <= 110:
                    etat = labels_arr[0]
                elif 110 < temp <= 180:
                    etat = labels_arr[1]
                elif 180 < temp <= 200:
                    etat = labels_arr[2]
                else:
                    etat = "T > 200C"
            else:
                etat = "Invalid equipment type"
            label_name=names[labels_arr[x]]+","+str("%.2f"%temp)+","+etat
            self.currentQRubberBand.setGeometry(QRect(xmin_arr[x],ymin_arr[x], xmax_arr[x]-xmin_arr[x],ymax_arr[x]-ymin_arr[x]))
            #self.currentQRubberBand.hide()
            currentQRect = self.currentQRubberBand.geometry()
            #self.currentQRubberBand.deleteLater()
         
            #print(self.get_temp())
         
            cropQPixmap = croped_image.pixmap().copy(currentQRect)
            #cropQPixmap.save('output.png')
            #tr = QTransform()
            #tr.scale(px.size().width()*1.0/self.label.size().width(), px.size().height()*1.0/self.label.size().height())
            #r = tr.mapRect(r)
            self.image_crop.setPixmap(cropQPixmap)
            self.image_crop.resize(cropQPixmap.width()*100,cropQPixmap.height()*100)

      

      self.series.clear()
      
      t_max=max(self.get_temp())
      
      t_array=np.asarray(self.get_temp())
      index_max=np.argmax(t_array)
      print(t_array)
      t_array=t_array[0:23]
      
      #
      for d in range(23):
            self.series.append(float(QtCore.QDateTime.fromString("20200507"+str(d), "yyyyMMddh").toMSecsSinceEpoch()),t_array[d],)



      #pen = QPen(QColor(200, 200, 200))
      #pen.setWidth(5)
      #self.series.setPen(pen)

      #self.displayLabel.setText(label_name)
      if(label_name != ""):
         label_name=label_name.split(",")
         #self.displayLabel.setText(label_name)
         self.component.setText(label_name[0])
         label_name_temp=label_name[1].split(".")
         self.labelPercentageRAM.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">"+label_name_temp[0]+"</span><span style=\" font-size:40pt; vertical-align:super;\">°</span></p>", None))
         self.labelPercentageGPU.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:15pt;\">"+label_name[0]+"</span><span style=\" font-size:1pt; vertical-align:super;\"></span></p>", None))
         self.labelPercentageCPU.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:20pt;\">"+label_name[2]+"</span><span style=\" font-size:1pt; vertical-align:super;\"></span></p>", None))
         self.temperature.setText(label_name[1])
         self.state.setText(label_name[2])


      t_array = np.array([])
      #


   def get_image_name(self):
        return self._image_name
    

   def set_image_name(self, x):
        self._image_name = x
   
   def get_temp(self):
        return self._temp
    

   def set_temp(self, x):
        self._temp = x

   def openFileNameDialog(self):
      options = QFileDialog.Options()
      options |= QFileDialog.DontUseNativeDialog
      fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Select Image Format (*.jpg)", options=options)
      if fileName:
         print(fileName)
      return fileName  



   def stack1UI(self):
      layout = QVBoxLayout()   
      layout_all = QVBoxLayout()   

      self.selected_image.setAlignment(Qt.AlignTop)
      self.loading_label.setAlignment(Qt.AlignBottom|Qt.AlignCenter)
      self.loading_label.setMovie(self.movie)
      
      
      layout.addWidget(self.selected_image)

      layout.addWidget(self.select_button)
      layout.addWidget(self.process_button)
      layout.addWidget(self.loading_label)

      layout.setAlignment(Qt.AlignCenter )



      self.stack1.setLayout(layout)

   def getPixel(self, event):
      x = event.pos().x()
      y = event.pos().y()
      c = self.img.pixel(x,y)  # color code (integer): 3235912
      # depending on what kind of value you like (arbitary examples)
      c_qobj = QColor(c)  # color object
      c_rgb = QColor(c).getRgb()  # 8bit RGBA: (255, 23, 0, 255)
      c_rgbf = QColor(c).getRgbf()  # RGBA float: (1.0, 0.3123, 0.0, 1.0)
      return x, y, c_rgb


   def stack2UI(self):



      


      layout_component_name = QHBoxLayout()
      layout_temperature_name = QHBoxLayout()
      layout_state_name = QHBoxLayout()

      layout_component_name.addWidget(self.component_name)
      layout_component_name.addWidget(self.component)

      layout_temperature_name.addWidget(self.temperature_name)
      layout_temperature_name.addWidget(self.temperature)

      layout_state_name.addWidget(self.state_name)
      layout_state_name.addWidget(self.state)



      layout_name = QVBoxLayout()
      layout_name.addLayout(layout_component_name)
      layout_name.addLayout(layout_temperature_name)
      layout_name.addLayout(layout_state_name)


      layout_all= QVBoxLayout()
      layout_graph= QHBoxLayout()
      layout = QHBoxLayout()
      layout_circle = QHBoxLayout()

      
      a="save.jpg"
      self.pix=QPixmap(a)
      self.res_image.setPixmap(self.pix)
      #self.res_image.setFrameStyle(QFrame.Panel | QFrame.Raised)
      self.res_image.resize(self.pix.width(),self.pix.height())
      #self.res_image.mousePressEvent = self.getPixel
      

      self.cal.setFixedSize(QSize(400, 200))
      self.cal.setStyleSheet("background-color :#ffffff ;font: bold 10px;  selection-color: rgb(0, 0, 255);"
                                    )
      date = self.cal.selectedDate()
      layout.addWidget(self.res_image)
      #layout.addLayout(layout_name)
      layout_circle.addWidget(self.circularProgressBar_Main_3)
      layout_circle.addWidget(self.circularProgressBar_Main_2)
      layout_circle.addWidget(self.circularProgressBar_Main)
      #layout_circle.addWidget(cal)

      layout.addLayout(layout_circle)

      layout_all.addLayout(layout)
      layout_graph.addWidget(self.chart_view)
      layout_graph.addWidget(self.cal)

      layout_all.addLayout(layout_graph)
      #layout_all.addWidget(self.image_crop)
      #layout_all.addWidget(self.circularProgressBar_Main_3)  
      self.stack2.setLayout(layout_all)
        

   
   def display_image_first(self):
      #self.movie.stop()
      self.loading_label.setHidden(True)
      a=self.openFileNameDialog()
      pix=QPixmap(a)
      self.selected_image.setAlignment(Qt.AlignCenter)
      self.selected_image.setPixmap(pix)
      self.selected_image.resize(pix.width(),pix.height())
      rgb_name=a.split("data/data_flir/")
      rgb_name=rgb_name[1].split(".")
      rgb_name='data/rgb/'+rgb_name[0]+'.jpg'
      print(rgb_name)

      self.set_image_name(rgb_name)

   def process_game(self):
      self.exit_button.setHidden(False)
      self.loading_label.setHidden(False)
      painter = QPainter(self)
      
      painter.drawPixmap(self.rect(), self.pix)
      pen = QPen(Qt.red, 3)
      painter.setPen(pen)
      painter.drawLine(10, 10, self.rect().width() -10 , 10)
      
      self.movie.start()
      print(self.get_image_name())

      subprocess.call("python detect.py --weights  data/best.pt --conf 0.6 --img-size 416 --save-txt --source "+self.get_image_name(), shell=True)
      a="save.jpg"


      self.pix=QPixmap(a)
      #self.displayLabel.setText("labas")
      self.res_image.setPixmap(self.pix)
      self.Stack.setCurrentIndex(1)


   def display(self,i):
      self.Stack.setCurrentIndex(i)

   
   def display_1(self):
      self.Stack.setCurrentIndex(0)
      

   def display_2(self):

      print(self.get_image_name())

      subprocess.call("python detect.py --weights  data/best.pt --conf 0.6 --img-size 416 --save-txt --source "+self.get_image_name(), shell=True)
      a="save.jpg"


      pix=QPixmap(a)
      #self.displayLabel.setText("labas")
      self.res_image.setPixmap(pix)
      self.Stack.setCurrentIndex(1)

        
def main():
   app = QApplication(sys.argv)
   ex = stackedExample()
   sys.exit(app.exec_())
    
if __name__ == '__main__':
   main()
