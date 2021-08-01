import socket
import sys
from _thread import *
import random


print("******************************************************************************************************")
print("--------------------------------------> TCP Serveri<--------------------------------------------------")
print("******************************************************************************************************")

#IP adresa  IPv4
EmriIServerit = '127.0.0.1'
#Porti i serveri 
PortiIServerit= 14000

adresa=(EmriIServerit,PortiIServerit)
#Krijimi i soketit te serverit sipas TCP protokollit
#socket.AF_INET pranon vetëm IP versioni 4
#socket.SOCK_STREAM mesazhet që i dergojmë shkojnë si të dhëna të kthyera në bajta 
serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serverS.bind(adresa)
except socket.error:
    print("Lidhja me klient nuk mund të arrihet!")
    sys.exit()   #importojm librarin për sys

print('Serveri është startuar në localhost në portin:  ' + str(PortiIServerit))
#Serveri mund të pranoj 10 kërkesa
serverS.listen(10)
print('Server është duke punuar dhe është duke pritur për ndonjë kërkesë!')

#Metoda IP
def IP():
    pergjigjja = str(addressaa[0])
    return pergjigjja

#Metoda NRPORTIT
def NRPORTIT():
    pergjigjja =str(addressaa[1])
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
    if(zgjedhja=="CMNEINCH"):
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

#Metoda GFC
def GCF(numri1,numri2):
    if numri1%numri2==0:
        return numri2
    return GCF(numri2,numri1%numri2)


#METODAT  SHTESE

#Metoda FAKTORIELI
def FAKTORIELI(n):
    if n==0:
        return 1
    else:
        return n* FAKTORIELI(n-1)

#Metoda CEASAR
def CAESAR(fjalia,opsioni):
    opsioni=opsioni.upper()
    fjalia=fjalia.upper()
    if((opsioni=="ENKRIPTO")):
        tekstiEnkriptuar=""
        for shkronja in fjalia:
            #Funksioni isalpha () kthehet e vërtetë(True) nëse të gjithë karakteret janë shkronja alfabeti (a-z).
            if(shkronja.isalpha()):
                #Funksioni ord() kthen vlerën e shkronjës që ka në bazë të tabelës ASCII 
                #Funksioni chr() kthen numrin në shkronjë duke u bazuar në tabelëen e ASCII
                #Funksioni str() kthen numrat në string   
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
            print("Numri duhet të jetë pozitiv")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return FIBONACCI(n-1) + FIBONACCI(n-2)


def Thread(connection):
    while True:
        try: 
            #Kërkesa e klientit merret dhe dekodohet
            #Kërkesa e pranuar mund të jetë më së shumti 128 bajt 
            data=connection.recv(128).decode()
        except socket.error:
            print("Klienti me IP "+ adresa[0]+" u shkyq nga serveri!")
            break

        print(" ")
        #Të dhënat nga klienti kthehen në string
        getdata=str(data)

        #rsplit() kthen një listë të vargjeve pasi thyen vargun e dhënë nga ana e djathtë me ndarës të specifikuar.
        ListaEFjaleve=getdata.rsplit(" ")
        ListaEFjaleve[0]=ListaEFjaleve[0].upper()
        rreshti=""
        GjatesiaListes=len(ListaEFjaleve)

        #Merret secila fjal pas kërkesës së shkruar
        for fjalet in range(1, GjatesiaListes):
            rreshti +=ListaEFjaleve[fjalet]
            if(fjalet!=GjatesiaListes):
                rreshti+=" "

        #Nëse nuk ka të dhëna ndalon
        if not data:
            break
        #Nëse ka të dhëna hyrëse(nëse është shkruar kërkesa) do të vizitoj secilen loop deri sa të gjendet kërkesa e shënuar
        elif(ListaEFjaleve[0]=="IP"):
            data="IP Adresa e klientit është: " + IP()

        elif(ListaEFjaleve[0]=="NRPORTIT"):
            data="Klienti është duke përdorur portin: " + NRPORTIT()

        elif (ListaEFjaleve[0]=="NUMERO"):
                data=str(NUMERO(ListaEFjaleve[1]))
                
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
                data="Vlera e fituar është : " + str(KONVERTO(ListaEFjaleve[1], number))
            except Exception:
                data="Gabim jepni njëhere opsionin pastaj numrin"

        elif(ListaEFjaleve[0]== "GCF"):
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
                data="Duhet të shënoni numrin!"

        elif(ListaEFjaleve[0]=="CAESAR"):
            fjaliaCaesarit=""
            for i in range(2,len(ListaEFjaleve)):
                fjaliaCaesarit+=ListaEFjaleve[i]
                if(fjalet!=i):
                    fjaliaCaesarit+=" "        
            if(ListaEFjaleve[1]=="ENKRIPTO"):
                data="Teksti i enkriptuar me algoritmin e Ceasar është: "+CAESAR(fjaliaCaesarit,"ENKRIPTO")
            elif(ListaEFjaleve[1]=="DEKRIPTO"):
                data="Teksti i dekriptuar me algoritmin e Ceasar është: "+CAESAR(fjaliaCaesarit,"DEKRIPTO")
            else:
                data="Keni dhënë kërkesë të gabuar"
        
        elif (ListaEFjaleve[0]=="FIBONACCI"):
            try: 
                number=int(ListaEFjaleve[1])
                data="Fibonacci i numrit që keni dhënë është: "+ str(FIBONACCI(number))
            except Exception:
                data="Duhet te shënoni numrin!"
        else:
            data="Kërkesa nuk ekziston. Provo përsëri!"

        connection.send(data.encode())#Dërgohet përgjigjja nga serveri tek klienti
    connection.close() #Mbyllet lidhja

while True:
    connection, addressaa=serverS.accept()
    print(f"Serveri është lidhur me klientin në IP adresë %s në portin %s"% addressaa)
    #Metoda start_new_thread mundëson në menyrë të shpejtë dhe efikase lidhjen me një klient tjeter(me disa klient) 
    start_new_thread(Thread,(connection,))
serverS.close()
