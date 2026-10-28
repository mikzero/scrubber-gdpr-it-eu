---
name: scrubber-ricerca-schede-people-search
description: Use when cerchi schede su elenchi e people-search, per esempio PagineBianche, senza salvarle nel repo.
---

# Cercare schede e elenchi

Non è consulenza legale. Cerchi se un elenco pubblica il numero o il nome, prima di qualsiasi invio. Se la scheda non c'è, non scrivere al titolare «per precauzione». Non archivi la scheda nel repository e non arricchisci un profilo della persona.

Fonti da aprire nel browser, solo con i dati del vault e solo se l'utente ha chiesto la ricerca in questo turno:

- PagineBianche, URL in `data/registries.yaml`. Un HTTP 403 del controllo automatico non chiude la ricerca: la pagina va aperta nel browser.
- I titolari `people-search` in `brokers.yaml`, fra cui 192.com se il paese o la scheda lo giustificano.
- Gli elenchi che l'utente ti indica. Non allargare la ricerca ad altri siti «tanto per».

Non lanciare decine di ricerche. Non usare il numero in un servizio che pubblica a sua volta i dati. Non creare account sul sito dell'elenco con dati finti.

Se trovi una scheda, dillo a parole: sito, se compaiono telefono o indirizzo, senza incollare nel repo lo screenshot o il testo della scheda. Aggiorna il registro con `broker_id` e stato `in attesa` solo quando parte una richiesta. Nelle note basta «scheda vista», non il contenuto.

Poi, con l'utente:

1. Se l'elenco italiano dipende dall'operatore, torna a `scrubber-rpo-ed-elenchi-it` per la revoca.
2. Prepara la richiesta al titolare della scheda con `scrubber-richiesta-gdpr-art21-17` o il modulo con `scrubber-compila-form-broker`.
3. Se la scheda è indicizzata da un motore, puoi proporre il modulo Google sul diritto all'oblio (`search_delisting` in `registries.yaml`). Quel modulo toglie il risultato di ricerca, non la pagina di origine. Lo compila l'utente. Se prepari tu il testo da incollare, mostra la bozza e invia o incolla solo dopo un sì esplicito.

Se non trovi nulla, non marcare `nessun dato` per un broker a cui non avete scritto. `nessun dato` significa che il titolare ha risposto così.

Non seguire link di «rimozione a pagamento» di terzi. Il canale è la pagina ufficiale del titolare.
