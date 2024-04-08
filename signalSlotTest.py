import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SignalThread(QThread):    # signal 부분
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()
        self.signal2.emit(1000, 2000)

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        signalClass = SignalThread()

        # signal
        signalClass.signal1.connect(self.signal1_print)
        signalClass.signal2.connect(self.signal2_print)
        signalClass.run()
    @pyqtSlot()
    def signal1_print(self):        # slot 함수
        print("signal1 제출됨(emit)~~")
    @pyqtSlot(int, int)
    def signal2_print(self, int1, int2):
        print(f"signal2 제출됨(emit)~~>> {int1}, {int2}")
        # 실제 프로그램에서는 윈도우에 출력하는 함수

app = QApplication(sys.argv)
win = MainWin()
win.show()
sys.exit(app.exec_())

