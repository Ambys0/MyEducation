def numbers(nm1): #Qwest1
    print(nm1 + nm1 ** 2 + nm1 **3)
numbers(10)

def summary (nm1, nm2): #Qwest2
    if nm1 % 2 != 0:
        nm1 += 1
    for x in range (nm1, nm2 + 2, 2):
        print(x)
summary(10, 100)