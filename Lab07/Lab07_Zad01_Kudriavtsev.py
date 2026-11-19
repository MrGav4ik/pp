# Laboratorium: 07; Zadanie 01; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

def analize_numbers(n1, n2, n3):
    n_sum = n1 + n2 + n3
    n_avg = n_sum / 3
    n_min = min(n1, n2, n3)
    n_max = max(n1, n2, n3)
    return n_sum, n_avg, n_min, n_max

output = analize_numbers(2, 5, 3)

print("Suma liczb:", output[0])
print("Średnia aretmetyczna liczb:", output[1])
print("Najmniejsza liczba:", output[2])
print("Największa liczba:", output[3])