# Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
# Дан номер единицы массы (целое число в диапазоне 1-5) и масса тела в этих единицах (вещественное число).
# Найти массу тела в килограммах.
while True:  # программа постоянно работает даже при ошибке
    try:  # пользователь ввёл числа
        print("Введите число от 1 до 5:")
        print("1 - килограмм", "2 - миллиграмм", "3 - грамм", "4 - тонна", "5 - центнер", sep='\n')
        S = int(input())  # для целочисленных значений
        G = float(input("Введите массу тела в этих единицах:"))  # для дробных значений
        if S == 1:  # выводим килограммы
            print("Масса тела в килограммах = ", G)
        elif S == 2:  # переводим миллиграммы в килограммы
            print("Масса тела в килограммах = ", G / 1000000)
        elif S == 3:  # переводим граммы в килограммы
            print("Масса тела в килограммах = ", G / 1000)
        elif S == 4:  # переводим тонны в килограммы
            print("Масса тела в килограммах = ", G * 1000)
        else:  # переводим центнеры в килограммы
            print("Масса тела в килограммах = ", G * 100)
        print("Спасибо, программа успешно завершена!)")
        break  # досрочно прерывает цикл
    except ValueError:  # проверка исключений(пользователь ввел не число, на экран выводится текст, а не ошибка)
        print("Введите числo, пожалуйста!")