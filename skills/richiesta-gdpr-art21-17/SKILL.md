---
name: richiesta-gdpr-art21-17
description: Use when prepari una richiesta art. 21 par. 2, art. 17, art. 19 e art. 15 verso un titolare.
---

# Richiesta art. 21 par. 2, art. 17, art. 19 e art. 15

Non è consulenza legale. Segui `docs/metodo.md`. Se `channel` in `data/brokers.yaml` è `form` o `portal`, non mandare l'email come primo passo: passa a `compila-form-broker`. Questa skill è il canale `email`, e anche la lettera di riserva quando il modulo è in `blocco-modulo`.

Non inviare a tutti i titolari lo stesso pacchetto di dati. Per questo titolare manda solo l'identificativo che gli serve. Apri o riusa la scheda caso prima di scrivere. L'oggetto inizia con `{{CASE_ID}}` e contiene `art. 21 par. 2`, senza parentesi dopo il numero dell'articolo. Il modello è `templates/letters/it/art21-17-19-15.md` se il paese è Italia o se l'utente non sceglie un'altra lingua. Inglese: `templates/letters/en/`. Tedesco, francese e spagnolo sono traduzioni di comunità: dillo prima.

Diritti da chiedere insieme: art. 21 par. 2, art. 17, art. 19, art. 15 par. 1 lett. c e lett. g. Dati solo il minimo del capitolo 1 del metodo. Se la lettera è di riserva dopo un modulo, aggiungi una frase sul perché il modulo non è stato completato (codice SMS non arrivato, HTTP 400, oppure campo vietato obbligatorio). Non aggiungere il dato che hai rifiutato di compilare.

Termine art. 12: un mese da `sent_at`, salvo `extended_deadline` già compilata secondo il metodo. Non allungarla tu.

Mostra oggetto, destinatario, corpo e allegati. Il destinatario è la casella appena riverificata. Invia solo dopo un sì esplicito. Poi stato `inviata`, etichetta `Scrubber/inviata` più `Scrubber/tipo/richiesta`, `sent_at`, `deadline`, `history`. Non salvare la bozza compilata nel repo.
