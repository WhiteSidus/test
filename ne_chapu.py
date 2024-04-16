zbozi = ["Jablko", "Hruška", "Tomat"]
kosik = []

def print_seznam(element):
    for x in range(len(element)):
        print(f"Tady mate neše zboži pod čislem {x+1} - {zbozi[x]}")

def kosik_pridavame(zbozi, cislo_produktu, kosik):
    kosik.append(zbozi)
    zbozi.pop(cislo_produktu)
    print(f"{zbozi[cislo_produktu]} byla přidána do košíku")

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

    cislo_produktu = int(vyber) - 1
    kosik_pridavame(zbozi, cislo_produktu, kosik) if 0 <= cislo_produktu < len(zbozi) else print("Neplatná volba. Zadejte prosím platné číslo!")