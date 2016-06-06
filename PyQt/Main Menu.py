import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    #We usually put the main menu in the init method because
    #it doesnt change when the screen changes
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("System Monitoring")
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        
        #Defining our MenuBar Dropdown Action
        #Copy these 4 lines to make another action
        extractAction = QtGui.QAction('&Quit', self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)
        #Initiating menu bar
        self.statusBar()
        mainMenu = self.menuBar()
        #Adding the File option to the menu bar
        fileMenu = mainMenu.addMenu('&File')
        #Adding the extractAction defined previously to the fileMenu
        fileMenu.addAction(extractAction)
        
        
        self.home()
    def home(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100,100)

        self.show()

    def close_application(self):
        sys.exit()


def run():      
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
