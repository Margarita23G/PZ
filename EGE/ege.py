#Дана последовательность У целых положительных чисел.  
# Рассматриваются все пары элементов последовательности, разность которых чётна, и в этих парах,  
# по крайней мере, одно из чисел пары делится на 17. Порядок элементов в паре неважен.  
# Среди всех таких пар нужно найти и вывести пару с максимальной суммой элементов.  
# Если одинаковую максимальную сумму имеет несколько пар, можно вывести любую из них.  
# Если подходящих пар в последовательности нет, нужно вывести два нуля. 
#Описание входных и выходных данных 
#В первой строке входных данных задаётся количество чисел N (2 ≤ N ≤ 10 000).  
# В каждой из последующих N строк записано одно натуральное число, не превышающее 10 000 

def find_max_sum_pair(a):
    b = int(a[0])
    max_ch = 0
    max_n = 0
    max_ch17 = 0
    max_n17 = 0
    for i in range(1, b + 1):
        a[i] = int(a[i])
        if a[i] % 2 == 0:
            if a[i] % 17 == 0 and a[i] > max_ch17:
                max_ch17 = a[i]
            elif a[i] % 17 == 0 and a[i] <= max_ch17:
                if a[i] > max_ch:
                    max_ch = a[i]
            elif a[i] > max_ch:
                max_ch = a[i]
        elif a[i] % 2 != 0:
            if a[i] % 17 == 0 and a[i] > max_n17:
                max_n17 = a[i]
            elif a[i] % 17 == 0 and a[i] <= max_n17:
                if a[i] > max_n:
                    max_n = a[i]
            elif a[i] > max_n:
                max_n = a[i]
    if max_n17 + max_n == 0 and max_ch17 + max_ch == 0:
        return 0, 0
    elif max_n17 + max_n > max_ch17 + max_ch:
        return max_n17, max_n
    else:
        return max_ch17, max_ch

if __name__ == '__main__':
    with open("numbers.txt") as f:
        a = f.readlines()
    result = find_max_sum_pair(a)
    print(result)
