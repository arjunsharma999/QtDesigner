from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        # MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        # MainWindow.setMaximumSize(QtCore.QSize(1024, 600))  # Prevent resizing larger
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: rgb(255, 170, 127);")
        self.centralwidget.setObjectName("centralwidget")
        
        # Fix: Position widget properly within the central widget bounds
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1024, 600))  # Fill the entire central widget
        self.widget.setStyleSheet("background-color: #17AEAA;")
        self.widget.setObjectName("widget")
        
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(40, 30, 944, 540))  # Adjusted to fit within widget
        self.frame_2.setStyleSheet("border: 1px ;\n"
                                 "border-radius: 40px; \n"
                                 "background-color: #FFF6ED;\n"
                                 "align-items: center;")
        self.frame_2.setObjectName("frame_2")
        
        self.widget_3 = QtWidgets.QWidget(self.frame_2)
        self.widget_3.setGeometry(QtCore.QRect(90, 310, 91, 51))
        self.widget_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                  "background-color: #17AEAA;\n"
                                  "border-radius: 14px")
        self.widget_3.setObjectName("widget_3")
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 71, 31))  # Adjusted to fit within widget_3
        self.textBrowser_2.setObjectName("textBrowser_2")
        
        self.widget_4 = QtWidgets.QWidget(self.frame_2)
        self.widget_4.setGeometry(QtCore.QRect(200, 310, 91, 51))
        self.widget_4.setStyleSheet("background-color: #17AEAA;\n"
                                  "border-radius: 14px;")
        self.widget_4.setObjectName("widget_4")
        
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(860, 20, 31, 31))
        self.label.setText("")
        # Note: Update these paths to your actual image locations
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Desktop/Downloads/settings.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(760, 20, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Desktop/Downloads/user.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(810, 20, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/Desktop/Downloads/report.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 91, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/Desktop/Desktop/aa-120x120.webp"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(80, 180, 491, 91))
        self.textBrowser.setStyleSheet("color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(720, 490, 171, 22))
        self.dateTimeEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "font-size: 13pt;")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_2.setHtml(_translate("MainWindow", 
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
            "<span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">HOME</span></p></body></html>"))
        
        self.textBrowser.setHtml(_translate("MainWindow",
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
            "<span style=\" font-family:'Consolas'; font-size:45pt;\">Welcome, Admin</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


