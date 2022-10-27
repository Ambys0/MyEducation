a = input('Вставьте свой список: ')  #dz1_quest1
rev = list(reversed(a))
print(rev)  # да! именно хитрожопый!) но задача была поменять местами первое и последнее значение))



city = ['Івано', '+', 'Франківськ']  #dz1_quest2
new = '-'
indx = 1
city[indx] = new
print(city)  # xDDD


mlist = [1, 2, 'дима', 4.0]  #dz1_quest3
for i in mlist:
    if i == 1:
        print(type(i), 'Это целое число')
    elif i == 2:
        print(type(i), 'И это тоже целое число')
    elif i == 'дима':
        print(type(i), 'А это строка..')
    elif i == 4.0:
        print(type(i), 'А тут у нас - с плавающей точкой..')  #изи, да?))

