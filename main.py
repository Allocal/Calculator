import sys


from PySide6.QtWidgets import QApplication, QMainWindow

from ui_design import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def add_digit(self, btn_text: str) -> None:
        if self.ui.le_entery.text() == '0':
            self.ui.le_entery.setText(btn_text)
        else:
            self.ui.le_entery.setText(self.ui.le_entery.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.le_entery.setText('0')
        self.ui.lbl_temp.clear()

    def clear_entry(self) -> None:
        self.ui.le_entery.setText('0')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
