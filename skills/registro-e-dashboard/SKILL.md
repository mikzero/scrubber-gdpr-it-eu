---
name: registro-e-dashboard
description: Use when aggiorni il registro locale delle richieste o esporti il JSON per la dashboard.
---

# Registro e dashboard

Non è consulenza legale. Il registro è la memoria delle pratiche. Non è un invio: non spedire nulla da questa skill. Se l'utente chiede di scrivere a un titolare, passa alla skill della lettera o del modulo e chiedi un sì esplicito sulla bozza.

Tieni il registro nel vault o in un file locale fuori dal repository, per esempio `dashboard/registro.local.json`, che è ignorato da git. Il file `dashboard/example-registro.json` è finto: non sovrascriverlo con dati veri e non copiare dati veri dentro il repo.

Schema: `docs/registro.md`. Stati ammessi, solo questi: `inviata`, `in attesa`, `risposta`, `cancellato`, `nessun dato`, `rifiutato`, `reclamo`.

Per ogni richiesta registra: id locale, `broker_id` come in `brokers.yaml`, nome, data di invio `sent_on`, canale, stato, `deadline`, riferimento libero senza dati non necessari, note brevi. La scadenza è un mese di calendario dopo l'invio. Non anticiparla e non spostarla se il titolare tace.

Quando mostri lo stato all'utente, evidenzia le righe la cui scadenza è prima di oggi e il cui stato è `inviata`, `in attesa` o `risposta`. Per quelle, proponi `solleciti-e-reclamo-garante`. Le righe `cancellato` e `nessun dato` non sono in ritardo. `rifiutato` e `reclamo` vanno richiamate, non nascoste.

Per vedere la dashboard, l'utente apre `dashboard/index.html` nel browser. Il file di esempio si carica da solo ed è marcato come finto. Per i dati veri usa «Carica registro JSON» e sceglie il file locale. La dashboard non ha backend e non chiama siti esterni. Non mettere il registro vero in una issue o in una pull request per «far vedere» la schermata: fai uno screenshot solo se il registro a schermo è l'esempio.

Cadenza da `getting-started`: un controllo a settimana finché esiste una scadenza non chiusa, poi un controllo al mese. A ogni controllo esegui anche `sync-dal-repo`.

Se esporti un riepilogo in chat, preferisci id del broker, stato e date. Evita di ripetere il numero di telefono se non serve a distinguere due pratiche.
