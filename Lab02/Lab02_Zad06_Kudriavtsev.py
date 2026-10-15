# Laboratorium: 02; Zadanie 06; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

netto = float(input("Podaj cenę netto produktu: "))
vat = int(input("Podaj stawkę VAT w procentach: "))

podatek = netto * vat / 100
brutto = netto + podatek

print(f"Kwota podatku VAT: {podatek} zł")
print(f"Cena brutto produktu: {brutto} zł")