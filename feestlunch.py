aantalCroissant = int(input("Geef aan hoeveel croissantjes u wilt: "))
aantalStokbrood = int(input("Geef aan hoeveel stokbroodjes u wilt: "))
aantalBon = int(input("Geef aan hoeveel cadeaubonnen u heeft: "))

bedrag = aantalCroissant * 39 + aantalStokbrood * 278 - aantalBon * 50

print("De feestlunch kost je bij de bakker " + str(bedrag) + " eurocent voor de "
+ str(aantalCroissant) + " croissantjes en de " + str(aantalStokbrood)
+ " stokbroden als de " + str(aantalBon) + " kortingsbonnen nog geldig zijn!")