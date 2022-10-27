health_pers = 10
armore_pers = 5
health_spider = 5
silaPav = 5
sila=5
put = input("[vlivo][vpravo][vpered][nazad]:")
if (put=="vlivo"):
 print("Ви знайшли меч. Ваша сила збільшилась!")
 print(sila+5)
elif(put=="vpravo"):
    print("Ви натрапили на павука, ваше здоров'я зменшилось!")
    print(health_pers-silaPav)
elif(put=="vpered"):
    print("Ви зробили крок вперед,натрапили на пастку і впали в яму з шипами. Ваше здоров'я:")
    print(health_pers-10)
    print("Game Over")
else:
    print("Ви залишились на місці і побачили захований шолом у тріщинах печери. Ваша броня збільшилась:")
    print(armore_pers+20)
