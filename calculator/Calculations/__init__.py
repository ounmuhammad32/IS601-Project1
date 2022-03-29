"""Calculation """
from calculator.Operations import Addition as Add, Subtraction as Sub, Multiplication as Mult, Division as Div


class Calculation:
    def __init__(self, tuple_list: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        list_values_float = []
        for item in tuple_list:
            list_values_float.append(float(item))
        return tuple(list_values_float)


class Addition(Calculation):
    def get_result(self):
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = Add.add(value, sum_of_values)
        return sum_of_values


class Multiplication(Calculation):
    def get_result(self):
        result = 1.0
        for value in self.values:
            result = Mult.multiply(result, value)
        return result


class Subtraction(Calculation):

    def get_result(self):
        difference_of_values = 2.0
        for value in self.values:
            difference_of_values = Sub.subtract(difference_of_values, value)
        return difference_of_values


class Division(Calculation):

    def get_result(self):
        result = 1.0
        for value in self.values:
            result = Div.divide(result, value)
        return result