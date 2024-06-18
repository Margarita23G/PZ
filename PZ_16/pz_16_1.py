# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.

class Matrix:
    def __init__(self, data=None, rows=3, cols=3):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)] if not data else data
        self.rows = len(self.data)
        self.cols = len(max(self.data))

        if len(max(self.data)) != len(min(self.data)):
            raise ValueError("Matrix must have same count of columns and rows")

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = Matrix(rows=self.rows, cols=other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


if __name__ == '__main__':
    matrix1 = Matrix(
        [[1, 2], [3, 4]],
    )

    matrix2 = Matrix(
        [[5, 6], [7, 8]],
    )

    sum_matrix = matrix1 + matrix2
    print("Сумма матриц:")
    print(sum_matrix)

    diff_matrix = matrix1 - matrix2
    print("Разность матриц:")
    print(diff_matrix)

    product_matrix = matrix1 * matrix2
    print("Произведение матриц:")
    print(product_matrix)
