import socket
from datetime import datetime
import random
import math
import sys
from _thread import *

EmriIServerit = '127.0.0.1'
PortiIServerit = 14000

adresa=(EmriIServerit,PortiIServerit)
serverS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    serverS.bind(adresa)
except socket.error:
    print("Lidhja me klientin nuk eshte arritur!")
    sys.exit()   #importojm paketen per sys

#Metoda IP
def IP():
    pergjigjja = str(EmriIServerit)
    return pergjigjja

#Metoda NRPORTIT
def NRPORTIT():
    pergjigjja =str(adresaa[1])
    return pergjigjja

#Metoda NUMERO
def NUMERO(tekst):
    zanore=0
    bashketingellore=0
    for i in tekst:
        if (i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u'or i=='A' or i=='E'or i=='I' or i=='O'or i=='U'):
            zanore=zanore+1
        else:
            bashketingellore=bashketingellore+1
    pergjigjja=str("Teksti ka "+str(zanore) +" zanore dhe " +str(bashketingellore)+" bashkëtingëllore.")
    return pergjigjja 

#Metoda ANASJELLTAS
def ANASJELLTAS(tekst):
    pergjigjja=tekst[::-1]
    return pergjigjja

#Metoda PALINDROM
def PALINDROM(tekst):
    w=""
    for i in tekst:
        w=i+w
    
    if(tekst==w):
        return "Teksti i dhënë është palindrome"
    else:
        return "Teksti nuk është palindrome"

#Metoda KOHA
def KOHA():
    from time import gmtime, strftime
    pergjigjja = strftime("%d.%m.%Y %I:%M:%S %p")
    return pergjigjja

#Metoda LOJA
def LOJA():
    NumerRandom = ""
    for x in range(1,6):
        #radint() kthen një numër të plotë
        randomNu = random.randint(1,35)
        NumerRandom += str(randomNu) + " "
    return NumerRandom

#Metoda KONVERTO
def KONVERTO(zgjedhja, vlera):
    if(zgjedhja=="CMTOINCH"):
        #Metoda format kthen vlerën e numrit të përcaktuar duke marrë parasysh .2f
        pergjigjja=format((vlera / 2.54),".2f")
    elif(zgjedhja=="INCHNECM"):
        pergjigjja = format((vlera * 2.54),".2f")
    elif(zgjedhja=="KMNEMILES"):
        conv_fac=0.621371
        pergjigjja= format((conv_fac * 2.54),".2f")
    elif(zgjedhja=="MILENEKM"):
        conv_fac=1.60934
        pergjigjja= format((conv_fac * 2.54),".2f")
    else:
        pergjigjja = "Komand jo valide"
    return pergjigjja


#GFC

def GCF(numri1,numri2):
    if numri1%numri2==0:
        return numri2
    return GCF(numri2,numri1%numri2)
   

#METODA SHTESE
#Metoda FAKTORIELI
def FAKTORIELI(n):
    if n==0:
        return 1
    else:
        return n* FAKTORIELI(n-1)

#Metoda CEASAR
def CEASAR(fjalia,opsioni):
    opsioni=opsioni.upper()
    fjalia=fjalia.upper()
    if((opsioni=="ENKRIPTO")):
        tekstiEnkriptuar=""
        for shkronja in fjalia:
            # Metoda isalpha () kthehet e vërtetë(True) nëse të gjithë karakteret janë shkronja alfabeti (a-z).
            if(shkronja.isalpha()):
                #Metoda ord() kthen vlerën e shkronjës që ka në bazë të tabelës ASCII 
                #Metoda chr() kthen numrin në shkronjë duke u bazuar në tabelëen e ASCII
                # Metoda str() kthen tekstin ne string   
                tekstiEnkriptuar+=str(chr(((ord(shkronja)-65+5)%26)+65))
            else:
                tekstiEnkriptuar+=shkronja
        return tekstiEnkriptuar
    elif(opsioni=="DEKRIPTO"):
        tekstiDekriptuar=""
        for shkronja in fjalia:
            if(shkronja.isalpha()):
                tekstiDekriptuar+=str(chr(((ord(shkronja)-65-5)%26)+65))
            else:
                tekstiDekriptuar+=shkronja
        return tekstiDekriptuar

#Metoda FIBONACCI
def FIBONACCI(n):
        if n < 0:
            print("Incorrect input")

        elif n == 0:
            return 0

        elif n == 1 or n == 2:
            return 1
 
        else:
            return FIBONACCI(n-1) + FIBONACCI(n-2)


def Thread(input,adresa):
    try: 
        data=input.decode("utf-8")
    except socket.error:
        print("Të dhënat nuk janë dërguar në server")
       
    print(" ")
    getdata=str(data)
    #rsplit()  kthen një listë të vargjeve pasi thyen vargun e dhënë nga ana e djathtë me ndares te specifikuar.
    ListaEFjaleve=getdata.rsplit(" ")
    ListaEFjaleve[0]=ListaEFjaleve[0].upper()
    rreshti=""
    GjatesiaListes=len(ListaEFjaleve)

    for fjalet in range(1, GjatesiaListes):
        rreshti +=ListaEFjaleve[fjalet]
        if(fjalet!=GjatesiaListes):
            rreshti+=" "
    if not data:
            return

    elif(ListaEFjaleve[0]=="IP"):
        data="IP Adresa e klientit është:" + IP()

    elif(ListaEFjaleve[0]=="NRPORTIT"):
        ListaEFjaleve[0].lower()
        data="Klienti është duke përdorur portin :" + NRPORTIT()

    elif (ListaEFjaleve[0]=="NUMERO"):
        data=str(NUMERO(rreshti))

    elif(ListaEFjaleve[0] == "ANASJELLTAS"):
        data=str(ANASJELLTAS(rreshti))

    elif(ListaEFjaleve[0] == "PALINDROM"):
        data=str(PALINDROM(ListaEFjaleve[1]))   

    elif(ListaEFjaleve[0] == "KOHA"):
        data=KOHA()     

    elif(ListaEFjaleve[0] == "LOJA"):
        data=LOJA()+"pra 5 numra të rastësishëm nga 35"

    elif(ListaEFjaleve[0] == "KONVERTO"):
        try:
            number = float(ListaEFjaleve[2])
        except socket.error:
            data="Gabim në shkrim"
            data="Vlera e fituar është : " + str(KONVERTO(ListaEFjaleve[1], number))

    elif(ListaEFjaleve[0]== "gcf"):
        try:
            rreshti = int(ListaEFjaleve[1])
            rreshti1= int(ListaEFjaleve[2])
            data=str(GCF(rreshti,rreshti1))
        except Exception:
            data = "Shtypni komanden si të tillë GCF Numëri1 Numëri2"
        
    elif (ListaEFjaleve[0]=="FAKTORIELI"):
        try: 
            number=int(ListaEFjaleve[1])
            data="Faktorieli i numrit që keni dhënë është: "+ str(FAKTORIELI(number))
        except Exception:
            data="Duhet te shenoni numrin!"

    elif(ListaEFjaleve[0]=="CEASAR"):
        fjaliaCeasarit=""
        for i in range(2,len(ListaEFjaleve)):
            fjaliaCeasarit+=ListaEFjaleve[i]
            if(fjalet!=i):
                fjaliaCeasarit+=" "        
            if(ListaEFjaleve[1]=="ENKRIPTO"):
                data="Teksti i enkriptuar me algoritmin e Ceasar është: "+CEASAR(fjaliaCeasarit,"ENKRIPTO")
            elif(ListaEFjaleve[1]=="DEKRIPTO"):
                data="Teksti i dekriptuar me algoritmin e Ceasar është: "+CEASAR(fjaliaCeasarit,"DEKRIPTO")
            else:
                data="Keni dhënë kërkesë të gabuar"
        
    elif (ListaEFjaleve[0]=="FIBONACCI"):
        try: 
            number=int(ListaEFjaleve[1])
            data="Fibonacci i numrit që keni dhënë është: "+ str(FIBONACCI(number))
        except Exception:
            data="Duhet te shenoni numrin!"
    else:
        data="Kerkesa nuk ekziston. Provo përsëri!"
    serverS.sendto(data.encode(),adresaa)

while True:
    data, adresaa=serverS.recvfrom(128)
    print(IP() + " ka bere kerkesen -> "+data.decode("utf-8"))
    start_new_thread(Thread,(data,adresaa,))
serverS.close()


