from src.classi import Utente
from src.classi import Gioco

L= Utente("Andrea","fiore",20,"Adventure","afiore@studenti.apuliadigitalmaker.it","gameba2426")
print (L.nome)
print (L.cognome)
print (L.età)
print (L.genere_preferito)
print (L.email)
print (L.password)

G=Gioco("game","action","8h","<3","pc","3D")
print (G.nome)
print (G.genere)
print (G.durata)
print (G.preferito)
print (G.piattaforma)
print (G.grafica)