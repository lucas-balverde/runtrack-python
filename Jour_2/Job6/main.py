def calc(nombre):
    if nombre < 0: 
        return "negatif"
    elif nombre >= 0:
        return "positif"

print(calc(5))
print(calc(-2))
print(calc(0))