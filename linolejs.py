garums = float(input("Ievadi telpas garumu:"))
platums = float(input("Ievadi telpas platumu:"))
lin_platums = float(input("Ievadi linolejas platumu:"))
lin_cena = float(input("Ievadi linolejas cenu par 1 kv.metru"))

laukums = garums * platums
nepieciešamais_daudzums = round(laukums / lin_platums)


kopējās_izmaksas = nepieciešamais_daudzums * lin_cena


print("Nepieciešamais linoleja daudzums:", nepieciešamais_daudzums, "rullīši")
print("Kopējās izmaksas:", kopējās_izmaksas, "EUR")




