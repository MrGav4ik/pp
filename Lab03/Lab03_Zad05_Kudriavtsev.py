# Laboratorium: 03; Zadanie 05; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

length1 = float(input("Wprowadź długość pierwszego odcinka: "))
length2 = float(input("Wprowadź długość drugiego odcinka: "))
length3 = float(input("Wprowadź długość trzeciego odcinka: "))

sum12 = length1 + length2
sum13 = length1 + length3
sum23 = length2 + length3

if sum12 < length3 or sum13 < length2 or sum23 < length1:
    print("Z odcinków nie można zbudować trójkąt")
else:
    if (length1 + length2 + length3) / 3 == length1:
        print("Trójkąt jest równoboczny")
    elif length1 == length2 or length1 == length3 or length2 == length3:
        print("Trójkąt jest równoramienny")
    else:
        print("Trójkąt jest różnoboczny")