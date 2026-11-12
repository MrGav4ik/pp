# Laboratorium: 06; Zadanie 04; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

running = True

cart = []

print("Menu: 1 – dodaj, 2 – usuń, 3 – wyświetl, 0 – zakończ")

while running:
    try:
        choice = int(input("Wybór: "))

        match choice:
            case 1:
                item = input("Co dodać? ")
                cart.append(item)
            case 2:
                item = input("Co usunąć? ")
                try:
                    cart.remove(item)
                except ValueError:
                    print(f'Produktu "{item}" nie ma na liście.')
            case 3:
                if len(cart) != 0:
                    for num, item in enumerate(cart, 1):
                        print(f"{num}. {item}")
                else:
                    print("Lista zakupów jest pusta")
            case 0:
                print("Koniec programu.")
                running = 0

            case _:
                print("Menu: 1 – dodaj, 2 – usuń, 3 – wyświetl, 0 – zakończ")

    except ValueError:
            print("Menu: 1 – dodaj, 2 – usuń, 3 – wyświetl, 0 – zakończ")