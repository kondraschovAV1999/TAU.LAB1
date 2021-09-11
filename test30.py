from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        string = ''
        for line in self.matrix:
            string += '\t'.join(list(map(str, line)))
            string += '\n'
        return string.strip()

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        newMatrix = list()
        line = list()
        if len(self.matrix[0]) == len(other[0]) and \
                len(list(self.matrix)) == len(list(other)):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    line.append(int(self.matrix[i][j]) + int(other[i][j]))
                newMatrix.append(line)
                line = list()
        else:
            error = MatrixError(self, other)
            raise error
        return Matrix(newMatrix)

    def __getitem__(self, index):
        return self.matrix[index]

    def __mul__(self, other):
        newMatrix = list()
        line = list()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                line.append(int(self.matrix[i][j]) * other)
            newMatrix.append(line)
            line = list()
        return Matrix(newMatrix)

    def transpose(self):
        self.matrix = list(zip(*self.matrix))
        return Matrix(self.matrix)
    __rmul__ = __mul__

    @staticmethod
    def transposed(other):
        return Matrix(list(zip(*other)))


exec(stdin.read())
