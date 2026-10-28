# Registro Pubblico delle Opposizioni e elenchi

Non è consulenza legale. La descrizione segue le pagine pubbliche del servizio. Se divergono da questo file, conta il sito.

## Cosa fa il RPO

Il Registro Pubblico delle Opposizioni è un servizio pubblico italiano. L'interessato iscrive uno o più numeri, fissi o mobili, per opporsi al loro uso per telefonate promozionali e ricerche di mercato. Può anche opporsi all'uso, per posta cartacea, dell'indirizzo già presente negli elenchi. Chi fa telemarketing deve consultare il registro.

L'iscrizione non è la stessa cosa della cancellazione di una scheda da PagineBianche o da un altro elenco. Quella passa dal proprio operatore telefonico, con revoca del consenso alla pubblicazione.

## Come ci si iscrive

L'utente agisce dal proprio numero. Il bot non invia l'iscrizione e non chiede credenziali SPID o CIE.

- Web, anche con SPID o CIE, oppure senza autenticazione se il modulo lo consente. Il sito poi chiede una chiamata di verifica dal numero da iscrivere.
- Telefono: si chiama, dal numero da iscrivere, il numero per utenze fisse o quello per i cellulari pubblicato sulla pagina cittadino. Quei numeri non sono copiati in questo repository, così non diventano obsoleti qui e non si confondono con dati personali.
- Email: modulo PDF ufficiale, salvato senza cambiarne il formato, inviato alla casella istituzionale indicata in `data/registries.yaml`. Segue una chiamata di verifica, nei tempi scritti nelle istruzioni che arrivano via email.

Le URL stanno in `data/registries.yaml`, voce `rpo-it`.

## Dopo

Conservare nel vault, non in git, l'eventuale codice registro. Serve per rinnovo, revoca selettiva e cancellazione dell'iscrizione, dalle stesse tre modalità.

Poi revocare l'elenco presso l'operatore, con il modello `templates/letters/it/revoca-consensi-operatore.md`, solo dopo un sì esplicito sulla bozza.
