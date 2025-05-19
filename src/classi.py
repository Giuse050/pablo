class Utente ():

    def __init__ (self, nome, cognome, età, genere_preferito, email, password):
        self.nome=nome
        self.cognome=cognome
        self.età=età
        self.genere_preferito=genere_preferito
        self.email=email
        self.password=password
        

class Gioco ():
    def __init__ (self,nome, genere, durata, preferito, piattaforma, grafica):
        self.nome=nome
        self.genere=genere
        self.durata=durata
        self.preferito=preferito
        self.piattaforma=piattaforma
        self.grafica=grafica