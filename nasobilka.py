import random

def nasobeni(x,y):
    vysledek = x * y
    return vysledek

def vyhodnoceni(vysledek, porovnani):
    if vysledek == porovnani:
        print("zvladl jsi to")
    else:
        print("udělal jsi chybu, zkousej to dal")


for a in range(99):
    x = random.randint(1,100)
    y = random.randint(1,5)


    porovnani = int(input(f"{x} * {y} = "))
    vysledek = nasobeni(x,y)
    vyhodnoceni(vysledek, porovnani)