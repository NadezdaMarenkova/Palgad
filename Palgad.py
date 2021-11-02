from random import*
inimesed=["Anna","Tomm","Anna","Max"]
palgad=[1200,2000,1560,1200]

def sisesta_andmed(i,p):   #Добавить еще несколько человек и зарплат(кол-во говорит пользователь)
    global N
    N=4
    for n in range(N):
        inimene=input("Nimi: ")
        i.append(inimene)
        palk=randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p): #удалить человека и его зарплату (вводим имя)
    nimi=input("Sisesta nimi, keda vaja kustutada:")
    n=i.count(nimi) #кол-во
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t, ". ", i[e],"-",p[e])
        j=int(input("Järjekordne number:"))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p


def suurim_palk(i,p):
    suurim=max(p)    #Самую большую зарплату и кто ее получает
    start_ind=-1
    x = p.count(suurim_palk)
    for j in range (x):
        ind = p.index (suurim_palk, start_ind)
        print ("Kõrgeima palgaga inimene : ", i[ind], "palk on ", p[ind])
        start_ind+=ind+1
        print()
 

def minimaalne_palk(i,p): #Кто получает самую маленькую зарплату и какую именно
    minimaalne=min(p)
    start_ind=-1
    x = p.count (minimaalne_palk)
    for j in range(x):
        ind = p.index (minimaalne_palk , start_ind)
        print ("Madalaima palgaga inimene : ", i[ind], "palk on ", p[ind])
        start_ind+=ind+1
        print()

def keskmine(i,p):    #Кто  получает среднюю зарплату
    summa=0
    for palk in p:
        summa+=palk
        summa/=len(p)
        print ("Keskmine palk: ", summa)
        for palk in p:
            if palk==summa:
                n=p.index(palk)
                print("Saab kätte", i[n])
            else:
                ("Sellised inimesed puuduvad")
#inimesed=["Anna","Tomm","Anna","Max"]
#palgad=[1200,2000,1560,1200]
keskmine(inimesed, palgad)



def sorteerimine(i,p,v):   #Упорядочить зарплаты в порядке возрастания и убывания вместе с именами
    N=len(p)
    if v==1:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i,p)

      #count() for abi_list p.index()->i.index() andmed_ekranile (abi_list)
def sort_nimi_jargi(p,i,v):   #Упорядочить зарплаты в порядке возрастания и убывания вместе с именами,
    N=len(p)
    if v==1:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i,p)

def vordsed_palgad(i,p):   #Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран.
    N=len(p)
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list (set(dublikatid))
    print(dublikatid)
    for palk in dublikatid:
        n=p.count(palk)
        print(n)
        k=0
        for j in range(n):
            k=p.index(palk,k)
            print(k)
            nimi=i[k]
            print(nimi)
            print (palk,"Saab kätte", nimi)
#inimesed=["Anna","Tomm","Anna","Max"]
#palgad=[1200,2000,1560,1200]
vordsed_palgad(inimesed,palgad)

def Tulumaks(i,p):
    salary12=0
    number=0
    for tg in range(len(p)):
        if p[tg]<=1200:
            number=int(p[tg])
            salary12=(number-((number-500)*0.2))
            print (salary12,"-"i[tg])





while 1:
    print("a-andmete sisestamine\ne-andmed ekranile\nk-kustutamine\nmin-kellel on minimum palk\nmax-kellel on suurim palk\kesk-kellel on keskmine palk\ns-sort\nv-vordsed")
    valik=input()
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=="k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=="min":
        minimaalne_palk(inimesed,palgad)
    elif valik.lower()=="max":
        suurim_palk(inimesed,palgad)
    elif valik.lower()=="kesk":
         keskmine(inimesed,palgad)
    elif valik.lower()=="s":
        sorteerimine(inimesed,palgad,int(input("1-kahaneb, 2-kasvab")))
    elif valik.lower()=="v":
        vordsed_palgad(inimesed,palgad)


    else:
        break


inimesed,palgad=sisesta_andmed(inimesed,palgad)
andmed_ekranile(inimesed,palgad)



print(inimesed)
print(palgad)