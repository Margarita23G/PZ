# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработкуэлементов:
#
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов: Положительные четные элементы:
# Сумма положительных четных элементов:
# Среднее арифметическое положительных четных элементов:

print('5, 4, 3, 2, 1, -1, -2, -3, -4, -5', file=open('file58_1.txt', 'w'))

s, g = [int(i) for i in open('file58_1.txt').read().split(', ')], open('file58_2.txt', 'w', encoding="utf-16")

a = [i for i in s if i > 0 if i % 2 == 0]

print("Исходные данные: ", open('file58_1.txt').read(), file=g)
print("Количество элементов: ", len(open('file58_1.txt').read().split(', ')), file=g)
print("Среднее арифметическое элементов: ", sum(s) / len(s), file=g)
print("Положительные чётные элементы: ", a, file=g)
print("Сумма положительных чётных элементов: ", sum(a), file=g)
print("Среднее арифметическое положительных чётных элементов: ", sum(a) / len(a), file=g)