# Инкапсуляция - это помещение в "капсулу": логическое объединение данных и функций для работы с ними, а также сокрытие
# внутреннего устройства объекта с предоставлением интерфейса взаимодействия с ним (публичные методы).
# Наследование - это получение нового типа объектов на основе уже существующего с частично или полностью заимствованный
# у родительского типа функциональностью.
# Полиморфизм - это предоставление одинаковых средств взаимодействия с объектами разной природы. Например, операция +
# может работать как с числами, так и со строками, несмотря на разную природу этих объектов.
class ComplexError(BaseException):
    def __init__(self, complex, other):
        self.first = complex
        self.second = other


class Complex:
    def __init__(self, re=0, im=0):  # конструктор класса
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + ' + ' + str(self.im) + 'i'

    def __add__(self, other):
        result = Complex(self.re + other.re, self.im + other.im)
        return result

    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re*other.re - self.im*other.im
            im = self.re*other.im + self.im*other.re
        elif isinstance(other, int) or isinstance(other, float):
            re = self.re * other
            im = self.im * other
        else:
            error = ComplexError(self, other)
            raise error
        return Complex(re, im)

    __rmul__ = __mul__


class Point(Complex):
    def length(self):
        return (self.re**2 + self.im**2)**0.5

    def __str__(self):
        return str((self.re, self.im))


p1 = Point(1, 1)
print(p1)



# a = Complex()
# b = Complex(1, 1)
# c = Complex(2, 3)
# print(str(c), str(b))
# print(b + c)
# print(b * c)
# print(b * 2)
# print(2 * b)
# try:
#     print(3 * b)
# except ComplexError as ce:
#     print('Multiplaction error,first param:', ce.first,
#           'second param', ce.second)

