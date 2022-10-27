enter = int(input("Введите колличество метров: "))
duim = enter * 39.36996
yard = enter * 1.9
miles = enter / 1609
print("Выберите в какую величину вам перевести: ")
vel = input("Введите: 'duim', 'yard', 'miles': ")
if vel == 'duim':
    print("Ваш результат: ", duim, "дюйма")

if vel == 'yard':
    print("Ваш результат: ", yard, "ярда")

elif vel == 'miles':
    print("Ваш результат: ", miles, "мили")

else:
    print("Это не сложно...")







