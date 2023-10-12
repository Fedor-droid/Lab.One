import math
a = float(input('Введите первое число '))
b = float(input('Введите второе число '))

max_abs = max(a,b , key=abs)
min_abs = min(a,b , key=abs)

print("Сумма чисел", round(a+b,2))
print("Разность чисел", round(a-b,2))
print("Произведение чисел", round(a*b,2))
print("Частное чисел",round((a/b),2))
print("Среднее арифметическое чисел", round((a+b)/2 ,2))
print("Разность максимального и минимального числа по модулю", round(abs(max_abs) - abs(min_abs),2))
