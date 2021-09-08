pizzaSmall = 4
pizzaMedium = 7
pizzaLarge = 10
smallAmount = mediumAmount = largeAmount = 0

# Geeft de klant de mogelijkheid om de 3 verschillende soorten pizza's te bestellen.
def bestellingMaker():
    global smallAmount
    global mediumAmount
    global largeAmount

    pizzaType = input("Wat voor pizza wilt u? ").lower()
    inputAmount = int(input("Hoeveel " + str(pizzaType) + " pizza's wilt u? "))

    if pizzaType == "small":
        smallAmount += inputAmount
    elif pizzaType == "medium":
        mediumAmount += inputAmount
    elif pizzaType == "large":
        largeAmount += inputAmount
    else:
        print("Dit is geen type pizza! Vul een geldige type pizza in.")
        bestellingMaker()
    
    meerBestellen()

# Rekent het te betalen bedrag uit en geeft het bonnetje door aan de klant.
def rekeningMaker():
    smallPrice = smallAmount * pizzaSmall
    mediumPrice = mediumAmount * pizzaMedium
    largePrice = largeAmount * pizzaLarge
    totalPrice = smallPrice + mediumPrice + largePrice

    print(" ----------------------------------------------------")
    a = print("|  " + str(smallAmount) + " small pizza's      : " + str(smallPrice) + " euro") if smallAmount > 0 else 0
    b = print("|  " + str(mediumAmount) + " medium pizza's      : " + str(mediumPrice) + " euro") if mediumAmount > 0 else 0
    c = print("|  " + str(largeAmount) + " large pizza's      : " + str(largePrice) + " euro") if largeAmount > 0 else 0
    print("|  Uw totale bedrag is   : " + str(totalPrice) + " euro")
    print(" ----------------------------------------------------")

# Geeft de klant de mogelijkheid om verder te bestellen of om de bon te ontvangen.
def meerBestellen():
    meerVraag = input("Wilt u nog meer bestellen? ").lower()

    if meerVraag == "ja":
        bestellingMaker()
    elif meerVraag == "nee":
        rekeningMaker()
    else:
        print("Dit is geen geldig antwoord. Beantwoord deze vraag alleen met ja of nee.")
        meerBestellen()

bestellingMaker()