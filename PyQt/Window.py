import sys
from PyQt4 import QtGui


#Basic Setup
##app = QtGui.QApplication(sys.argv)
##
##window = QtGui.QWidget()
##window.setGeometry(50,50,500,300)
##window.setWindowTitle("Learning PyQt")
##
##
##window.show()

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("System Monitoring")
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
