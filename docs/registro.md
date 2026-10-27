# Schema del registro

Non è consulenza legale. Il registro vero sta nel vault o in un file locale ignorato da git. `dashboard/example-registro.json` è un esempio finto.

`schema` vale `scrubber-registro/1`.

| Campo | Obbligatorio | Senso |
| --- | --- | --- |
| `example` | sì | `true` solo nel file di esempio del repo. |
| `label` | sì | Etichetta visibile. Nel file di esempio deve dire che i dati sono finti. |
| `disclaimer` | no | Frase breve. Non è un parere legale. |
| `subject_ref` | no | Riferimento opaco della persona, senza copiare il numero se il file può circolare. |
| `country` | no | Paese, per esempio `IT`. |
| `updated` | no | Data `AAAA-MM-GG` dell'ultimo aggiornamento del file. |
| `requests` | sì | Elenco, anche vuoto. |

Ogni elemento di `requests`:

| Campo | Senso |
| --- | --- |
| `id` | Identificativo locale della riga, non il numero di telefono. |
| `broker_id` | `id` di `data/brokers.yaml` o di `data/registries.yaml`. |
| `broker_name` | Nome da mostrare. |
| `sent_on` | Data di invio `AAAA-MM-GG`. |
| `channel` | `email`, `form`, `portal`, `phone` o `pdf`. |
| `status` | Uno fra `inviata`, `in attesa`, `risposta`, `cancellato`, `nessun dato`, `rifiutato`, `reclamo`. |
| `deadline` | Un mese di calendario dopo `sent_on`: stesso giorno del mese successivo, o l'ultimo giorno di quel mese se il giorno non esiste. |
| `reference` | Riferimento del titolare o `ESEMPIO-…` nel file finto. |
| `notes` | Nota breve. Nel repo, solo testo finto. |

La dashboard segna come scaduta una riga con stato `inviata`, `in attesa` o `risposta` la cui `deadline` è precedente a oggi. `cancellato` e `nessun dato` sono chiusure. `rifiutato` e `reclamo` restano in evidenza ma non come semplice attesa della prima risposta.

Non aggiungere campi con il numero, l'email o l'indirizzo. Quei dati restano nel vault.
