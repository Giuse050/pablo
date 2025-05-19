from src.classi import Utente
from src.classi import Gioco

L= Utente("Andrea","fiore",20,"action-rpg","afiore@studenti.apuliadigitalmaker.it","gameba2426")


G1=Gioco("Dark souls remastered","action-rpg","8h","<3","pc","3D")
G2=Gioco("Dark souls 2","action-rpg","8h","<3","pc","3D")
G3=Gioco("Dark souls 3","action-rpg","8h","<3","pc","3D")
G4=Gioco("the forest","survival","8h","<3","pc","3D")
G5=Gioco("hollow knight","metroid-vania","8h","<3","pc","3D")

Ricerca=(G1,G2,G3,G4,G5)
log=False
I=0
pref="no"

while log==False:
    mail = input("Inserisci la tua mail: ")
    password = input("Inserisci la tua password: ")
    if mail==L.email and password==L.password:
        log=True
        print("accesso consentito")
        while I!=4:
            if Ricerca[I].genere==L.genere_preferito:
                print(Ricerca[I].nome)
                print(Ricerca[I].genere)
                print(Ricerca[I].durata)
                print(Ricerca[I].piattaforma)
                print(Ricerca[I].grafica)
                if pref=="no":
                    pref=input("ti interessa(si / no)")
                    if pref=="si": 
                        print("compra su(nome store più economico)")
            I=I+1
            pref="no"
        
    else:
        print("accesso negato")