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
        btn.move(35,35)
        extractAction = QtGui.QAction(QtGui.QIcon('favicon.png'),'Quit', self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)
        
        self.show()
    #If we are gonna close the application, we need to give them a reconfirm message
    #therefore we keep it in the close application method
    def close_application(self):
        #second parameter is title, third is message
        #4th parameter is basically a binary option yes or no
        # the | means either or
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
