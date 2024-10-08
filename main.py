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

error_zero_div = 'Division by zero'
error_undefined = 'Undefined Error'

default_font_size = 16
default_entry_font_size = 40


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max_len = self.ui.le_entery.maxLength()

        # Digits
        self.ui.Button_0.clicked.connect(self.add_digit)
        self.ui.Button_1.clicked.connect(self.add_digit)
        self.ui.Button_2.clicked.connect(self.add_digit)
        self.ui.Button_3.clicked.connect(self.add_digit)
        self.ui.Button_4.clicked.connect(self.add_digit)
        self.ui.Button_5.clicked.connect(self.add_digit)
        self.ui.Button_6.clicked.connect(self.add_digit)
        self.ui.Button_7.clicked.connect(self.add_digit)
        self.ui.Button_8.clicked.connect(self.add_digit)
        self.ui.Button_9.clicked.connect(self.add_digit)

        # Actions
        self.ui.Button_C.clicked.connect(self.clear_all)
        self.ui.Button_CE.clicked.connect(self.clear_entry)
        self.ui.Button_Decimal.clicked.connect(self.add_point)
        self.ui.Button_ChangeSine.clicked.connect(self.negate)
        self.ui.Button_Backspace.clicked.connect(self.backspace)

        # Calculation
        self.ui.Button_Result.clicked.connect(self.calculate)
        self.ui.Button_Add.clicked.connect(self.math_operation)
        self.ui.Button_Substract.clicked.connect(self.math_operation)
        self.ui.Button_Multiple.clicked.connect(self.math_operation)
        self.ui.Button_Divide.clicked.connect(self.math_operation)

    def add_digit(self):
        self.remove_error()
        self.clear_temp_if_equality()
        btn = self.sender()

        digit_buttons = ('Button_0', 'Button_1', 'Button_2', 'Button_3', 'Button_4',
                         'Button_5', 'Button_6', 'Button_7', 'Button_8', 'Button_9')

        if btn.objectName() in digit_buttons:
            if self.ui.le_entery.text() == '0':
                self.ui.le_entery.setText(btn.text())
            else:
                self.ui.le_entery.setText(self.ui.le_entery.text() + btn.text())

        self.adjust_entry_font_size()

    def add_point(self) -> None:
        self.clear_temp_if_equality()
        if '.' not in self.ui.le_entery.text():
            self.ui.le_entery.setText(self.ui.le_entery.text() + '.')

        self.adjust_entry_font_size()

    def negate(self):
        self.clear_temp_if_equality()
        entry = self.ui.le_entery.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.ui.le_entery.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.le_entery.setMaxLength(self.entry_max_len)

        self.ui.le_entery.setText(entry)
        self.adjust_entry_font_size()

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.ui.le_entery.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.le_entery.setText('0')
            else:
                self.ui.le_entery.setText(entry[:-1])
        else:
            self.ui.le_entery.setText('0')

        self.adjust_entry_font_size()

    def clear_all(self) -> None:
        self.remove_error()
        self.ui.le_entery.setText('0')
        self.ui.lbl_temp.clear()
        self.adjust_entry_font_size()

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        self.ui.le_entery.setText('0')
        self.adjust_entry_font_size()

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sing() == '=':
            self.ui.lbl_temp.clear()
            self.adjust_temp_font_size()

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.ui.le_entery.text())

        if not self.ui.lbl_temp.text() or self.get_math_sing() == '=':
            self.ui.lbl_temp.setText(entry + f' {btn.text()} ')
            self.adjust_temp_font_size()
            self.ui.le_entery.setText('0')
            self.adjust_entry_font_size()

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

    def get_entry_text_width(self) -> int:
        return self.ui.le_entery.fontMetrics().boundingRect(self.ui.le_entery.text()).width()

    def get_temp_text_width(self) -> int:
        return self.ui.lbl_temp.fontMetrics().boundingRect(self.ui.lbl_temp.text()).width()

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entery.text()
        temp = self.ui.lbl_temp.text()

        if temp:
            try:
                result = self.remove_trailing_zeros(
                    str(operations[self.get_math_sing()](self.get_temp_num(), self.get_entry_num()))
                )
                self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
                self.adjust_temp_font_size()
                self.ui.le_entery.setText(result)
                self.adjust_entry_font_size()
                return result
            except KeyError:
                pass

            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_div)

    def math_operation(self) -> None:
        temp = self.ui.lbl_temp.text()
        btn = self.sender()

        try:
            if not temp:
                self.add_temp()
            else:
                if self.get_math_sing() != btn.text():
                    if self.get_math_sing() == '=':
                        self.add_temp()
                    else:
                        self.ui.lbl_temp.setText(temp[:-2] + f'{btn.text()}')
                else:
                    self.ui.lbl_temp.setText(self.calculate() + f'{btn.text()}')
        except TypeError:
            pass

        self.adjust_temp_font_size()

    def show_error(self, text: str) -> None:
        self.ui.le_entery.setMaxLength(len(text))
        self.ui.le_entery.setText(text)
        self.adjust_entry_font_size()
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.ui.le_entery.text() in (error_undefined, error_zero_div):
            self.ui.le_entery.setMaxLength(self.entry_max_len)
            self.ui.le_entery.setText('0')
            self.adjust_entry_font_size()
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:
        self.ui.Button_Result.setDisabled(disable)
        self.ui.Button_Add.setDisabled(disable)
        self.ui.Button_Substract.setDisabled(disable)
        self.ui.Button_Multiple.setDisabled(disable)
        self.ui.Button_Divide.setDisabled(disable)
        self.ui.Button_Decimal.setDisabled(disable)
        self.ui.Button_ChangeSine.setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str) -> None:
        self.ui.Button_Result.setStyleSheet(css_color)
        self.ui.Button_Add.setStyleSheet(css_color)
        self.ui.Button_Substract.setStyleSheet(css_color)
        self.ui.Button_Multiple.setStyleSheet(css_color)
        self.ui.Button_Divide.setStyleSheet(css_color)
        self.ui.Button_Decimal.setStyleSheet(css_color)
        self.ui.Button_ChangeSine.setStyleSheet(css_color)

    def adjust_entry_font_size(self) -> None:
        font_size = default_font_size
        while self.get_entry_text_width() > self.ui.le_entery.width() - 15:
            font_size -= 1
            self.ui.le_entery.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

        font_size = 1
        while self.get_entry_text_width() < self.ui.le_entery.width() - 60:
            font_size += 1

            if font_size > default_font_size:
                break

            self.ui.le_entery.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size
        while self.get_temp_text_width() > self.ui.lbl_temp.width() - 10:
            font_size -= 1
            self.ui.lbl_temp.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.ui.lbl_temp.width() - 60:
            font_size += 1

            if font_size > default_font_size:
                break

            self.ui.le_entery.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;')

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
