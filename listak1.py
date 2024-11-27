import random

def szoBeolvas():
    szo = input("Kérem adjon meg egy szót!: ")
    return szo

def elsoFeladat():
    # Üres lista létrehozása
    listam = []

    # 5 szó bekérése és hozzáadása a listához
    for db in range(0, 5, 1):
        szo = szoBeolvas()
        listam.append(szo)

    # Első ciklus: kiírás index alapján, minden szó után szóköz
    for index in range(0, len(listam), 1):
        print(str(listam[index]) + " ", end="")
    print()

    # Második ciklus: kiírás a lista elemein iterálva, szóközzel elválasztva
    for elem in listam:
        print(elem, end=" ")
    print()

    # b feladat
    db = 0;
    for elem in listam:
        if len(elem)==5:
            db += 1
            print("5 hosszú gyümölcsök száma:"+str(db)+".")
            #körte, málna, banán, egres, szőlő

    # c feladat

    db = 0
    for elem in listam:
      if "k" in elem:
        db += 1
        print("K betűt tartalmazó gyümölcsök száma: " + str(db) + ".")


def masodikFeladat():
    #1. Lépés: Listák létrehozása

    list1 = list(range(0, 31, 2))  # Páros számok 0-tól 30-ig
    list2 = list(range(39, 20, -2))  # Páratlan számok 39-től 21-ig

    # 2. Lépés: Két lista összefűzése
    list1.extend(list2)

    # 3. Lépés: Minden 3. helyre véletlen szám beillesztése 40 és 70 között
    for i in range(2, len(list1), 3):  # Indulunk a 3. helytől (index 2)
        list1.insert(i, random.randint(40, 70))

    # 4. Lépés: Lista kiírása 5-önkénti sortöréssel
    for i in range(len(list1)):
        if i % 5 == 0 and i != 0:  # Minden 5. elem után sortörés
            print()
        print(list1[i], end=" ")  # Kiíratás, szóközzel elválasztva




def harmadikFeladat():
    n = int(input("Add meg a lista hosszát (20 és 30 közötti véletlen számok): "))

    # Létrehozzuk a listát véletlen számokkal 20 és 30 között
    random_list = [random.randint(20, 30) for _ in range(n)]

    # a) Megszámoljuk, hány olyan szám van, ami osztható a lista hosszával (n)
    divisible_by_n = sum(1 for num in random_list if num % n == 0)

    # b) Kiszámoljuk az átlagot
    average = sum(random_list) / len(random_list)

    # Eredmények kiírása
    print("A lista elemei:", random_list)
    print(f"A {n}-nal osztható számok száma: {divisible_by_n}")
    print(f"Az átlag: {average:.2f}")



def atlag(szamok, tizedes):
    return round(sum(szamok) / len(szamok), tizedes)

def negyedikFeladat():
    # Kérjük be a lista hosszát
    n = int(input("Add meg a lista hosszát: "))

    # Kérjük be a tizedes jegy pontosságot
    tizedes = int(input("Add meg a tizedes jegy pontosságát: "))

    # Létrehozzuk a listát véletlen számokkal 20 és 30 között
    random_list = [random.randint(20, 30) for _ in range(n)]

    # Az átlag kiszámolása eljárással
    lista_atlag = atlag(random_list, tizedes)

    # Eredmény kiírása
    print("A lista elemei:", random_list)
    print(f"Az átlag a {tizedes} tizedes jegy pontosságával: {lista_atlag}")