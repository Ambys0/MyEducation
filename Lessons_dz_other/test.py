age = int(input("Введите свой возраст: "))
gender = str(input("Man or Woman: "))
if age < 18 and gender == "Man":
    print("Ты слишком мал для этого сайта! Иди в школу учись малец!")
elif age < 18 and gender == "Woman":
    print("Ты слишкам маленькая девочка для этого сайта!")

if age >= 18 and gender == "Man":
        print("Добро пожаловать Мужчина!")
elif age >= 18 and gender == "Woman":
        print("Добро пожаловать Девушка!")