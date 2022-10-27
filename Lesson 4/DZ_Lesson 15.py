import random

while True:
    user_action = input("Выбери вариант (камень, бумага, ножницы): ")
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = random.choice(possible_actions)
    you_score = 0
    comp_score = 0
    print(f"\nТы выбрал {user_action}, компьютер выбрал {computer_action}.\n")
    if user_action == computer_action:
        print(f"Вы выбрали одинаковый вариант. {user_action}. Это ничья!")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Камень точит ножницы! Вы победили!")
            you_score = you_score + 1
        else:
            print("Бумага накрывает камень! Вы проиграли.")
            comp_score = comp_score + 1
        print("Ваши очки: ", you_score, "Очки компьютера: ", comp_score)
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Бумага накрывает камень! Вы победили!")
            you_score = you_score + 1
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
            comp_score = comp_score + 1
        print("Ваши очки: ", you_score, "Очки компьютера: ", comp_score)
    elif user_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
            you_score = you_score + 1
        else:
            print("Камень точит ножницы! Вы проиграли.")
            comp_score = comp_score + 1
        print("Ваши очки: ", you_score, "Очки компьютера: ", comp_score)

