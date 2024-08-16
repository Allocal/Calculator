import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_design import Ui_MainWindow

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Digits
        self.ui.Button_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.Button_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.Button_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.Button_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.Button_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.Button_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.Button_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.Button_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.Button_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.Button_9.clicked.connect(lambda: self.add_digit('9'))

        #Actions
        self.ui.Button_C.clicked.connect(self.clear_all)
        self.ui.Button_CE.clicked.connect(self.clear_entry)
        self.ui.Button_Decimal.clicked.connect(self.add_point)

        #Calculation
        self.ui.Button_Result.clicked.connect(self.calculate)
        self.ui.Button_Add.clicked.connect(lambda: self.math_operation('+'))
        self.ui.Button_Substract.clicked.connect(lambda: self.math_operation('-'))
        self.ui.Button_Multiple.clicked.connect(lambda: self.math_operation('*'))
        self.ui.Button_Divide.clicked.connect(lambda: self.math_operation('/'))

    def add_digit(self, btn_text: str) -> None:
        if self.ui.le_entery.text() == '0':
            self.ui.le_entery.setText(btn_text)
        else:
            self.ui.le_entery.setText(self.ui.le_entery.text() + btn_text)

    def add_point(self) -> None:
        if '.' not in self.ui.le_entery.text():
            self.ui.le_entery.setText(self.ui.le_entery.text() + '.')

    def clear_all(self) -> None:
        self.ui.le_entery.setText('0')
        self.ui.lbl_temp.clear()

    def clear_entry(self) -> None:
        self.ui.le_entery.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self, math_sign: str):
        if not self.ui.lbl_temp.text() or self.get_math_sing() == '=':
            self.ui.lbl_temp.setText(self.remove_trailing_zeros(self.ui.le_entery.text()) + f' {math_sign} ')
            self.ui.le_entery.setText('0')

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.le_entery.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sing(self) -> Optional[str]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entery.text()
        temp = self.ui.lbl_temp.text()

        if temp:
            result = self.remove_trailing_zeros(
                str(operations[self.get_math_sing()](self.get_temp_num(), self.get_entry_num()))
            )
            self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
            self.ui.le_entery.setText(result)
            return result

    def math_operation(self, math_sign: str):
        temp = self.ui.lbl_temp.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sing() != math_sign:
                if self.get_math_sing() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{math_sign}')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f'{math_sign}')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
