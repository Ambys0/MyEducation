text = input("Введите текст: ").lower()

count = 0

for i in 'аеиоуюя':
    count += text.count(i)
print(count)