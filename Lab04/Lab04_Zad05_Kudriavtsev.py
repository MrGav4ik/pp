# Laboratorium: 04; Zadanie 05; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

pin_correct = "2468"
attempts = 3

attempt_allowed = True

while attempt_allowed:
    pin = input("Podaj PIN: ")

    if pin == pin_correct:
        print("Dostęp przyznany.")
        attempt_allowed = False
    else:
        if attempts > 1:
            attempts -= 1
            print(f"Błędny PIN. Pozostało prób: {attempts}")
        else:
            print("Karta zablokowana.")
            attempt_allowed = False