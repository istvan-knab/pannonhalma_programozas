"""
Knáb István Gellért
SZTAKI
2023.08.01.
"""

# Onallo feladat
# Todo: Készíts egyszerű programot ami megvalósít egy számológépet,
#  de a művelet kiválasztása és megvalósítása is függvényekkel legyen lebonyolítva


def muvelet(szam1, szam2, muveleti_jel):
    pass

def osszead():
    pass

def kivon():
    pass

def szoroz():
    pass

def oszt():
    pass

def kiir(eredmeny):
    print(eredmeny)

if __name__ == "__main__":
    szam1 = input("Add meg az elso szamot")
    szam2 = input("Add meg a masodik szamot")
    muveleti_jel = input("mi legyen a muvelet?")
    eredmeny = muvelet(szam1, szam2, muveleti_jel)
    kiir(eredmeny)