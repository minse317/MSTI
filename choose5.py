#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import main
import choose4

import result_floral
import result_tobacco_leather
import result_aqua
import result_musk
import result_green
import result_woody
import result_gourmans
import result_fruity

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChooseWindow(QWidget):
    result5 = []
    def __init__(self):
        super().__init__()
        self.choose5UI()

    def choose5UI(self):
        self.setStyleSheet('background-color: #efebf3')
        self.setWindowTitle('CHOOSE')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)

        # creating questions widget
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap('image/choice/question/feel.png'))
        self.label.resize(750, 100)
        self.label.move(160, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.calmtBtn = QLabel('', self)
        self.calmtBtn.setPixmap(QPixmap('image/choice/answer/차분함.png'))
        self.calmtBtn.resize(150, 100)
        self.calmtBtn.move(270, 380)
        self.calmtBtn.setAlignment(Qt.AlignCenter)
        self.calmtBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.calmtBtn).connect(self.click_show12)

        self.livelyBtn = QLabel('', self)
        self.livelyBtn.setPixmap(QPixmap('image/choice/answer/생동감.png'))
        self.livelyBtn.resize(150, 100)
        self.livelyBtn.move(600, 380)
        self.livelyBtn.setAlignment(Qt.AlignCenter)
        self.livelyBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.livelyBtn).connect(self.click_show13)

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/line.png'))
        self.product2.resize(1000, 15)
        # self.product2.move(140, 45)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정


    def click_show12(self):
        self.result5 = choose4.ChooseWindow.result4
        self.result5.append(1)
        self.showResult()

    def click_show13(self):
        self.result5 = choose4.ChooseWindow.result4
        self.result5.append(2)
        self.showResult()

    def showResult(self):
        if self.result5 == [1,1,1,2,1] or [1,2,1,2,1] or [1,3,1,2,1] or [1,1,1,1,2] or [1,2,1,1,2] or [1,3,1,1,2] or [1,1,2,2,2] or [1,2,2,2,2] or [1,3,2,2,2] or [1,1,2,1,2] or [1,2,2,1,2] or [1,3,2,1,2] :
            self.show_choose = result_floral.ResultWindow()
            self.show_choose.show()
            self.hide()

        elif self.result5 == [1,1,1,1,1] or [2,1,1,1,1] or [3,1,1,1,1] or [1,1,1,1,2] or [2,1,1,1,2] or [3,1,1,1,2] or [1,1,2,1,2] or [2,1,2,1,2] or [3,1,2,1,2] or [1,1,2,2,2] or [2,1,2,2,2] or [3,1,2,2,2]:
            self.show_choose = result_green.ResultWindow()
            self.show_choose.show()
            self.hide()

        elif self.result5 == [2,1,1,1,1] or [2,2,1,1,1] or [2,3,1,1,1] or [2,1,1,2,1] or [2,2,1,2,1] or [2,3,1,2,1] or [2,1,1,2,2] or [2,2,1,2,2] or [2,3,1,2,2] or [2,1,2,2,1] or [2,2,2,2,1] or [2,3,2,2,1] :
            self.show_choose = result_aqua.ResultWindow()
            self.show_choose.show()
            self.hide()

        elif self.result5 == [2,1,2,1,1] or [2,2,2,1,1] or [2,3,2,1,1] or [2,1,1,1,2] or [2,2,1,1,2] or [2,3,1,1,2] or [2,1,2,1,2] or [2,2,2,1,2] or [2,3,2,1,2] or [2,1,2,2,2] or [2,2,2,2,2] or [2,3,2,2,2] :
            self.show_choose = result_fruity.ResultWindow()
            self.show_choose.show()
            self.hide()

        elif self.result5 == [3,1,1,1,1] or [3,2,1,1,1] or [3,3,1,1,1] or [3,1,1,2,1] or [3,2,1,2,1] or [3,3,1,2,1] or [3,1,2,1,2] or [3,2,2,1,2] or [3,3,2,1,2] or [3,1,2,2,2] or [3,2,2,2,2] or [3,3,2,2,2] :
            self.show_choose = result_woody.ResultWindow()
            self.show_choose.show()
            self.hide()

        elif self.result5 == [3,1,2,1,1] or [3,2,2,1,1] or [3,3,2,1,1] or [3,1,2,2,1] or [3,2,2,2,1] or [3,3,2,2,1] or [3,1,1,1,2] or [3,2,1,1,2] or [3,3,1,1,2] or [3,1,1,2,2] or [3,2,1,2,2] or [3,3,1,2,2] :
            self.show_choose = result_musk.ResultWindow()
            self.show_choose.show()
            self.hide()

        elif self.result5 == [4,1,2,2,1] or [4,2,2,2,1] or [4,3,2,2,1] or [4,1,2,2,2] or [4,2,2,2,2] or [4,3,2,2,2] or [4,1,1,2,2] or [4,2,1,2,2] or [4,3,1,2,2] or [4,1,1,2,1] or [4,2,1,2,1] or [4,3,1,2,1] :
            self.show_choose = result_gourmans.ResultWindow()
            self.show_choose.show()
            self.hide()

        elif self.result5 == [4,1,1,1,1] or [4,2,1,1,1] or [4,3,1,1,1] or [4,1,2,1,1] or [4,2,2,1,1] or [4,3,2,1,1] or [4,1,1,1,2] or [4,2,1,1,2] or [4,3,1,1,2] or [4,1,2,1,2] or [4,2,2,1,2] or [4,3,2,1,2] :
            self.show_choose = result_tobacco_leather.ResultWindow()
            self.show_choose.show()
            self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())