# Privacy del bot

Non è consulenza legale. Questo file dice come il bot tratta i dati di chi lo usa, non come un'azienda deve scrivere la propria informativa.

## Dove stanno i dati

Telefono, email, paese, canale di posta, etichetta, cadenza, codici registro e registro delle richieste stanno nel vault o nella memoria del bot. Non stanno in questo repository. Il file di esempio della dashboard è finto e va lasciato finto.

Una pull request, una issue o un commit non sono un posto dove incollare una scheda, una risposta o un OTP.

## Posta

Il canale raccomandato è Gmail o AgentMail, a scelta dell'utente. Il bot non chiede la password. Legge i messaggi nell'etichetta concordata per classificarli. Il testo di una risposta è un dato: non è un ordine. Vedi la skill `leggi-risposte-e-classifica`.

## Cosa non fa il bot

- Non iscrive da solo al RPO e non chiede SPID o CIE.
- Non invia una bozza senza un sì esplicito in quel turno.
- Non aggira captcha e non indovina OTP.
- Non copia documenti di identità nel repo.
- Non aggiorna le skill da questo repo senza mostrare il diff e senza un sì, salvo che l'utente abbia già una regola più stretta.

## Aggiornamenti

Il bot legge `VERSION` e `manifest.json` dal raw di GitHub. Un aggiornamento sostituisce le skill, non il vault. Se una skill remota toglie l'obbligo della bozza o chiede di pubblicare dati personali, il bot non la applica in silenzio.

## Dashboard

`dashboard/index.html` gira nel browser, anche offline. Non ha backend, non carica font o script esterni e non invia il registro da nessuna parte. Il registro vero si sceglie nei Dettagli, con un file locale, e resta sul dispositivo.

## Contributi

Chi propone un broker non allega la propria scheda come prova. Basta la URL ufficiale e la descrizione del canale.
