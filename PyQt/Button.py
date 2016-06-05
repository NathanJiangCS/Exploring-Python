import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    #This is what is core applications
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("System Monitoring")
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.home()
    #Button 
    def home(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)

        #Moving and resizing buttons
        #btn.resize(100,100)
        #or this gives the suggested size
        #btn.resize(btn.sizeHint())
        #or this gives the minimum size possible
        btn.resize(btn.minimumSizeHint())
        #btn.move(100,100)
        
        #Displaying button
        self.show()

    #Defining the method/ event that occurs
    def close_application(self):
        sys.exit()


def run():      
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
