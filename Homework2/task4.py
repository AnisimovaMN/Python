# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


n = int(input('Введите число: '))
a = []
p = 1
for i in range(-n, n+1):
    a.append(i)
print(a)
f = open('file.txt')
for i in f:
    p *= a[int(i)]
print(p)
f.close()
