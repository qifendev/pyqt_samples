# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys


from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PyQt5.QtCore import QObject, pyqtSignal


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()




    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        root = loader.load(ui_file, self)
        ui_file.close()
#发送消息
class Qbj1(QObject):
    sign1 = pyqtSignal(float);
    def __init__(self):
        super(Qbj1,self).__init__()
    def sendSign(self):
        print("send message====")
        self.sign1.emit(999)
#接受消息
class Qbj2(QObject):
    def __init__(self):
        super(Qbj2,self).__init__()
    def receiverSign(self,value):
        print("receiver signal=======")
        print(value)


if __name__ == "__main__":
    app = QApplication([])

    obj1 = Qbj1()
    obj2 = Qbj2()
    obj1.sign1.connect(obj2.receiverSign)
    obj1.sendSign()
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
