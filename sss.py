def rekina(x, operators, z):
    x = int(x)
    z = int(z)
    if operators == "+":
        rezultats = x + z
    elif operators == "-":
        rezultats = x - z
    elif operators == "*":
        rezultats = x * z
    else:
        rezultats = x / z
    return round(float(rezultats),1)

ievade = input("Ievadi matemātisko izteiksmi x y z, kur y-darbība: ")
ievade_dalita = ievade.split()
if len(ievade_dalita) != 3:
    print("Nepareizs ievades formāts!")
else:
    x, operators, z = ievade_dalita
    rezultats = rekina(x, operators, z)
    print("Rezultāts:",rezultats)

