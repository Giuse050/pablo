## Creazione del profilo:

**Attori principali**: *utente*, *sistema Syncgames*

**Obiettivo**: permettere all’utente di creare un profilo personalizzato, che rifletta le sue preferenze di gioco.

#### Flusso principale:

1. L’utente si registra tramite email/social login.
2. Il sistema chiede di compilare un questionario/intervista (es: generi preferiti, piattaforme possedute, tempo medio di gioco, interesse per multiplayer/singleplayer).
3. L’utente può aggiungere manualmente i giochi già giocati o collegare account esterni (es: Steam, Xbox, PlayStation) per importare la propria libreria.
4. Il sistema genera una scheda profilo con:

    * Preferenze esplicite
    * Cronologia giochi
    * Abitudini di gioco
    * Obiettivi (es: giochi veloci, esperienze immersive, party games).

5. L’utente può modificare o aggiornare il profilo in qualsiasi momento.

## Riuscire a trovare il gioco tramite l’algoritmo:

**Attori principali**: utente, sistema Syncgames, algoritmo di matchmaking giochi

**Obiettivo**: suggerire all’utente uno o più giochi adatti sulla base del profilo e del contesto.

**Flusso principale**: 
1. L’utente accede alla funzionalità di ricerca.
2. Il sistema chiede eventuali filtri contestuali (es: “sto cercando un gioco per 2 persone, sessioni brevi, stasera”).
3. L’algoritmo analizza:
    * Dati del profilo utente
    * Preferenze contestuali
    * Database dei giochi (recensioni, caratteristiche, durata, modalità).

4. Viene generata una classifica personalizzata di giochi, con una percentuale di compatibilità.
5. L’utente può esplorare i dettagli di ciascun gioco, leggere recensioni, vedere video.
6. L’utente può salvare giochi nella wishlist o scartarli (migliorando l’algoritmo con feedback implicito).

## Acquistare il gioco al miglior prezzo

**Attori principali**: utente, sistema Syncgames, siti di store esterni Obiettivo: permettere di acquistare il gioco scelto al prezzo più conveniente.

**Obiettivo**: riusicire a trovare tra gli store partner il prezzo migliore per il titolo desiderato

**Flusso principale**:

1. Dopo aver selezionato un gioco, l’utente clicca su “Trova al miglior prezzo”.
2. Il sistema effettua uno scraping o usa API di siti esterni (Steam, Epic, Instant 0.Gaming, Amazon, ecc.) per recuperare i prezzi aggiornati.
3. Viene mostrata una lista di offerte ordinate per prezzo, con indicazione di:

    * Negozio
    * Prezzo totale (eventuali tasse/commissioni incluse)
    * Valutazione dello store (se disponibile)
    * Link diretto all’acquisto.

4. L’utente seleziona lo store e viene reindirizzato al sito esterno per completare l’acquisto.
5. (Opzionale) Syncgames registra l’acquisto per aggiornare la libreria dell’utente.