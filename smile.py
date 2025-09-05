def konverte(fraze):
    fraze = fraze.replace(":)","😃")
    fraze = fraze.replace(":(","☹️")
    return fraze 



ievade = input("Ievadi frāzi: ")
ievade = konverte(ievade)
print("Konvertētā frāze: ",ievade)
