
```mermaid

flowchart TD
    A["Inizio: Utente accede a Syncgames"] --> B["Registrazione con email o social login"]
    B --> C["Compilazione questionario preferenze"]
    C --> D{"Collegare account esterni?"}
    D -- Sì --> E["Importazione libreria giochi"]
    D -- No --> G["Generazione scheda profilo"]
    E --> G
    G --> H["Profilo salvato e modificabile"]
    H --> I["Accesso funzione cerca gioco"]
    I --> J["Inserimento filtri contestuali"]
    J --> K["Analisi profilo, contesto e database giochi"]
    K --> L["Classifica giochi personalizzata"]
    L --> M["Visualizza dettagli del gioco"]
    M --> N{"Aggiungere alla wishlist?"}
    N -- Sì --> O["Aggiunto alla wishlist"]
    N -- No --> P{"Acquistare il gioco?"}
    O --> R["Aggiorna algoritmo"]
    P -- Sì --> S["Clic su Trova al miglior prezzo"]
    P -- No --> R
    S --> T["Recupero prezzi da store esterni"]
    T --> U["Visualizza offerte ordinate per prezzo"]
    U --> V["Seleziona store"]
    V --> W["Reindirizzamento a sito esterno"]
    W --> X{"Sincronizzare con libreria?"}
    X -- Sì --> Y["Aggiorna libreria utente"]
    X -- No --> FINE["Fine"]
    Y --> FINE
    R --> L
    style FINE color:#D50000
 ---
config:
  layout: dagre
---
flowchart TD
    A["Utente
    ___
    -età
    -nome
    -cognome
    -genere_preferito
-email
-password"] <--> B["Gioco
__
-genere
-durata
-preferito
-piattaforma
-grafica"] 