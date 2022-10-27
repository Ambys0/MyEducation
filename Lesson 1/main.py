import time
import random

# number = 1
#
# while True:
#     print(number, "is natural number")
#     number += 1
#     time.sleep(1)

# seconds = 1660059105.1659868
# local = time.ctime()
# print("Local time", local)

# print("Hello, Vitaliy")
# time.sleep(2.5)
# print ("ITs ITSTEP Baby!")


# seconds = time.time()
# local = time.localtime(seconds)
# print("Результат", local)
# print("Year", local.tm_year)
# print("Hour", local.tm_hour)
# print("Hour", local.tm_min)

# print("Random number", random.randrange(1, 100, 5))

# products = [2, 5, 8, 10, 12]
# random.shuffle(products)
# print("Random products", random.sample(products, 5))

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
            break

        else:
            print("Your score is: ", count, "Bot score is: ", bot_count)

    elif choice == 'n':
        print("Count is", count)
        break
print("Good luck man!")





