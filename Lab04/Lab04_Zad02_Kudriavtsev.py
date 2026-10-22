# Laboratorium: 04; Zadanie 02; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

value = None
value_int = None

print("""
Program przyjmuje od Użytkownika liczby typu int w pętli while.
Podanie 1234 kończy program.
""")

while value_int != 1234:
    value = input("Podaj liczbę całkowitą: ")
    try:
        value_float = float(value)

        try:
            value_int = int(value)
            print(f"Podano liczbę całkowitą: {value_int}")
        except ValueError:
            print(f'Podany ciąg "{value}" jest liczbą zmiennoprzecinkową!')

    except ValueError:
        print(f'Podany ciąg "{value}" jest tekstem!')