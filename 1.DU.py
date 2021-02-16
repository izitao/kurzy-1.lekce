#1 HMOTNOST DESTILOVANE VODY
chyba = False
objem = input('Zadejte objem destilovane vody v cm^3: ')

#KONTROLA ZDA JE VSTUP CISLO
try:
	objem = int(objem) 
except ValueError: #Pokud nelze prevest na integer pak zkus prevest na float, muze se stat ze vstup je v desetin. tvaru
	try:
		objem = float(objem)
	except ValueError: #Pokud nelze prevest ani na float, pak je zadany vstup neciselneho charakteru
		chyba = True

if chyba:
	print('Zadany vstup neni ciselneho charakteru.')
else:
	hustota = 1 #Hustota vody v kg/cm^3
	hmotnost = objem * hustota
	print(f"Hmotnost destilovane vody je {hmotnost} kg.")
	
input()
