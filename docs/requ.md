REQUISITI FUNZIONALI 

1️. Creazione Profilo Utente

-Registrazione e accesso

--L’utente può registrarsi usando email/password o account social (Google, Facebook, Steam).

--È possibile effettuare il login su più dispositivi.

-Inserimento preferenze videoludiche

L’utente compila un questionario su: generi preferiti, piattaforme possedute, modalità di gioco preferite (singleplayer, multiplayer).

-Collegamento account esterni:

Possibilità di sincronizzare la propria libreria giochi da account Steam, Xbox, PlayStation per popolare automaticamente i giochi già giocati.

-Modifica e aggiornamento profilo:

L’utente può aggiornare preferenze, aggiungere/rimuovere piattaforme e generi in qualsiasi momento.

2️.  Ricerca e Suggerimento Giochi

-Definizione filtri di ricerca:1

L’utente può specificare contesto e parametri: es. “cercami un gioco per 3 persone, durata max 1 ora, su PC”.

-Algoritmo di matchmaking:

Il sistema combina le informazioni del profilo con il contesto per calcolare una classifica di giochi consigliati.

-Visualizzazione classifica giochi:

Ogni gioco suggerito mostra: nome, copertina, descrizione breve, percentuale di compatibilità, recensioni.

-Gestione lista preferiti:

L’utente può aggiungere giochi ai preferiti o escluderli per non ricevere più suggerimenti simili.

-Feedback sul consiglio:

L’utente può votare i consigli ricevuti per migliorare l’accuratezza dell’algoritmo nel tempo.


3️. Comparazione e Acquisto

-Ricerca automatica prezzi:

Il sistema interroga store partner (es. Steam, Epic, Amazon, Instant Gaming) per recuperare i prezzi aggiornati.

-Visualizzazione offerte:

Le offerte vengono ordinate per prezzo, con indicazione di: nome store, eventuali tasse/spese incluse, valutazione dello store.

-Reindirizzamento acquisto:

Cliccando su un’offerta, l’utente viene portato sul sito esterno per completare l’acquisto.

-Notifiche calo prezzo:

SyncGames invia notifiche via email/app se un gioco nella wishlist scende sotto un prezzo soglia impostato dall’utente.





REQUISITI NON FUNZIONALI 

1️. Prestazioni

--Il sistema deve rispondere alle richieste di ricerca in ≤ 2 secondi per garantire un’esperienza fluida.

--L’aggiornamento dei prezzi avviene ogni 12 ore per garantire dati affidabili senza sovraccaricare le API esterne.


2️. Affidabilità

--SyncGames deve garantire un uptime del 99% su base mensile.

--In caso di crash del sistema, i dati utente (profilo, preferenze, giochi salvati) devono essere recuperabili senza perdita.

--Salvataggio automatico di ogni modifica alle preferenze utente o ai giochi salvati.



3️. Usabilità

--Interfaccia user-friendly, accessibile sia da mobile che desktop, con design responsive.

--Inclusione di un tutorial guidato alla prima registrazione per spiegare il funzionamento di SyncGames.


--Iconografia chiara e linguaggio semplice per utenti non esperti di tecnologia.


4️.  Compatibilità

--Compatibilità con i principali browser aggiornati: Chrome, Firefox, Edge, Safari.

--Supporto a risoluzioni da 720p a 4K, con adattamento automatico della UI.

--L’app mobile (se prevista) compatibile con Android (≥ 8.0) e iOS (≥ 13).


5️. Sicurezza

--Utilizzo di protocolli sicuri HTTPS per tutte le comunicazioni tra client e server.

--Crittografia dei dati sensibili (email, password) e uso di OAuth 2.0 per l’autenticazione tramite social.

--Gestione dei dati utente in conformità con il GDPR, con possibilità per l’utente di cancellare definitivamente il proprio account e i relativi dati.