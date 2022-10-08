# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

 # Пример:

# 6 -> да
# 7 -> да
# 1 -> нет

d = int(input('Введите число дня недели от 1 до 7: '))
if d > 7:
    print('такого дня недели нет')
elif d < 6:
    print('нет')
else:
    print('да')


# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            print(bool(not(X or Y or Z) == (not(X) and not(Y) and not(Z))))


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причем X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

 # Пример:

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Введите х: '))
y = int(input('Введите у: '))
if y > 0:
    if x > 0:
        print(1)
    else:
        print(2)
elif x < 0:
        print(3)
else:
    print(4)
    

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти: '))
if a == 1:
    print('X > 0, Y > 0')
elif a == 2:
    print('X < 0, Y > 0')
elif a == 3:
    print('X < 0, Y < 0')
elif a == 4:
    print('X > 0, Y < 0')
else:
    print('такого дня нет')


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

 # Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

a_x = int(input('Введите Ах: '))
a_y = int(input('Введите Ау: '))
b_x = int(input('Введите Bх: '))
b_y = int(input('Введите Bу: '))
ab = round(((b_x - a_x)**2 + (b_y - a_y)**2)**0.5, 2)
print(ab)

