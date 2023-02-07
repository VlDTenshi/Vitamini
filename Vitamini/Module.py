def loe_failist(file:str)->list:
    """Loeme failist read ja lisame järjendisse
    :param str file: Faili nimetus
    """
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def list_failisse(mas:list,file:str):
    """Salvestame loetelu failisse
    :param str file: Faili nimetus
    :param list mas: loetelu
    """
    f=open(file,"w",encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def elem_listisse(p:list,i:list):
    n=int(input("Mitu iminesi lisame?"))
    for j in range(n):
        nimi=input("Nimi: ")
        i.append(nimi)
        D_vitamiin=input("D_vitamiin: ")
        p.append(D_vitamiin)

    return p,i

def kustutamine(nimi:str,p:list,i:list):
    n=i.count(nimi)
    pos=0
    for j in range(n):
        ind=i.index(nimi,pos)
        pos=ind
        i.remove(nimi)
        p.pop(ind)
    return p,i

def D_puudus(p:list,i:list):
    p=list(map(int,p))
    if p[0]<30:
        n=p.count(D_vitamiin)
        pos=0
        print(f"See vitamiin puudub järgmistel inimestel {D_vitamiin}\nInimeste nimed:")
        for j in range(n):
            ind=p.index(D_vitamiin,pos)
            nimi=i[ind]
            print(f"{nimi}")
            pos=ind+1
    else:
        break
def keskmine_astendaja(p:list):
    p=list(map(int,p))
    keskmine_D=sum(p)/len(p)
    print("Keskmine_astendaja_D_Vitamiinid ",keskmine_D)
def suurem_astendaja(p:list,i:list):
    p=list(map(int,p))
    ule_jaak=len(max(p))
    n=p.count(ule_jaak)
    pos=0
    print("Kõige suurem D_vitamiini astendaja on: ",ule_jaak)
    for j in range(n):
        ind=p.index(ule_jaak,pos)
        nimi=i[ind]
        print(f"{nimi}")
        pos=ind+1
def otsing(i:list):
    n=0
    for j in range(n):
        nimi=input("Nimi: ")