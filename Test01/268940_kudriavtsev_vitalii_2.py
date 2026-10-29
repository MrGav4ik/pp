month_number = input("Podaj liczbę całkowitą z zakresu 1..12: ")

months = [
    "Styczeń – zima",
    "Luty – zima",
    "Marzec – wiosna",
    "Kwiecień – wiosna",
    "Maj – wiosna",
    "Czerwiec – lato",
    "Lipiec – lato",
    "Sierpień – lato",
    "Wrzesień – jesień",
    "Październik – jesień",
    "Listopad – jesień",
    "Grudzień – zima",
]

try:
    month_number = int(month_number)

    if month_number >= 1 and month_number <= 12:
        print(f"{month_number} – {months[month_number - 1]}")
    else:
        print("Podano niewłaściwą liczbę")

except:
    print("Podanj liczbę całkowitą")