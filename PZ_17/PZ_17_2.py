# Задание 1
import os
import subprocess
import sys

os.chdir('./PZ_11')
files = os.listdir()
for file in files:
    if os.path.isfile(file):
        print(file)

# Задание 2
os.chdir('../')  # переходим в корень проекта
os.makedirs('test/test1', exist_ok=True)  # создаем папки test и test1

with open("./PZ_6/PZ_6_1.py", "r", encoding="utf-8") as pz6_1, open("./PZ_6/PZ_6_2.py", "r", encoding="utf-8") as pz6_2, open("./PZ_7/PZ_7_1.py", "r", encoding="utf-8") as pz7_1, \
     open("./test/file1.txt", "w+", encoding="utf-8") as txt1, open("./test/file2.txt", "w+", encoding="utf-8") as txt2, open("./test/test1/test.txt", "w+", encoding="utf-8") as txt3:
    content_pz6_1 = pz6_1.read()
    content_pz6_2 = pz6_2.read()
    content_pz7_1 = pz7_1.read()

    txt1.write(content_pz6_1)
    txt2.write(content_pz6_2)
    txt3.write(content_pz7_1)

total_size = 0
for dirpath, dirnames, filenames in os.walk('test'):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        file_size = os.path.getsize(filepath)
        total_size += file_size
        print(f"Размер файла {filename}: {file_size} байт")
print(f"Общий размер файлов {total_size} байт")

# Задание 3
os.chdir('PZ_11')
short_file = min(os.listdir(), key=len)
print("Файл с самым коротким именем: ", os.path.basename(short_file))

# Задание 4
os.chdir("../reports")
if sys.platform == "win32":
    os.startfile("Отчет PZ_2.pdf")
else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, "Отчет PZ_2.pdf"])

# Задание 5
os.chdir('../test/test1')  # переходим в папку test1
print(*os.listdir())
os.remove('test.txt')  # удаляем файл test.txt
