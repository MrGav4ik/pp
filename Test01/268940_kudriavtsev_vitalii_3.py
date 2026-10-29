number = None
incorrect = 0
correct = 0
positive = 0
negative = 0

while number != 0:
    number = input("Podaj liczbę całkowitą (int): ")

    try:
        number = int(number)

        if number > 0:
            print("Liczba jest dodatnia")
            positive += 1
            correct += 1
        elif number < 0:
            print("Liczba jest ujemna")
            negative += 1
            correct += 1
        elif number == 0:                       # Assumeing "0" shouldn't count as correct value as it finishing the program
            print("Liczba jest równa zero")     # Zakładam że zero nie liczy się jako poprawna wartość
    except ValueError:
        print("[Błąd] Podaj liczbę całkowitą!!!")
        incorrect += 1 # bonus

print(f"{correct} poprawnie podanych wartości, {positive} wartości dodatnich oraz {negative} wartości ujemnych, {incorrect} niepoprawnie podanych wartości")