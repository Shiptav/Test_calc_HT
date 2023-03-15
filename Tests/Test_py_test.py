import pytest

from app.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator
    
    def test_adding_success(self):
        # проверяем сложение
        assert self.calc.adding(self,1, 1) == 2
        
    def test_multiply_success(self):
        # проверяем умножение
        assert self.calc.multiply(self,5, 5) == 25
        
    def test_division_success(self):
        # проверяем деление
        assert self.calc.division(self,9, 3) == 3
    
    def test_subtraction_success(self):
        # проверяем вычитание
        assert self.calc.substraction(self,10, 5) == 5
        
    def test_zero_division(self):
        # проверяем деление на ноль
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown_method(self):
        print('Выполнение метода Teardown')
