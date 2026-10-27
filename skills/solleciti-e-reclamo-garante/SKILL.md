---
name: solleciti-e-reclamo-garante
description: Use when il mese dell'art. 12 è scaduto, la risposta non basta, o serve un reclamo all'autorità.
---

# Sollecito e reclamo

Non è consulenza legale. Prima il sollecito al titolare. Il reclamo all'autorità viene dopo, se l'utente lo vuole.

Sollecito quando la scadenza nel registro è passata e lo stato è ancora `inviata` o `in attesa`, oppure lo stato è `risposta` o `rifiutato` e la risposta non tratta i diritti chiesti. Non sollecitare il giorno stesso dell'invio.

Usa `templates/letters/it/sollecito-art12.md` (o la lingua del primo invio). Richiama la data dell'invio, i diritti, l'art. 12 e il fatto che il mese è passato. Chiedi una risposta. Non insultare e non minacciare azioni che l'utente non ha deciso. Puoi scrivere che si riserva il reclamo all'autorità di controllo.

Mostra oggetto, destinatario e testo. Invia solo dopo un sì esplicito. Poi aggiorna la nota del registro, senza spostare la scadenza originale: la data da cui contare il ritardo resta quella del primo invio.

Reclamo se, dopo il sollecito, il silenzio o il rifiuto resta, e l'utente chiede di andare all'autorità. Non aprire il reclamo di tua iniziativa.

Scegli l'autorità del paese nel vault (`scrubber.country`), che è lo Stato della residenza abituale, oppure un'altra se l'utente lavora lì o lì è avvenuto il fatto. L'elenco è `data/registries.yaml`, chiave `authorities`. Se `complaint_url_verified` è false, apri il sito e cerca la pagina reclami corrente. Non inventare un modulo.

Per l'Italia l'autorità è il Garante. La pagina reclami in `registries.yaml` descrive PEC, raccomandata o consegna a mano. La PEC istituzionale è nel file: accetta solo messaggi provenienti da PEC. L'indirizzo postale si legge sulla pagina, non da questo repo. Il Garante chiede un reclamo firmato. Con firma autografa la pagina pubblica chiede anche la copia di un documento. Spiegalo e lascia scegliere all'utente. Firma digitale o firma autenticata seguono le istruzioni della stessa pagina. Non conservare il documento nel repo.

Prepara `templates/letters/it/reclamo-garante.md` con i fatti già nel registro: titolare, URL, data della richiesta, assenza di risposta o rifiuto, diritti invocati. Niente dati in più. Mostra la bozza completa, destinatario compreso. Invia solo dopo un sì esplicito. Segna lo stato `reclamo`.

In Germania il reclamo verso un'azienda di solito va all'autorità del Land, non al BfDI. La URL in elenco porta all'indice dei Länder. In Spagna, se la sede elettronica non si apre, parti dalla home dell'AEPD.

L'EDPB non riceve reclami contro aziende. L'EDPS serve per le istituzioni UE, non per un broker.
