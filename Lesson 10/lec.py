f = open('/home/ambys/Work/MyRepo/Basic/20.09/text.txt', 'r')
while True:
    dino = f.read()
    print(dino)
    if not dino:
        break
f.close()
