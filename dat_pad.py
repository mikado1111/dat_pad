from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
import sys
import pymorphy2


class Main_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.push)

    def push(self):
        self.ui.plainTextEdit_2.clear()
        if len(self.ui.plainTextEdit.toPlainText()) == 0:
            return
        list_of_names = self.ui.plainTextEdit.toPlainText().split("\n")
        morph = pymorphy2.MorphAnalyzer()
        all_names = ""
        for names in list_of_names:
            if names == "":
                break
            name_in_dat_padezh = ""
            name = names.split()[1]
            if morph.parse(name)[0].tag.gender == "masc":
                case = "masc"
            else:
                case = "femn"
            # print(name, case)
            for word in names.split():
                name = morph.parse(word)[0]
                # print(name)
                if "ms-f" in name.tag:
                    name_in_dat_padezh += name.word.capitalize() + " "
                else:
                    name_in_dat_padezh += name.inflect({"datv", case}).word.capitalize() + " "
            all_names += name_in_dat_padezh + "\n"
        self.ui.plainTextEdit_2.setPlainText(all_names)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pr = Main_window()
    pr.show()
    sys.exit(app.exec_())