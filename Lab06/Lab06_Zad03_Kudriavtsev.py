# Laboratorium: 06; Zadanie 03; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

file_path = input("Wpisz ścieżkę pliku: ")
result_path = input("Wpisz ścieżkę pliku poprawionych danych: ")
counter = 0

with open(file_path, "r", encoding="utf-8") as file:
    print("Imiona wczytane z pliku dane.txt")
    for number, name in enumerate(file, 1):
        name = name.replace("\n", "")
        print(f"{number}. {name}")

        open(result_path, 'w').close()
        
        with open(result_path, "a", encoding="utf-8") as result:
            name_capital = name.upper()         # "zamieni wszystkie imiona na pisane wielkimi literami",
            result.write(name_capital + "\n")   # jezeli w zadaniu chodziło o pierwzą literę warto użuc funkcji capitaize()
            counter += 1

    print(f'Zapisano {counter} imiona do pliku {result_path}')
