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

        #Creating the check box
        checkBox = QtGui.QCheckBox('Enlarge Window',self)
        #Moving the checkbox to the desired location
        checkBox.move(100,25)
        #This makes it so that the checkbox is checked from the get go
        #However, this won't make the action occur because we are checking for
        #STATE CHANGED in the line below. Therefore, we can just switch the
        #conditions around in our enlarge_window function
        'checkBox.toggle()'
        #Setting what the checkBox does when it is active
        checkBox.stateChanged.connect(self.enlarge_window)
    
        #Everything has to go before the self.show()
        self.show()

        #This is the action that we define for when the checkbox is active
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
