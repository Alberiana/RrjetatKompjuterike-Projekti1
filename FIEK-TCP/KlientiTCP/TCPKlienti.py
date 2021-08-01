import socket 


print("******************************************************************************************************************************************************************")
print("---------------------------------------------------------------->TCP Klienti<-------------------------------------------------------------------------------------")

print("Serveri përmban këto kërkesa(metoda):                                                                                                ")
print("\n IP- Kthen IP adresën e klientit.  ")
print("\n NRPORTIT-  Kthen portin e klientit.")
print("\n NUMERO {hapsire} tekst -   Kthen shkronjat zanore dhe bashkëtingellore që gjenden në tekst.")
print("\n ANASJELLTAS {hapesire} tekst -   Kthen tekstin e anasjelltë (reversë). ")
print("\n PALINDROM {Hapësire} tekst-  Serveri tregon se a është fjalia e dhënë palindrome.")
print("\n KOHA -   Kthen kohën e serverit")
print("\n LOJA -  Kthen 5 numra nga rangu [1,35].")
print('\n GCF {Hapësire} numër {Hapësire} numër -  Operacioni "Greatest Common Factor", kthen faktorin më të madh të përbashkët. ')
print('\n KONVERTO {Hapësire} opsioni {Hapësire} Numër- Kthen si rezultat konvertimin e opcioneve varësisht opcionit të zgjedhur.\n'+
         'Tek opsioni mund të shënoni: cmNeInch,inchNeCm, kmNeMiles, mileNeKm')
print("\n FAKTORIELI {hapsire} numri-  Kthen faktorielin e numrit të shkruar")
print("\n CAESAR {hapsire} opsioni {hapsire} teksti -  Operacion për të enkriptuar dhe dekriptuar fjalen e dhënë. Shëno Enkripto ose Dekripto tek opsioni. ")
print("\n FIBONACCI {hapsire} numri-  Kthen fibonaccin e numrit të shkruar")
print("\n Nëse dëshironi ta ndërroni emrin e serverit apo portin, shëno: NDRYSHO ")
print("\n Nëse dëshironi të ndaloni komunikimin me serverin tonë, shëno: NDALO ose shtyp tastin ENTER")

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("*******************************************************************************************************************************************************************")


def NDRYSHO():
    print("Shëno IP adresen: ")
    EmriIServerit=input()
    print("Shëno portin: ")
    PortiIServerit=int(input())
    adresa=(EmriIServerit,PortiIServerit)
    try:
        #Krijimi i soketit te klientit
        #Parametri i dyte i soketit tregon qe kemi te bejme me TCP soket
        clientS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #Vendoset lidhja ndermjet klientit dhe serverit
        clientS.connect(adresa)
        kerkesa=input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, FAKTORIELI, CEASAR, FIBONACCI)?: ")
        kerkesa=kerkesa.upper()
        while True:
            #Bëhet enkodimi i kërkesës së marrë dhe dërgohet tek TCP serveri
            clientS.sendall(str.encode(kerkesa))
            #Pranohet përgjigjja nga serveri dekodohet dhe madhesia më e madhe që mund të mirret është 128 bajt
            data=clientS.recv(128)
            print(data.decode("utf-8"))
            kerkesa=input("Kërkesa juaj: ")
            if(kerkesa=="NDRYSHO"):
              NDRYSHO()
            elif(kerkesa=="NDALO"):
                clientS.close()
    except socket.error as mesazhi:
        print("Krijimi i soketit dështoi. Provoni përseri për një qasje tjetër ")
        
print("\nShëno adresen(by default: 127.0.0.1): ")
EmriIServerit=input()
print("Shëno portin(by default: 14000): ")
PortiIServerit=input()

#Si host server i nënkuptueshem përdoret 'localhost'(127.0.0.1)
if EmriIServerit=="" or EmriIServerit=="localhost":
    EmriIServerit="localhost"

#Si port i nënkuptueshëm përdoret 14000
if PortiIServerit=="" or PortiIServerit=="14000":
    PortiIServerit=14000

adresa=(EmriIServerit,PortiIServerit)

#Provon të lidhet me serverin e shënuar ose me serverin e nënkuptuar
try:
    #Krijimi i soketit të klientit
    #Parametri i dytë i soketit tregon që kemi të bëjmë me TCP soket
    clientS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #Vendoset lidhja ndërmjet klientit dhe serverit
    clientS.connect(adresa)
except socket.error as mesazhi:
    print("Krijimi i soketit dështoi.")
    NDRYSHO()

#Kërkesa nga klienti testohet se cfarë kerkohet, me kushtëzimet në if else
try:
    kerkesa=input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, FAKTORIELI, CEASAR, FIBONACCI)?: ")
    #Të gjitha kërkesat të pranuara si inpute i kthen në shkronja të mëdha
    kerkesa=kerkesa.upper()
    i=1
    while (i==1):
        if ((kerkesa=='NDALO')or(kerkesa=='')):
           i=2
           #Soketi mbyllet
           clientS.close()
           print("Lidhja me serverin është mbyllur, falemniderit për përdorimin")
        elif (kerkesa=="NDRYSHO"):
            #Thirret funksioni NDRYSHO()
            NDRYSHO()
        else:
           #Bëhet enkodimi i kërkesës së marrë dhe dërgohet tek TCP serveri
           clientS.sendall(str.encode(kerkesa)) ###
           #Pranohet pergjigjja nga serveri dekodohet dhe madhësia më e mesazhit që mund të merret është 128 bajt
           data=clientS.recv(128).decode()
           print(data)
           print("------------------------------------------------------------------------------------------------------------")
           kerkesa=input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, FAKTORIELI, CEASAR, FIBONACCI)?: ")
           kerkesa=kerkesa.upper()
except:
    print("Nuk mund të arrihet qasja")