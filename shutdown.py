import sys
from PyQt5 import QtWidgets
import shutGUI
import subprocess as sp

class shutApp(QtWidgets.QMainWindow, shutGUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.turnOff.clicked.connect(self.down)
        self.cancel.clicked.connect(self.off)

    def down(self):
        if self.seconds.isChecked():
            seconds = str(int(self.timer.toPlainText()))
        elif self.minutes.isChecked():
            seconds = str(int(self.timer.toPlainText()) * 60)
        elif self.hours.isChecked():
            seconds = str(int(self.timer.toPlainText()) * 3600)
        sp.call(['shutdown', '-f', '-s', '-t', seconds])
    
    def off(self):
        sp.call(['shutdown', '/a'])
        

    


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = shutApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()