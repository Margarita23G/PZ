import re

with open('Dostoevsky.txt', 'r', encoding="UTF-8") as file:
    
    lst = re.findall(r'\d{4}(?:\s*года|\s*год|\s*году|\s*лет|\s*г.)', ''.join([i for i in file.readlines()]))
    lst = [i[0::] for i in lst]

   
    print(f"Список годов: {lst}\n")
    print(f"Количество полученных элементов: {len(lst)}")