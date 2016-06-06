import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("System Monitoring")
        self.setWindowIcon(QtGui.QIcon('favicon.png'))

        extractAction = QtGui.QAction('&Quit', self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        self.home()

    def home(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(35,65)
        extractAction = QtGui.QAction(QtGui.QIcon('favicon.png'),'Quit', self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)

        checkBox = QtGui.QCheckBox('Enlarge Window',self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,200,10)
        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)
        #Initiating the stylem, it defaults to Windows
        self.styleChoice = QtGui.QLabel("Windows", self)
        #To find out what style it is on currently, you can do
        'print self.style().objectName()'
        #Different styles available with PyQt
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("Windows")
        comboBox.addItem("motif")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        #Moving the style dropdown
        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        #connecting our drop down selection to the actual action of changing styles
        comboBox.activated[str].connect(self.style_choice)

        self.show()
    #Action of changing styles
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
        
        self.show()
        
    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50, 50, 500, 300)
    
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Confirm',
                                            "Are you sure you want to quit",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass



def run():      
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
