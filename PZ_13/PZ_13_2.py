#  В матрице элементы последнего столбца заменить на -1

from random import randint

a, b, c, d = [int(input(i)) for i in ("Количество строк: ", "Количество столбцов: ", "От: ", "До: ")]

matrix = [[randint(c, d) for _ in range(b)] for j in range(a)]
print(f"Исходная матрица: ")
for i in matrix:
    print(*i, sep='\t')

for i in range(a):
    matrix[i][b - 1] = -1
print(f"Полученная матрица: ")
for i in matrix:
    print(*i, sep='\t')