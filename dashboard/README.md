# Dashboard

Non è consulenza legale. Apri `index.html` nel browser, anche senza connessione. L'esempio finto è dentro la pagina.

In prima vista ci sono tre numeri, la barra «quanto sei protetto» e l'elenco di cosa fare. Il semaforo sulle aziende è verde se il dato risulta rimosso o escluso con una prova, giallo se si aspetta una risposta, rosso se il termine è passato o c'è un rifiuto, grigio se tocca ricontrollare. La scheda Skill elenca le istruzioni del bot: ufficiali o personali, con versione, ultimo cambiamento e avvisi. I dati di quella scheda sono finti nell'esempio.

Identificativo della pratica, date, prove e il pulsante per caricare un registro vero stanno sotto «Dettagli». Il file vero, per esempio `registro.local.json`, resta sul dispositivo ed è ignorato da git. Non committare dati veri.

Lo schema delle richieste è `docs/registro.md`. Il diario delle skill è `docs/registro-skill.md`. La pagina non chiama servizi esterni e non include tracker.
