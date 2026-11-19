# Laboratorium: 07; Zadanie 03; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

def fibonacci(n):
    if n > 1:
        try:
            return fibonacci(n-1) + fibonacci(n-2)
        except TypeError:
             return("Podano niewłaściwy argument")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return("Podano niewłaściwy argument")
    

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(2.5))
print(fibonacci(-1))
#print(fibonacci(40))

