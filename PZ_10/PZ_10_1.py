#Туристические агенства предлагают следующие туры.
#  Вояж - Мексика, Канада, Израиль, Италия, США.
#  РейнаТур - Англия, Япония, Канада, ЮАР.
#  Радуга - США, Испания, Швеция, Австралия.
#  Определить, в каких турагенствах можно приобрести туры в Канаду, а в каких в США.

s = {'Вояж': ["Мексика", "Канада", "Израиль", "Италия", "США"],  # Создаём словарь с Агенствами (ключи),
     'РейнаТур': ["Англия", "Япония", "Канада", "ЮАР"],  # Которые предлагают туры в Страны (значения)
     'Радуга': ["США", "Испания", "Швеция", "Австралия"]}

for key, value in s.items():  # Делаем функцию перебора ключей и значений
    if "Канада" in value:  # Если Канада есть в значениях
        print("Турагенство в котором можно приобрести тур в Канаду: ", key)  # Выводим Турагенство (ключ)
for key, value in s.items():  # Делаем функцию перебора ключей и значений
    if "США" in value:  # Если США есть в значениях
        print("Турагенство в котором можно приобрести тур в США: ", key)  # Выводим Турагенство (ключ)