from Module import*
inimesed = [] 
D_vitamiini_sisaldus = []
while True:
    print("--------------------------")
    print("0-loe failist\n1-andmete lisamine\n2-salvestame failisse\n3-kustuta nimi järgi\n4-max palk ")
    v=int(input())
    if v==0:
        D_vitamiini_sisaldus=[]
        inimesed=[]
        D_vitamiini_sisaldus=loe_failist("D_vitamiini_sisaldus.txt")
        inimesed=loe_failist("nimed.txt")
        #palgad=str_to_int(palgad)
        print(D_vitamiini_sisaldus)
        print(inimesed)

    elif v==1:
        D_vitamiini_sisaldus, inimesed=elem_listisse(D_vitamiini_sisaldus,inimesed)
        print(D_vitamiini_sisaldus)
        print(inimesed)
    elif v==2:
        list_failisse(D_vitamiini_sisaldus,"D_vitamiini_sisaldus.txt")
        list_failisse(inimesed,"nimed.txt")
    elif v==3:
        D_vitamiini_sisaldus,inimesed=kustutamine(input("Sisesta nimi"),D_vitamiini_sisaldus,inimesed)
        print(D_vitamiini_sisaldus)
        print(inimesed)
    elif v==4:
        D_puudus(D_vitamiini_sisaldus,inimesed)