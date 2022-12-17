# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

digit = (input("Введите число "))
result = 0
for element in digit:
    if element.isdigit():
        result += int(element)
print("Сумма цифр числа равна", result)