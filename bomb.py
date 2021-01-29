# !/usr/bin/env python
# _*_ coding: utf-8 _*_
#time: 2021/1/22 15:31

import  sys, time, pyautogui, pyperclip
from PyQt5.QtWidgets import QMainWindow, QApplication,  QMessageBox
from Home import Ui_MainWindow

class bombTool (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.send_type = self.buttonGroup.checkedButton().property('dataValue')  # 选择的 炸弹、烟花、庆祝

    def radioClicked(self):
        self.send_type = self.buttonGroup.checkedButton().property('dataValue')  # 选择的 炸弹、烟花、庆祝

    def sendSms(self):
        if self.lineEdit.text() != '':
            send_num = self.lineEdit.text()
        else:
            send_num = 5
        if self.lineEdit_2.text() != '':
            send_time = self.lineEdit_2.text()
        else:
            send_time = 3
        time.sleep(5)
        for _ in range(int(send_num)):
            pyperclip.copy(self.send_type)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")
            time.sleep(int(send_time))
        QMessageBox.information(self, '信息框', '执行完成')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bombToolMain = bombTool()
    bombToolMain.show()
    sys.exit(app.exec_())