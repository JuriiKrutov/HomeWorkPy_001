'''Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).'''

num = int(input("Введите номер четверти: "))
if num == 1:
    print("x = 0 -> +infinity, y = 0 -> +infinity ")
elif num == 2:
    print("x = 0 -> -infinity, y = 0 -> +infinity ")
elif num == 3:
    print("x = 0 -> -infinity, y = 0 -> -infinity ")
elif num == 4:
    print("x = 0 -> +infinity, y = 0 -> +infinity ")
else:
    print("Не верный ввод")