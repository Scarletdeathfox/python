i = 0   
while i < 5:
    from random import randint
    print ("A on")
    a = randint(1, 10)
    print (a)
    print ("B on")
    b = randint(1, 10)
    print (b)
    c = a * b
    print ("Korruta!")
    sinu_valik = int(input())
    if sinu_valik == c:
        print ("tubli")
    else:
        print ("paha paha")
    i = i + 1
    

