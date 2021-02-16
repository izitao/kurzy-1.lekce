#3 SCITANI POD SEBE

    #Zadani vstupu + overeni vhodnosti
while True:
    cislo_1 = input('Zadej prvni cislo: ')
    try:
        int(cislo_1)
    except ValueError:
        try:
            float(cislo_1)
        except ValueError:
            print('Zadany vstup neni ciselneho charakteru!')
        else:
            break
    else:
        break

while True:
    cislo_2 = input('Zadej druhe cislo: ')
    try:
        int(cislo_2)
    except ValueError:
        try:
            float(cislo_2)
        except ValueError:
            print('Zadany vstup neni ciselneho charakteru!')
        else:
            break
    else:
        break

    #Vypocet
soucet = float(cislo_1) + float(cislo_2)

    #Prevod celociselneho vysledku na integer, pokud je to mozne
if soucet.is_integer():
    soucet = int(soucet)

    #Formatovani vystupu
cislo_1 = f"{cislo_1}"
cislo_2 = f"+ {cislo_2}"
soucet = f"= {soucet}"

    #Zjisteni delky nejdelsiho retezce
if len(cislo_2) > len(cislo_1):
    max_delka_retezce = len(cislo_2)
elif len(cislo_1) > len(cislo_1):
    max_delka_retezce = len(cislo_1)
else:
    max_delka_retezce = len(soucet)

    #Tisknuti vystupu na obrazovku
print(f"{cislo_1.rjust(max_delka_retezce)}\n{cislo_2.rjust(max_delka_retezce)}\n"
      f"{soucet}")