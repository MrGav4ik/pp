# Laboratorium: 04; Zadanie 01; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

for i in range(0, 4):
    globals()['string%s' % i] = input(f"Podaj tekst nr {i}: ")
    print(f"W zmiennej '{'string%s' % i}' zapisano tekst:", globals()['string%s' % i])
