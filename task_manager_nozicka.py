ukoly = []

def pridat_ukol(nazev, popis):
    novy_ukol = {'nazev': nazev, 'popis': popis}
    ukoly.append(novy_ukol)
    print(f"Úkol '{nazev}' byl přidán.")

def zobrazit_ukoly():
    print("Seznam úkolů:\n")
    for index, ukol in enumerate(ukoly, 1):
        print(f"{index}. {ukol['nazev']} - {ukol['popis']}")    

def odstranit_ukol():
    zobrazit_ukoly()

    try:
        cislo = int(input("Zadejte číslo úkolu ke smazání:\n"))
        index_mazani = cislo -1

        if 0 <= index_mazani < len(ukoly):
            vymazany = ukoly.pop(index_mazani)
            print(f"Úkol '{vymazany['nazev']}' byl smazán!")
        else:
            print("Upozornění! Zadal jste číslo neexistujícího úkolu.")
    except ValueError:
        print("Chyba! Zadejte platné číslo.")

def hlavni_menu():
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

def spustit_spravce_ukolu():
    while True:
        hlavni_menu()
        try:
            volba = int(input("Vyberte možnost (1-4):\n"))

            if volba == 1:
                while True:
                    nazev_ukolu = input("Zadejte název úkolu: ").strip()
                    if nazev_ukolu:
                        break
                    print("Chyba! Název úkolu nesmí být prázdný!")

                while True:
                    popis_ukolu = input("Zadejte popis úkolu: ").strip()
                    if popis_ukolu:
                        break
                    print("Chyba! Popis úkolu nesmí být prázdný!")

                pridat_ukol(nazev_ukolu, popis_ukolu)

            elif volba == 2:
                zobrazit_ukoly()

            elif volba == 3:
                odstranit_ukol()

            elif volba == 4:
                    print("Konec programu.")
                    break
            else:
                print("Neplatná volba, vybete 1-4.")

        except ValueError:
            print("Chyba: Zadejte prosím číslo od 1 do 4.")

spustit_spravce_ukolu()