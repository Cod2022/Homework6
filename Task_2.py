# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

with open('file.txt', 'r') as text:
    text = text.read()

count = len(max(text.split('O')))

print(f'Наибольшее количество выпавших Решек: {count}')
