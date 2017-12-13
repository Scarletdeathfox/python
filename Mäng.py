print ("Tere mis su nimi on?")
myName = input ()
print (myName+ ",tere tulemast mängu kus pead tegema valikuid." )

Answer = print("Sa kohtad hunti, mida teha? a) Tee hundile pai   b) Jookse ära")
Answer = input ()
if Answer == ("a"):
    print("Hunt tuli kallale ja sa surid")
    print("THE END!")
else:
    print("Hea valik, kuid hunt jookseb su järel")
    teine_Answer = print("Sul on valik a)joosta sügavamale metsa    b) ronida suure kivi otsa")
    teine_Answer = input ()
    if teine_Answer == ("a"):
        print("Sa eksid veel sügavamale metsa ja väsid.")
        print("Hunt jõuab järgi ja rebib su surnuks")
        print("THE END!")
    else:
        ("Parim vähestest valikutsest, kuid nüüd sa ei saa kuskile joosta")
        kolmas_Answer = print("Sul on valik a)karjuda appi b) oodata kuni keegi su leiab, vaikselt.")
        kolmas_Answer = input()
        if kolmas_Answer == ("b"):
            print("Sa ootasid liiga kaua ja nälg tappis su")
            print("THE END!")
        else:
            print("Sa karjusid piisavalt kaua appi")
            print("Üksik jahimees ehmatas hundi")
            print("Pääsesid edukalt metsast eluga!")
            print("HAPPY END!")
       


    

    
