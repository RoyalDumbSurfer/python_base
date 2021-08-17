num1 = int(input('введите первое число '))
num2 = int(input('введите второе число '))
action = str(input('Выберите действие: Умножение - (M), Деление - (D), Сложение - (A), Вычитание - (S) -->'))

print('Результат ', end='')
if action == 'M':
    print(num1 * num2)
elif action == 'D':
    print(num1 / num2)
elif action == 'A':
    print(num1 + num2)
else:
    print(num1 - num2)
