def iemet_monetu():
    while True:
        m = int(input("Ievadi monētas nominālu: "))
        if m == 25 or m == 10 or m == 5:
            return m
        else:
             print("Nederīgs nomināls")



nauda = 0
while nauda < 50:
    nominals = iemet_monetu()
    nauda += nominals
    rezultats = nauda - 50
    if rezultats >= 0:
            print("Pirkums veikts! Atlikumā atdos",rezultats,"centus!")
    else:
            print("Pirkumam nepieciešami vēl",50 - nauda,"centi")
   