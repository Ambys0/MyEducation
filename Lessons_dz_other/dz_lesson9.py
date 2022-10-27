import random
cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(cards)
print("Lets play 21!")
count = 0
bot_count = 0
while True:
    choice = input("Take card? y/n \n")
    if choice == 'y':
        current = cards.pop()
        current_bot = cards.pop()
        print("You take", current)
        count += current
        bot_count += current_bot
        if count > 21:
            print("You loose. You have a ", count, "Bot count is:", bot_count)
            break

        elif count == 21:
            print("You win a game. You score is: ", count, "Bot score is: ", bot_count)
            continue

        else:
            print("Your score is: ", count, "Bot score is: ", bot_count)

    elif choice == 'n':
        print("Count is", count)
        continue
print("Good luck man!")
