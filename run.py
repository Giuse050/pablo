from src.classi import Utente
from src.classi import Gioco
from src.classi import Store
from pdb import set_trace

L= Utente("Andrea","fiore",20,"action-rpg","afiore@studenti.apuliadigitalmaker.it","gameba2426")


G1=Gioco("Dark souls Remastered","action-rpg","8h","pc","3D")
G2=Gioco("Dark souls 2","action-rpg","8h","pc","3D")
G3=Gioco("Dark souls 3","action-rpg","8h","pc","3D")
G4=Gioco("the forest","survival","8h","pc","3D")
G5=Gioco("hollow knight","metroid-vania","8h","pc","3D")

S1_1=Store("Epic","Dark souls Remastered",20)
S1_2=Store("Epic","Dark souls 2",10)
S1_3=Store("Epic","Dark souls 3",20)
S1_4=Store("Epic","the forest",10)
S1_5=Store("Epic","hollow knight",20)

S2_1=Store("Steam","Dark souls Remastered",10)
S2_2=Store("Steam","Dark souls 2",20)
S2_3=Store("Steam","Dark souls 3",10)
S2_4=Store("Steam","the forest",10)
S2_5=Store("Steam","hollow knight",10)

Rprezzi=(S1_1,S1_2,S1_3,S1_4,S1_5,S2_1,S2_2,S2_3,S2_4,S2_5)
Ricerca=(G1,G2,G3,G4,G5)
log=False
IR=0
IRP=0
IP=0
Pmin=100
pref="no"

while log==False:
    mail = input("Inserisci la tua mail: ")
    password = input("Inserisci la tua password: ")
    if mail==L.email and password==L.password:
        log=True
        print("accesso consentito")
        while IR!=4:
            if Ricerca[IR].genere==L.genere_preferito:
                print(Ricerca[IR].nome)
                print(Ricerca[IR].genere)
                print(Ricerca[IR].durata)
                print(Ricerca[IR].piattaforma)
                print(Ricerca[IR].grafica)
                pref=input("ti interessa(si / no)")
                if pref=="si":
                    
                    while IRP!=9:
                        if Ricerca[IR].nome==Rprezzi[IRP].nomeGioco:
                            if Pmin>Rprezzi[IRP].prezzo:
                                
                                Pmin=Rprezzi[IRP].prezzo
                                IP=IRP
                        IRP=IRP+1
                    print("compra su", Rprezzi[IP].nomeStore, "a",Rprezzi[IP].prezzo,Rprezzi[IP].nomeGioco )
                    IP=0
                    Pmin=100
            IR=IR+1
    else:
        print("accesso negato")