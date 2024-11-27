import string

def beolvas():
    szoveg = input("Kérem adja meg a szöveget!: ")
    return szoveg

def elsoFeladat():
    szoveg = beolvas()
    hossz = len(szoveg)
    print("A szöveg hossza: " + str(hossz))

def masodikFeladat():
    szoveg = beolvas()
    sorszam = int(input("Kérem adja meg, hányadik karakterét szeretné!: "))
    if len(szoveg) < sorszam:
        print("HIBA: Nem elég hosszú a szöveg.")
    else:
        print("A kért karakter: " + szoveg[sorszam-1])

"""
def masodikFeladat():
    szoveg = beolvas()
    while True:
        sorszam = int(input("Kérem adja meg, hányadik karakterét szeretné!: "))
        if len(szoveg) < sorszam:
            print("HIBA: Nem elég hosszú a szöveg. Próbálja újra!")
        else:
            print("A kért karakter: " + szoveg[sorszam - 1])
            break
"""


def megfordit(szoveg):
    ujszoveg = ""
    for index in range(len(szoveg)-1, -1, -1):
        ujszoveg += szoveg[index]
    return ujszoveg

def szokozEltavolit(szoveg):
    # Szóközök eltávolítása
    ujszoveg = szoveg.replace(" ", "")
    return ujszoveg

def irasjelEltavolit(szoveg):
    # Írásjelek eltávolítása
    atalakitott = ""
    for betu in szoveg:
        if betu not in string.punctuation:
            atalakitott += betu
    return atalakitott

def harmadikFeladat():
    szoveg = beolvas()
    ujszoveg = megfordit(szoveg)
    # Szóközök és írásjelek eltávolítása, kisbetűssé alakítás
    eredeti_tisztitott = irasjelEltavolit(szokozEltavolit(szoveg.lower()))
    megforditott_tisztitott = irasjelEltavolit(szokozEltavolit(ujszoveg.lower()))

    if eredeti_tisztitott == megforditott_tisztitott:
        print("A szöveg palindrom.")

"""
def harmadikFeladat():
    szoveg = beolvas()
    eredeti_tisztitott = irasjelEltavolit(szokozEltavolit(szoveg.lower()))
    megforditott_tisztitott = eredeti_tisztitott[::-1]  # Egyszerű inverzálás

    if eredeti_tisztitott == megforditott_tisztitott:
        print("A szöveg palindrom.")
    else:
        print("A szöveg nem palindrom.")
"""



def negyedikFeladat():
    szoveg = beolvas()
    utolsoKarakter = szoveg[len(szoveg) - 1]
    if (utolsoKarakter == "." or
            utolsoKarakter == "," or
            utolsoKarakter == "?" or
            utolsoKarakter == "!"):
        print("Van")
    else:
        print("Nincs")


def NegyedikFeladatB():
    szoveg = beolvas()
    utolsoKarakter =  szoveg[len(szoveg) - 1]
    rosszKarakterek= ".,?!"
    if utolsoKarakter in rosszKarakterek:
        print("Van.")
    else:
        print("Nincs.")

