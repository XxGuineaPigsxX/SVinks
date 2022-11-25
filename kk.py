import random 
h = random.randint(1, 20)
p = random.randint(1, 20)
prav = (p*h)/100
while True:
    h = random.randint(1, 20)
    p = random.randint(1, 20)
    prav = (p*h)/100
    otvet = float(input("найди "+ str(p) +"% от "+ str(h) +" = "))
    if otvet == prav:
        print("правильно")
    else:
        print(prav)


