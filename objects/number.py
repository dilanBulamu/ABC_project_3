import typing
from enum import Enum
from abc import abstractmethod
import random
import math


class NumberType(Enum):
    COMPLEX = 0
    FRACTION = 1
    POLAR = 2

class Number:
    @staticmethod
    def static_input(input_file) -> typing.Optional['Number']:
        """
        Getting number from input file.
        :param input_file:
        :return: complex, polar or fraction number type.
        """
        try:
            data = input_file.readline()
            number_type = NumberType(int(data))
            if number_type == NumberType.COMPLEX:
                return Complex.input(input_file)
            elif number_type == NumberType.FRACTION:
                return Fraction.input(input_file)
            elif number_type == NumberType.POLAR:
                return Polar.input(input_file)
            else:
                print("Error: incorrect number type = {}.".format(data))
                return None
        except Exception as ex:
            print("Error: incorrect input.")
            return None

    @staticmethod
    def static_generate() -> 'Number':
        """
        Generate random number.
        :return: complex, polar or fraction number type.
        """
        number_type = NumberType(random.randint(0, 2))
        if number_type == NumberType.COMPLEX:
            return Complex.generate()
        elif number_type == NumberType.FRACTION:
            return Fraction.generate()
        elif number_type == NumberType.POLAR:
            return Polar.generate()

    @abstractmethod
    def output(self, output_file):
        """
        Output number info to output file.
        :param output_file:
        :return:
        """
        pass

    @staticmethod
    def generate():
        """
        Generate random number params.
        :return:
        """
        pass

    @staticmethod
    def input(input_file):
        """
         Getting number params from input file.
        :param input_file:
        :return:
        """
        pass

    @abstractmethod
    def cast_to_double(self):
        """
        Cast number to float.
        :return: float.
        """
        pass



class Complex(Number):
    def __init__(self, type: NumberType, real: float, imaginary: float):
        """
        Constructor.
        :param type: number type.
        :param real: real part of the complex number.
        :param imaginary: imaginary part of the complex number.
        """
        self.__type = type
        self.__real = real
        self.__imaginary = imaginary

    def __str__(self):
        """
        Cast complex number to string.
        :return: params as string.
        """
        return "0\n{} {}\n".format(self.__real, self.__imaginary)

    @staticmethod
    def input(input_file) -> 'Complex':
        try:
            data = input_file.readline().split(" ")
            return Complex(NumberType.COMPLEX, float(data[0]), float(data[1]))
        except Exception as ex:
            print("Error: incorrect input.")
            return None

    @staticmethod
    def generate() -> 'Complex':
        return Complex(NumberType.COMPLEX, random.uniform(-100, 100), random.uniform(-100, 100))

    def output(self, output_file):
        output_file.write("Number type: {}; real = {}; imaginary = {}; double cast = {}.\n".format \
                              (str(Complex.__name__), self.__real, self.__imaginary, str(self.cast_to_double())))
        pass

    def cast_to_double(self):
        return math.sqrt(self.__real ** 2 + self.__imaginary ** 2)

class Fraction(Number):
    def __init__(self, type: NumberType, numerator: int, denomirator: int):
        """
        Constructor.
        :param type: number type.
        :param numerator: fractional numerator.
        :param denomirator: fractional denominator.
        """
        self.__type = type
        self.__numerator = numerator
        self.__denomirator = denomirator

    def __str__(self):
        """
        Cast fraction number to string.
        :return: params as string.
        """
        return "1\n{} {}\n".format(self.__numerator, self.__denomirator)

    @staticmethod
    def input(input_file) -> 'Fraction':
        try:
            data = input_file.readline().split(" ")
            if int(data[1]) == 0:
                print("Error: denominator = 0.")
                return None
            return Fraction(NumberType.FRACTION, int(data[0]), int(data[1]))
        except Exception as ex:
            print("Error: incorrect input.")
            return None

    @staticmethod
    def generate() -> 'Fraction':
        return Fraction(NumberType.FRACTION, random.randint(-100, 100), random.randint(1, 100))

    def output(self, output_file):
        output_file.write("Number type: {}; fraction = {}/{}; double cast = {}.\n".format \
                              (str(Fraction.__name__), self.__numerator, self.__denomirator, str(self.cast_to_double())))
        pass

    def cast_to_double(self):
        return self.__numerator / self.__denomirator

class Polar(Number):
    def __init__(self, type: NumberType, point_x: int, point_y: int, angle: float):
        """
        Constructor.
        :param type: number type
        :param point_x: x coordinate
        :param point_y: y coordinate
        :param angle: tilt angle
        """
        self.__type = type
        self.__point_x = point_x
        self.__point_y = point_y
        self.__angle = angle

    def __str__(self):
        """
        Cast polar number to string.
        :return: params as string.
        """
        return "2\n{} {} {}\n".format(self.__point_x, self.__point_y, self.__angle)

    @staticmethod
    def input(input_file) -> 'Polar':
        try:
            data = input_file.readline().split(" ")
            return Polar(NumberType.POLAR, int(data[0]), int(data[1]), float(data[2]))
        except Exception as ex:
            print("Error: incorrect input.")
            return None

    @staticmethod
    def generate() -> 'Polar':
        return Polar(NumberType.POLAR, random.randint(-100, 100), random.randint(-100, 100), random.uniform(-100, 100))

    def output(self, output_file):
        output_file.write("Number type: {}; point = ({}, {}); angle = {}; double cast = {}.\n".format \
                              (str(Polar.__name__), self.__point_x, self.__point_y, self.__angle, str(self.cast_to_double())))
        pass

    def cast_to_double(self):
        return math.sqrt(self.__point_x ** 2 + self.__point_y ** 2)
