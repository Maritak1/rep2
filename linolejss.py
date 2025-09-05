def aprēķināt_linoleja_daudzumu_un_izmaksas(cena_m2, l_platums, telpas_platums, telpas_garums):

  telpas_laukums = telpas_platums*telpas_garums

  nepieciešams_linoleja_garums = telpas_laukums/l_platums

  izmaksas = telpas_laukums*cena_m2

  return nepieciešams_linoleja_garums, izmaksas

cena_m2 = float(input("Ievadiet linoleja cenu par 1 kv.m: "))
l_platums = float(input("Ievadiet linoleja platumu mrtros: "))
telpas_platums = float(input("Ievadiet telpas platumu metros: "))
telpas_garums = float(input("Ievadiet telpas garumu metros: "))

linoleja_garums, izmaksas = aprēķināt_linoleja_daudzumu_un_izmaksas(cena_m2, l_platums, telpas_platums, telpas_garums)

print(f"Jums nepieciešams {linoleja_garums:.2f} metri linoleja")
print(f"Linoleja izmaksa būs {izmaksas:.2f} EUR")