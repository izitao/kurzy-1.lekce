# 2 GENERATOR ZAPAMATOVATELNEHO HESLA

import random

chyba_format_veku = False  #True spusti prevod retezce veku na retezec obsahujici cislo

uzivatelske_jmeno = input('Zadej uzivatelske jmeno: ')

while uzivatelske_jmeno == '' or uzivatelske_jmeno == None:
    uzivatelske_jmeno = input('Zadej uzivatelske jmeno:')

vek = input('Zadej svuj vek: ')

#KONTROLA ZDA JE VSTUP CISLO
try:
	vek = int(vek)
except ValueError: #Pokud nelze prevest na integer pak je vstup neciselneho charakteru
	chyba_format_veku = True


vek = str(vek) #Prevod int na retezec

novy_vek = ' ' #Promenna pro opraveny vystup veku

#VYTVORENI RETEZCE Z CISLIC POKUD UZIVATEL NEZADA ZADNY VSTUP
    #POKUD JE ZADANY VSTUP PRAZDNY, PAK VYTVOR RETEZEC SLOZENY Z CISLIC
if (vek == '' or vek == None) and chyba_format_veku:
    print('Nebyl zadan zadny vek.')
    seznam_veku = list(vek)
    for index in range(3):
        seznam_veku.append(random.randint(0, 9))

    novy_vek = novy_vek.join(str(ele) for ele in seznam_veku)
    vek = novy_vek.replace(" ", "")
    chyba_format_veku = False

    #POKUD JE ZADANY VSTUP NECISELNEHO CHARAKTERU, PAK NAHRAD JEDEN ZNAK CISLICI (TAK ABY BYLO V HESLE ALESPON JEDNA CISLICE)
elif chyba_format_veku == True:
    print('Zadany vek neni ciselneho charakteru, jeho cast bude nahrazena cislem!')
    index_nahrazeni_znaku = random.randint(1, len(vek)) - 1  #Pozice znaku v retezci, ktera bude nahrazena cislem
    seznam_veku = list(vek) #Prevod reztezce na seznam
    for index in range(len(vek)):
        if index == index_nahrazeni_znaku:
            seznam_veku[index] = str(random.randint(0, 9)) #Vybranou pozici v retezci nahrad cislici od 0 do 9

    novy_vek = novy_vek.join(str(ele) for ele in seznam_veku) #Uprava formatovani vystupu

    vek = novy_vek.replace(" ", "") #Vymazani mezer v retezci

misto_narozeni = input('Zadej misto narozeni (volitelne): ')

heslo = uzivatelske_jmeno.title() + vek   #Heslo vznikne sloucenim zadaneho jmena a veku (narozeni se nepouzije)

print(f"Tve heslo je: {heslo}")
