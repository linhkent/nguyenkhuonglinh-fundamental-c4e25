import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import  *
from random import choice
import back_color
import time



class GameWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.shapes = back_color.get_shapes()
        self.initBoard()
        self.generate_quiz()
        self.initUI()
        self.initTimer()
        self.initSound()
        self.score = 0
        self.chk = True
        self.play = True
      
    

    def initSound(self):
        self.correctSound = QSound('sound/correct.wav')
        self.incorrectSound = QSound('sound/incorrect.wav')


    def initTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timerTick)


    def timerTick(self):
        self.timer.stop()
        self.shapes = back_color.get_shapes()
        self.generate_quiz()
        self.repaint()


    def initUI(self):
        self.text = "Back color"
        self.setGeometry(0, 0, 260, 340)
        self.setFixedSize(260, 340)
        self.show()
       
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(event.rect(), QBrush(QColor("#FFFFFF")))
        if self.quiz_type:
                textRect = QRectF(0, 0, 260, 60)
        else:
                textRect = QRectF(0, 280, 260, 60)
        if self.chk:
            self.yes.hide()
            self.no.hide()           
            for shape in self.shapes:
                brush = QBrush(QColor(shape['color']))
                rect = shape['rect']
                qp.fillRect(rect[0], rect[1], rect[2], rect[3], brush)                      
            qp.setPen(QColor("#2209E2"))
            qp.setFont(QFont('Arial', 12, QFont.Bold))
            qp.drawText(QRectF(0, 0, 260, 340), Qt.AlignTop | Qt.AlignRight, 'Score: '+str(self.score))
            qp.setPen(QColor(self.quiz_color))
            qp.setFont(QFont('Times New Roman', 20, QFont.Bold))
            qp.drawText(textRect, Qt.AlignCenter, self.quiz_text)
        else:    
            self.yes.show()
            self.no.show()         
            qp.setPen(QColor("#2209E2"))
            qp.setFont(QFont('Arial', 20, QFont.Bold))
            qp.drawText(QRectF(0, 60, 260, 60), Qt.AlignCenter, 'GAME OVER')
            qp.drawText(QRectF(0, 60, 260, 130), Qt.AlignCenter, 'Score: '+str(self.score))
            qp.drawText(QRectF(0, 60, 260, 200), Qt.AlignCenter, 'Play again?')
        qp.end()
    
    def initBoard(self):
        yes_x = 25
        yes_y = 220

        no_x = 140
        no_y = 220

        self.yes = QPushButton("", self)
        self.yes.setGeometry(yes_x, yes_y, 80, 80)
        self.yes.setIcon(QIcon(".//icon/yes.png"))
        self.yes.clicked.connect(self.handleYes)
        self.yes.setIconSize(QSize(80, 80))

        self.no = QPushButton("", self)
        self.no.setGeometry(no_x, no_y, 80, 80)
        self.icon = QIcon(".//icon/no.png")
        self.no.setIcon(self.icon)
        self.no.setIconSize(QSize(80, 80))
        self.no.clicked.connect(qApp.quit)
        
        
    def handleYes(self):
        self.chk = True
        self.score = 0
        self.repaint()

    def generate_quiz(self):
        [self.quiz_text, self.quiz_color, self.quiz_type] = back_color.generate_quiz()

    
    def mouseReleaseEvent(self, mouseEvent):
        x = mouseEvent.x()
        y = mouseEvent.y()
        if back_color.mouse_press(x, y, self.quiz_text, self.quiz_color, self.quiz_type):
            self.quiz_text = 'Correct'
            self.correctSound.play()
            self.score += 1
        else:                
            self.quiz_text = 'Incorrect'
            self.incorrectSound.play()
            self.repaint()                
            time.sleep(1)                
            self.chk = False
                            
        self.timer.start()
        self.repaint()   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GameWindow()
    sys.exit(app.exec_())
