def patskani(teksts):
    v_patskani ="AĀEĒIĒOUŪaāeēiīouū"
    rezultats =""
    for burts in teksts:
        if burts not in v_patskani:
            rezultats += burts
    return rezultats


ievade = input("Ievadi virkni: ")
izvade = patskani(ievade)
print(izvade)