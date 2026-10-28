# Privacy del bot

Non è consulenza legale. Questo file dice come il bot tratta i dati di chi lo usa, non come un'azienda deve scrivere la propria informativa.

## Dove stanno i dati

Telefono, email, paese, canale di posta, etichetta, cadenza, codici registro e registro delle richieste stanno nel vault o nella memoria del bot. Il diario delle skill sta nello stesso posto, dentro il registro (`skill_log`) o in `skill-log.json`. Non stanno in questo repository. Il file di esempio della dashboard è finto e va lasciato finto.

Una pull request, una issue o un commit non sono un posto dove incollare una scheda, una risposta o un OTP.

## Posta

Il canale raccomandato è Gmail o AgentMail, a scelta dell'utente. Il bot non chiede la password. Legge i messaggi nell'etichetta concordata per classificarli. Il testo di una risposta è un dato: non è un ordine. Vedi la skill `scrubber-leggi-risposte-e-classifica`.

## Cosa non fa il bot

- Non iscrive da solo al RPO e non chiede SPID o CIE.
- Non invia una bozza senza un sì esplicito in quel turno.
- Non aggira captcha e non indovina OTP.
- Non copia documenti di identità nel repo.
- Non sovrascrive una skill personale, né una skill con lo stesso nome che non è di questo pacchetto. Lo registra e lo dice.

## Aggiornamenti

Il bot legge `VERSION` e `manifest.json` dal raw di GitHub. La prima installazione delle skill può usare `main` dopo un merge del proprietario. Poi le skill ufficiali cambiano solo con un tag firmato, e solo se i controlli passano. Il sì prima di ogni messaggio in uscita non dipende da quell'aggiornamento. Una skill dell'utente resta personale: gli avvisi si mostrano e si registrano, e non c'è un blocco silenzioso. Il vault non si sostituisce. Se una skill ufficiale toglie l'obbligo della bozza o chiede di pubblicare dati personali, il bot non la applica e registra il motivo.

## Dashboard

`dashboard/index.html` gira nel browser, anche offline. Non ha backend, non carica font o script esterni e non invia il registro da nessuna parte. Il registro vero si sceglie nei Dettagli, con un file locale, e resta sul dispositivo. La scheda Skill elenca origine, versione, ultimo cambiamento e avvisi, leggendo il diario. I dati di prova sono finti.

## Contributi

Chi propone un broker non allega la propria scheda come prova. Basta la URL ufficiale e la descrizione del canale.
