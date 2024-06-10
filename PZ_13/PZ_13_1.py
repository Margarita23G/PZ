# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.

from random import randint

a, b, c, d, e = [int(input(i)) for i in ("Количество строк: ", "Количество столбцов: ",
                                         "От: ", "До: ",
                                         "Строка, значения которой увеличим на 3: ")]
matrix = [[randint(c, d) for _ in range(b)] for j in range(a)]  
print(f"Исходная матрица: ")
for i in matrix:
    print(*i, sep='\t')
s = []
for i in matrix[e - 1]:
    s.append(i + 3)

matrix[e - 1] = s
print(f"Полученная матрица: ")
for i in matrix:
    print(*i, sep='\t')