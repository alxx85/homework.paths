
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path

migrations = 'Advanced Migrations'
abs_path = os.path.dirname(__file__)

print(abs_path)

def search_file(files_list, search_string, paths):
	quantity = 0
	file_list_new = list()
	for file in files_list:
		with open(file, encoding='cp1251') as f:
			if search_string in f.read():
				file_list_new.append(str(file))
				quantity += 1
	if len(file_list_new) > 10:
		print('...Большой список файлов...')
	else:
		for file_in_list in file_list_new:
			print(os.path.join(paths, file_in_list))
	print(quantity)
	return file_list_new


files = glob.glob(os.path.join(migrations, "*.sql"))
while True:
	input_string = input('Введите строку: ')
	files = search_file(files, input_string, abs_path)
