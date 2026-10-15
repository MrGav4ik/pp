# Laboratorium: 02; Zadanie 05; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

s = int(input("Podaj liczbę sekund: "))

h = s // 3600
m = (s % 3600) // 60
sek = s % 60

print(f"dla {s} sekund: {s} s to {h} h {m} min {sek} s")