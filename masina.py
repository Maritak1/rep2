def parbaude(ievade):
    #vai ir vismaz 2 burti
    if len(ievade) < 2 or not ievade[:2].isalpha():
        return False
    
    #vai pārējie simboli ir cipari
    for simbols in ievade[2:]:
        if not simbols.isdigit():
         return False
        
    #vai cipari nesākas ar 0
    if ievade[2] == '0':
        return False
    
    #kopējais garums nav lielāks par 6 simb
    if len(ievade) > 6:
        return False
    
        return True



ievade = input("Ievadi numurzīmi: ")

if parbaude(ievade):
    print("Derīga")
else:
    print("Nederīga")