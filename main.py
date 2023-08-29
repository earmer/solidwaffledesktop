# Copyright (c) 2023 LTL Team. All rights reserved.
# Author: Earmer Carey

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from Wafflefront import Ui_Solidwaffle
class MyWindow(QMainWindow, Ui_Solidwaffle):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())