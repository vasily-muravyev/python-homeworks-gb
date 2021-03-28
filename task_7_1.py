# Задание 1.

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.

# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно
# — первый элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.

class InvalidDimension(BaseException):
    pass


class UnequalDimensions(BaseException):
    pass


class Matrix:

    def __init__(self, matrix):
        """
        :param matrix: list of lists
        """
        self._matrix = matrix
        self._n_rows = len(matrix)
        self._n_columns = len(matrix[0])

        self.__check_dimensions()

    def __str__(self):
        string_repr = ""
        for row in self._matrix:
            for column in row:
                string_repr += str(column) + " "
            string_repr += "\n"
        return string_repr

    def __add__(self, other):
        if self._n_rows != other._n_rows or self._n_columns != other._n_columns:
            raise UnequalDimensions()

        # it would be better to just use numpy here, but task is task
        sum_of_matrixes = []
        for row1, row2 in zip(self._matrix, other._matrix):
            row_of_sum = []
            for column1, column2 in zip(row1, row2):
                row_of_sum.append(column1 + column2)
            sum_of_matrixes.append(row_of_sum)
        return Matrix(sum_of_matrixes)

    def __check_dimensions(self):
        column_dimensions = []
        for row in self._matrix:
            column_dimensions.append(len(row))

        # check that all rows have same number of elements
        if len(list(set(column_dimensions))) != 1:
            raise InvalidDimension(str(self._matrix))


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])

print(matrix1)
print(matrix2)

try:
    invalid_matrix = Matrix([[1, 2], [4, 5, 6]])
    print(invalid_matrix)
except InvalidDimension:
    print("Invalid dimensions of matrix")

try:
    invalid_sum = matrix1 + matrix2
except UnequalDimensions:
    print("Unequal dimensions for sum of matrix")

print("Sum of two matrix")
print(matrix2 + matrix2)