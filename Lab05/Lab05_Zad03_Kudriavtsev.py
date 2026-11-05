# Laboratorium: 05; Zadanie 03; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

text = "Ala ma koty"
number = 2
res = ""

words = text.split(" ")

for i in range(0, len(words)):
    if i != 2:
        res += f"{words[i]} "
    else:
        res += f"{str(number)} {words[i]}"

res_join = "-".join(res.split(" "))

print(res_join)