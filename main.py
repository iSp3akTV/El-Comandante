# *************  Ce va avea acest Calculator?  *********************
# 1.Adunari
# 2.Scaderi
# 3.Inmultiri
# 4.impartiri

print("Selectati o operatie pentru a continua:")
print("1. ADUNARE")
print("2. SCADERE")
print("3. INMULTIRE")
print("4. IMPARTIRE")

operation=input()

if operation == "1":
    #code pentru adunare
    num1 = input("Introduceti primul numar:  ")
    num2 = input("Introduceti al doilea numar:  ")
    print("Suma este: " + str(int(num1) + int(num2)))

elif operation  == "2":
    #pentru scadere
    num1 = input("Introduceti primul numar:  ")
    num2 = input("Introduceti al doilea numar:  ")
    print("Diferenta este: " + str(int(num1) - int(num2)))

elif operation  == "3":
    #pentru inmultire
    num1 = input("Introduceti primul numar:  ")
    num2 = input("Introduceti al doilea numar:  ")
    print("Produsul este: " + str(int(num1) * int(num2)))

elif operation  == "4":
    #pentru impartire
    num1 = input("Introduceti primul numar:  ")
    num2 = input("Introduceti al doilea numar:  ")
    print("Rezultatul este: " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")