# Приложение АПТЕКА для автоматизации работы аптечных пунктов. 
# Таблица Лекарственные Средства должна содержать следующую информацию: 
# Код, Название препарата, Применение, Количество, Цена, Страна-производитель

import sqlite3

conn = sqlite3.connect('aptechka.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ЛекарственныеСредства (
        Код INTEGER PRIMARY KEY AUTOINCREMENT,
        НазваниеПрепарата TEXT,
        Применение TEXT,
        Количество INTEGER,
        Цена REAL,
        СтранаПроизводитель TEXT
    )
''')

def add_medicine():
    name = input("Введите название препарата: ")
    usage = input("Введите применение: ")
    quantity = int(input("Введите количество: "))
    price = float(input("Введите цену: "))
    country = input("Введите страну-производителя: ")

    cursor.execute('''
        INSERT INTO ЛекарственныеСредства (НазваниеПрепарата, Применение, Количество, Цена, СтранаПроизводитель)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, usage, quantity, price, country))
    conn.commit()
    print("Лекарство добавлено в базу данных.")


def view_medicines():
    cursor.execute("SELECT * FROM ЛекарственныеСредства")
    medicines = cursor.fetchall()
    if medicines:
        print("Список лекарственных средств:")
        for medicine in medicines:
            print(f"Код: {medicine[0]}, Название: {medicine[1]}, Применение: {medicine[2]}, Количество: {medicine[3]}, Цена: {medicine[4]}, Страна-производитель: {medicine[5]}")
    else:
        print("В базе данных нет лекарственных средств.")


def search_medicine():
    name = input("Введите название препарата: ")
    cursor.execute('''
        SELECT * FROM ЛекарственныеСредства WHERE НазваниеПрепарата LIKE ?
    ''', ('%' + name + '%',))
    medicines = cursor.fetchall()
    if medicines:
        print("Найденные лекарственные средства:")
        for medicine in medicines:
            print(f"Код: {medicine[0]}, Название: {medicine[1]}, Применение: {medicine[2]}, Количество: {medicine[3]}, Цена: {medicine[4]}, Страна-производитель: {medicine[5]}")
    else:
        print("Лекарственное средство не найдено.")


def update_medicine():
    code = int(input("Введите код лекарственного средства: "))
    cursor.execute('''
        SELECT * FROM ЛекарственныеСредства WHERE Код = ?
    ''', (code,))
    medicine = cursor.fetchone()
    if medicine:
        print("Текущая информация о лекарственном средстве:")
        print(f"Код: {medicine[0]}, Название: {medicine[1]}, Применение: {medicine[2]}, Количество: {medicine[3]}, Цена: {medicine[4]}, Страна-производитель: {medicine[5]}")

        name = input("Введите новое название (оставьте пустым, чтобы не изменять): ")
        usage = input("Введите новое применение (оставьте пустым, чтобы не изменять): ")
        quantity = input("Введите новое количество (оставьте пустым, чтобы не изменять): ")
        price = input("Введите новую цену (оставьте пустым, чтобы не изменять): ")
        country = input("Введите новую страну-производителя (оставьте пустым, чтобы не изменять): ")

        if name:
            cursor.execute('''
                UPDATE ЛекарственныеСредства SET НазваниеПрепарата = ? WHERE Код = ?
            ''', (name, code))
        if usage:
            cursor.execute('''
                UPDATE ЛекарственныеСредства SET Применение = ? WHERE Код = ?
            ''', (usage, code))
        if quantity:
            cursor.execute('''
                UPDATE ЛекарственныеСредства SET Количество = ? WHERE Код = ?
            ''', (quantity, code))
        if price:
            cursor.execute('''
                UPDATE ЛекарственныеСредства SET Цена = ? WHERE Код = ?
            ''', (price, code))
        if country:
            cursor.execute('''
UPDATE ЛекарственныеСредства SET СтранаПроизводитель = ? WHERE Код = ?
            ''', (country, code))
        conn.commit()
        print("Информация о лекарственном средстве обновлена.")
    else:
        print("Лекарственное средство с данным кодом не найдено.")


def delete_medicine():
    code = int(input("Введите код лекарственного средства: "))
    cursor.execute('''
        SELECT * FROM ЛекарственныеСредства WHERE Код = ?
    ''', (code,))
    medicine = cursor.fetchone()
    if medicine:
        print("Информация о лекарственном средстве:")
        print(f"Код: {medicine[0]}, Название: {medicine[1]}, Применение: {medicine[2]}, Количество: {medicine[3]}, Цена: {medicine[4]}, Страна-производитель: {medicine[5]}")
        confirm = input("Вы уверены, что хотите удалить это лекарственное средство? (Да/Нет): ")
        if confirm.lower() == 'да':
            cursor.execute('''
                DELETE FROM ЛекарственныеСредства WHERE Код = ?
            ''', (code,))
            conn.commit()
            print("Лекарственное средство удалено.")
        else:
            print("Удаление отменено.")
    else:
        print("Лекарственное средство с данным кодом не найдено.")


while True:
    print("\nАптека - главное меню:")
    print("1. Добавить лекарственное средство")
    print("2. Просмотреть все лекарственные средства")
    print("3. Поиск лекарственных средств")
    print("4. Обновить информацию о лекарственном средстве")
    print("5. Удалить лекарственное средство")
    print("6. Выход")

    choice = input("Введите номер действия: ")

    if choice == '1':
        add_medicine()
    elif choice == '2':
        view_medicines()
    elif choice == '3':
        search_medicine()
    elif choice == '4':
        update_medicine()
    elif choice == '5':
        delete_medicine()
    elif choice == '6':
        break
    else:
        print("Неверный выбор.")
        
conn.close()