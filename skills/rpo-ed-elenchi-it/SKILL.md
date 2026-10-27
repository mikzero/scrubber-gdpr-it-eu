---
name: rpo-ed-elenchi-it
description: Use when l'utente in Italia deve iscriversi al RPO o revocare l'elenco telefonico presso l'operatore.
---

# RPO e elenchi telefonici

Non è consulenza legale. Il Registro Pubblico delle Opposizioni e la revoca dell'elenco sono due cose diverse. Fanno entrambe, se l'utente è in Italia e vuole fermare il telemarketing e la pubblicazione del numero.

Il RPO serve a opporsi all'uso del numero per chiamate promozionali e, se l'utente lo chiede, all'uso dell'indirizzo già presente negli elenchi per la posta cartacea. Gli operatori di telemarketing devono consultarlo. Non cancella da solo la scheda sull'elenco telefonico.

La revoca presso il proprio operatore toglie il consenso all'inserimento del numero negli elenchi pubblici. Senza questo passo la scheda può restare su PagineBianche e sugli altri elenchi.

Leggi `data/registries.yaml`, voce `rpo-it`, e la pagina cittadino indicata. I numeri di telefono del servizio stanno su quella pagina e non in questo repo. Non ricopiarli in un file, in una issue o in un commit. Se la pagina e questo repo divergono, conta la pagina ufficiale e proponi una correzione senza dati personali.

L'utente compie l'iscrizione. Tu non la invii, non ti autentichi e non chiedi password SPID, PIN della CIE o codici dell'operatore.

Tre strade, da spiegare in breve. L'utente ne sceglie una.

- Web: pagina di iscrizione del RPO. SPID, CIE oppure il percorso senza autenticazione, come offre il sito. Poi il sito mostra un numero da chiamare dal telefono da iscrivere, per provare che la linea è sua. La chiamata può essere abbattuta senza risposta: è il meccanismo pubblicato, non un errore.
- Telefono: l'utente chiama **dal numero da iscrivere** il numero per fissi o quello per cellulari pubblicato sulla pagina cittadino. In chiaro, non anonimo.
- PDF: modulo ufficiale collegato in `registries.yaml`. Va compilato e salvato senza cambiare formato, poi inviato alla casella istituzionale indicata lì. Entro il tempo scritto nelle istruzioni che arrivano via email, l'utente chiama dal proprio numero il numero di verifica che gli comunicano.

Fino a cinque numeri per richiesta, secondo le istruzioni correnti del RPO. Non inventare un sesto. Conserva nel vault, non nel repo, l'eventuale codice registro che l'utente ti detta: serve a rinnovare o revocare.

Dopo l'iscrizione, occupati dell'elenco. Chiedi il nome dell'operatore, una domanda sola. Prepara la bozza con `templates/letters/it/revoca-consensi-operatore.md`. Mostra destinatario, oggetto e testo. Invia solo dopo un sì esplicito in questo turno. Un sì dato per un'altra bozza non vale.

Nel registro locale segna `rpo-it` e l'operatore come passi a parte, con la data e l'esito che l'utente riferisce (`inviata`, `in attesa`, `risposta`). Non salvare il numero in chiaro nel file se quel file può finire nel repo. Il registro vero resta fuori da git. Vedi `registro-e-dashboard`.

Se l'utente non è in Italia, non spingerlo sul RPO. Cerca nell'elenco autorità il paese del vault e dillo.
