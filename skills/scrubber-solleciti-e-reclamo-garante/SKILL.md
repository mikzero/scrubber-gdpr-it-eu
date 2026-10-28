---
name: scrubber-solleciti-e-reclamo-garante
description: Use when il mese dell'art. 12 è scaduto, la risposta non basta, o serve un reclamo all'autorità.
---

# Sollecito e reclamo

Non è consulenza legale. I tempi sono in `docs/metodo.md`. Prima il sollecito al titolare. Il reclamo viene dopo, se l'utente lo vuole.

Proponi il sollecito il giorno della scadenza effettiva (`extended_deadline` se c'è, altrimenti `deadline`) se lo stato è `inviata`, `in-attesa` o `portale-ticket`. `next_action` è `sollecito` e `next_action_due` è quella data più 7 giorni di grazia. Non inviare nel giorno stesso del primo invio. Dopo la grazia, se l'utente non ha ancora detto sì, il sollecito resta nel report fra le azioni in attesa.

Usa `templates/letters/it/sollecito-art12.md` o la lingua del primo invio. L'oggetto inizia con `{{CASE_ID}}`. Non spostare `deadline`. Mostra la bozza. Invia solo dopo un sì esplicito. Poi stato `sollecito`, etichetta `Scrubber/sollecito` e `Scrubber/tipo/sollecito`, e `next_action_due` a 14 giorni da questo invio.

Proponi il reclamo se quei 14 giorni passano senza una risposta nel merito, oppure se lo stato è `rifiutato` e il rifiuto non indica una base. Non aprire il reclamo da solo. Autorità del paese nel vault, elenco in `data/registries.yaml`. Per l'Italia, il Garante: modalità e indirizzo si leggono sulla pagina reclami, la PEC istituzionale è nel file e accetta solo PEC. Avvisa che la firma autografa, secondo quella pagina, chiede la copia di un documento. Il documento non entra nel repo.

Bozza `templates/letters/it/reclamo-garante.md` con il `case_id`, il titolare, l'URL, le date e l'esito. Sì esplicito, poi stato `reclamo` e etichetta `Scrubber/reclamo`.

In Germania il reclamo verso un'azienda di solito va all'autorità del Land. L'EDPB non riceve reclami contro aziende. L'EDPS non è l'autorità di un broker.
