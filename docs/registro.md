# Schema del registro

Non è consulenza legale. Il registro vero sta nel vault o in `dashboard/registro.local.json`, ignorato da git. L'esempio è finto.

`schema` vale `scrubber-registro/2`.

Le categorie di un titolare, in `data/brokers.yaml`, sono `adtech`, `b2b`, `credit`, `lists`, `people-search`, `directory`, `telco`, `registry`, `authority`, `contract`. `contract` è un rapporto in corso: di norma si revoca il marketing, non si chiede la cancellazione del contratto. `uncertain: true` è facoltativo: quelle voci non si contattano da soli. `verified_source` può essere l'oggetto con `page`, `email` e `form`, oppure assente.

| Campo | Obbligatorio | Senso |
| --- | --- | --- |
| `example` | sì | `true` solo nell'esempio del repository |
| `label` | sì | Nell'esempio deve dire che i dati sono finti |
| `requests` | sì | Elenco, anche vuoto |

Ogni scheda:

| Campo | Senso |
| --- | --- |
| `case_id` | `GDPR-` anno `-` progressivo. Nell'oggetto delle email |
| `broker_id` | `id` in `data/brokers.yaml` |
| `broker_name` | Nome da mostrare |
| `channel` | `email`, `form` o `portal` come in `brokers.yaml`. `phone` e `pdf` solo per RPO e operatore |
| `case_type` | `broker`, `operatore`, `sito-terzo`, `rpo`, `motore-ricerca`, `non-gdpr` |
| `related_case_ids` | Schede collegate, per esempio le fonti dichiarate da un titolare |
| `listings` | URL controllati prima e dopo, senza copiare la scheda |
| `identifier_mask` | Maschera, per esempio `+00 *** *** 12`. Mai il dato intero |
| `sent_at` | Data di invio o di submit, `AAAA-MM-GG` |
| `submitted_at` | Uguale a `sent_at` se il canale è un modulo, altrimenti vuoto |
| `deadline` | Un mese di calendario dopo `sent_at` |
| `extended_deadline` | Vuoto, salvo proroga comunicata nel primo mese |
| `status` | Vedi sotto |
| `labels` | Etichette `Scrubber/…` applicate |
| `last_reply_at` | Ultima risposta, o vuoto |
| `next_action` | Azione proposta |
| `next_action_due` | Data entro cui va fatta, o vuoto |
| `next_recheck_at` | Prossimo ricontrollo. Vuoto se `escluso` |
| `cycle_count` | Quanti invii sono partiti per questa scheda |
| `form_url` | URL del modulo, o vuoto |
| `ticket_id` | Riferimento del titolare, o vuoto |
| `proof_path` | Percorso locale della prova, finto nell'esempio |
| `verification_status` | `non-richiesto`, `attesa-otp`, `verificato`, `fallito-sms`, `fallito-captcha`, `fallito-http` |
| `proof` | Elenco di `{kind, ref, at}`. `kind` è `email`, `ticket` o `screenshot` |
| `history` | `{at, event, from, to, note}` |
| `notes` | Nota senza dati della persona |

Stati: `bozza`, `inviata`, `in-attesa`, `risposta-da-leggere`, `richiesta-info`, `verifica-otp`, `blocco-modulo`, `portale-ticket`, `cancellato`, `nessun-dato`, `escluso`, `rifiutato`, `sollecito`, `reclamo`, `chiuso`.

`cancellato`, `nessun-dato` ed `escluso` richiedono almeno una prova. `escluso` significa lista di soppressione: non si ricontrolla. Gli altri due si ricontrollano dopo i giorni in `coverage.recheck_days` (60 per `people-search`, 90 per il resto, se non diversamente configurato).

La dashboard, in prima vista, mostra tre numeri (dati rimossi, in attesa di risposta, interventi tuoi), una barra «quanto sei protetto» e l'elenco delle aziende con un semaforo. Identificativi, date, prove e caricamento del file stanno nella sezione Dettagli.
