---
name: scrubber-rpo-ed-elenchi-it
description: Use when l'utente in Italia deve iscriversi al RPO o revocare l'elenco telefonico presso l'operatore.
---

# RPO e elenchi telefonici

Non è consulenza legale. Il Registro Pubblico delle Opposizioni e la revoca dell'elenco sono due cose diverse. Fanno entrambe, se l'utente è in Italia e vuole fermare il telemarketing e la pubblicazione del numero.

Il RPO, dal 2022, copre fissi e cellulari, anche se non sono in elenco, e le chiamate automatiche. L'iscrizione annulla i consensi al telemarketing dati prima. Non annulla i consensi dati dopo, né i contratti continuativi di telefono, luce e gas. Non copre SMS, email, chat, né i call center abusivi o esteri. Non cancella da solo la scheda sull'elenco.

La rimozione vera dagli elenchi è nel database unico (DBU), tramite il proprio operatore. PagineBianche, 89.24.24, 1254 e Infobel leggono quel database. Sul modulo chiedi tre no: no all'elenco, no alla consultazione (servizi di informazione abbonati), no alla posta pubblicitaria. Proponi prima l'area clienti o l'app, dove l'identità è già verificata. Il modulo cartaceo con documento è il passo successivo, non il primo. Le caselle a cui si spedisce il modulo non sono il DPO.

Canale per operatore, da `data/brokers.yaml`: Iliad e Fastweb in area clienti; Vodafone dal sito; TIM, Kena e CoopVoce per email; WINDTRE e Very per PEC; ho. per posta. Una voce `uncertain` non si contatta: dilla come da verificare.

Ordine per il telefono, una scheda alla volta: RPO; l'operatore dell'utente; Italiaonline (PagineBianche, 89.24.24 e TuttoCittà in una richiesta); Infobel; Truecaller; tellows; MiChiama; GhostCallers; Getcontact; Digital Metrics; Concorsi Web; Ediscom; Foryou; Realmaps se le chiamate sono di agenzie immobiliari; Hiya. Poi, se verificati, MXT e Consodata. Il portale ANCIC è una sola richiesta verso una trentina di società di informazione commerciale. L'AGCOM, delibera 106/25/CONS, blocca lo spoofing: non è una cancellazione.

Dettaglio e lacune: `docs/italia.md`.

Leggi `data/registries.yaml`, voce `rpo-it`, e la pagina cittadino indicata. I numeri di telefono del servizio stanno su quella pagina e non in questo repo. Non ricopiarli in un file, in una issue o in un commit. Se la pagina e questo repo divergono, conta la pagina ufficiale e proponi una correzione senza dati personali.

L'utente compie l'iscrizione. Tu non la invii, non ti autentichi e non chiedi password SPID, PIN della CIE o codici dell'operatore.

Tre strade, da spiegare in breve. L'utente ne sceglie una.

- Web: pagina di iscrizione del RPO. SPID, CIE oppure il percorso senza autenticazione, come offre il sito. Poi il sito mostra un numero da chiamare dal telefono da iscrivere, per provare che la linea è sua. La chiamata può essere abbattuta senza risposta: è il meccanismo pubblicato, non un errore.
- Telefono: l'utente chiama **dal numero da iscrivere** il numero per fissi o quello per cellulari pubblicato sulla pagina cittadino. In chiaro, non anonimo.
- PDF: modulo ufficiale collegato in `registries.yaml`. Va compilato e salvato senza cambiare formato, poi inviato alla casella istituzionale indicata lì. Entro il tempo scritto nelle istruzioni che arrivano via email, l'utente chiama dal proprio numero il numero di verifica che gli comunicano.

Fino a cinque numeri per richiesta, secondo le istruzioni correnti del RPO. Non inventare un sesto. Conserva nel vault, non nel repo, l'eventuale codice registro che l'utente ti detta: serve a rinnovare o revocare.

Dopo l'iscrizione, occupati dell'elenco. Chiedi il nome dell'operatore, una domanda sola. Prepara la bozza con `templates/letters/it/revoca-consensi-operatore.md`. Mostra destinatario, oggetto e testo. Invia solo dopo un sì esplicito in questo turno. Un sì dato per un'altra bozza non vale.

Nel registro locale segna `rpo-it` e l'operatore come passi a parte, con la data e l'esito che l'utente riferisce (`inviata`, `in attesa`, `risposta`). Non salvare il numero in chiaro nel file se quel file può finire nel repo. Il registro vero resta fuori da git. Vedi `scrubber-registro-e-dashboard`.

Se l'utente non è in Italia, non spingerlo sul RPO. Cerca nell'elenco autorità il paese del vault e dillo.
