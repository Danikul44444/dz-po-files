import os
import re

folder_path = os.getcwd() + '\data\\'

files = os.listdir(folder_path)

file_count = len(files)
print(f"Количество файлов в папке: {file_count}")

digit_count = 0
for file in files:
    if re.search(r'\d', file):
        digit_count += 1
print(f"Количество файлов с цифрой в имени: {digit_count}")

letter_count = 0
for file in files:
    if re.search(r'g', file):
        letter_count += 1
print(f"Количество файлов с буквой 'g' в имени: {letter_count}")

double_letter_count = 0
for file in files:
    if re.search(r'gg', file):
        double_letter_count += 1
print(f"Количество файлов с двумя буквами 'g' подряд в имени: {double_letter_count}")

sum_greater_than_10_count = 0
for file in files:
    numbers = re.findall(r'\d+', file)
    if sum(map(int, numbers)) > 10:
        sum_greater_than_10_count += 1
print(f"Количество файлов, в имени которых сумма чисел больше 10: {sum_greater_than_10_count}")

