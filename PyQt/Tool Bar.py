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
    #Tool bars are usually specific to the page that they are on
    #Therefore, we add them to the page itself instead of the core init
    def home(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(35,35)
        #Setting up a button on the toolbar
        #You can replace the icon parameter with text if you don't want an image
        #First parameter is the icon, second is the hover message, third is self
        extractAction = QtGui.QAction(QtGui.QIcon('favicon.png'),'Quit', self)
        extractAction.triggered.connect(self.close_application)

        #This sets up the toolbar
        self.toolbar = self.addToolBar("Extraction")
        #Adding our button to the toolbar
        self.toolbar.addAction(extractAction)
        
        self.show()

    def close_application(self):
        sys.exit()


def run():      
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
