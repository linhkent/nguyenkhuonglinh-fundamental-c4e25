import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initBoard()
    
    def initBoard(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        yes_x = 25
        yes_y = 30

        no_x = 140
        no_y = 30

        self.yes = QPushButton("", self)
        self.yes.setGeometry(yes_x, yes_y, 25, 25)
        self.yes.setIcon(QIcon(".//icon/yes.png"))
        self.yes.clicked.connect(self.on_click)
        self.yes.setIconSize(QSize(25, 25))

        self.no = QPushButton("", self)
        self.no.setGeometry(no_x, no_y, 25, 25)
        self.icon = QIcon(".//icon/no.png")
        self.no.setIcon(self.icon)
        self.no.setIconSize(QSize(25, 25))
        self.no.clicked.connect(qApp.quit)
    
        self.show()
    
    # @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(event.rect(), QBrush(QColor("#FFFFFF")))
        qp.setPen(QColor("#2209E2"))
        qp.setFont(QFont('Arial', 20, QFont.Bold))
        qp.drawText(QRectF(0, 60, 260, 140), Qt.AlignCenter, 'GAME OVER')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())