name = input("Введите свое имя: ")
height = int(input("Введите свой рост в сантиметрах: "))
weight = int(input("Укажите ваш вес: "))
form = (height - 100) * 1.15
if height <= form:
    print("У вас идеальный вес!")
else:
    print(name, "Ваш идеальный вес: ", form)