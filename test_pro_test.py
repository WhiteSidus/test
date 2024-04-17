zbozi = ["Jablko", "Hruška", "Tomat"]
kosik = []

def print_seznam(element):
    for x in range(len(element)):
        print(f"Tady mate neše zboži pod čislem {x+1} - {zbozi[x]}")

def kosik_pridavame(zbozi, cislo_produktu, kosik):
    if vyber.isdigit():  # Kontrola, zda je vstup číslo
        cislo_produktu = int(vyber) - 1
        if cislo_produktu < len(zbozi):
            kosik.append(zbozi[cislo_produktu])
            zbozi.pop(cislo_produktu)
            print(f"{kosik[-1]} byla přidána do košíku")
        else:
            print("Neplatná volba. Zadejte prosím platné číslo!")
    else:  # Pokud není vstup číslo, předpokládáme, že je to název produktu
        if vyber in zbozi:
            kosik.append(vyber)
            zbozi.remove(vyber)
            print(f"{vyber} byla přidána do košíku")
        else:
            print("Neplatná volba. Zadejte prosím platný název produktu.")

while True:
    print (" ")
    print ("---------------------------------")
    print ("Vitejte v našem Obchodu!")
    print ("---------------------------------")
    print (" ")
    print ("---------------------------------")
    print ("Zde si vyberte z našiho zboží")
    print ("Vybirat mužete pomoci čisla")
    print ("Pro ukončení zadejte slovo <KONEC>")
    print ("---------------------------------")    
    print ("")
    print_seznam(zbozi)
    print ("")
    print("Vaš košik: ")
    if len(kosik) > 0:
        s = ", "
        o = s.join(kosik)
        print(o)
    else:
        print("Košík je prázdný")
    print ("")

    vyber = input("Vyberte položku podle čísla: ")

    if vyber == 'KONEC':
        break
    elif vyber == "konec":
        break

    kosik_pridavame(zbozi, vyber, kosik)