---
name: richiesta-gdpr-art21-17
description: Use when prepari una richiesta art. 21 par. 2, art. 17, art. 19 e art. 15 verso un titolare.
---

# Richiesta art. 21 par. 2, art. 17, art. 19 e art. 15

Non è consulenza legale. Prepari una bozza. L'utente la legge e decide.

Usa il modello `templates/letters/it/art21-17-19-15.md` se il paese nel vault è Italia o se l'utente non sceglie un'altra lingua. Per l'inglese usa `templates/letters/en/art21-17-19-15.md`. Per tedesco, francese e spagnolo i file in `de/`, `fr/` e `es/` sono traduzioni di comunità da rivedere: dillo prima di usarle.

Diritti da chiedere insieme, con questi nomi, senza parentesi dopo il numero dell'articolo:

- art. 21 par. 2: opposizione al marketing diretto, compresa la profilazione connessa. Il titolare deve cessare quel trattamento.
- art. 17: cancellazione. Richiamala insieme all'opposizione (art. 17 par. 1 lett. c) e, se non c'è altra base, perché i dati non servono più o il trattamento è illecito.
- art. 19: il titolare comunica la cancellazione a chi ha ricevuto i dati, salvo impossibilità o sforzo sproporzionato, e ti dice chi sono quei destinatari se l'utente lo chiede.
- art. 15 par. 1 lett. c e lett. g: destinatari o categorie di destinatari, e la fonte se i dati non arrivano dall'interessato.

Nell'oggetto scrivi `art. 21 par. 2`. Non mettere il numero del paragrafo tra parentesi: in passato la parentesi è sparita e l'oggetto è diventato illeggibile. Stessa cautela per gli altri articoli: `art. 15 par. 1 lett. c`, non una sigla con parentesi.

Dati minimi, presi dal vault, solo quelli che servono a far trovare la scheda:

- nome, se l'utente accetta di indicarlo
- telefono, se il broker ha `phone` fra gli `identifier_required` o `phone_relevance` alta
- email, se serve a cercare o a ricevere risposta
- paese
- per North Data e casi analoghi, l'URL del profilo, non un URL costruito da te

Non aggiungere data di nascita, documento, codice fiscale o indirizzo postale. Se il titolare li chiede dopo, passa a `leggi-risposte-e-classifica`. L'art. 12 par. 6 consente dati ulteriori solo quando ci sono dubbi ragionevoli sull'identità. L'art. 5 par. 1 lett. c chiede il minimo. La decisione di inviare un documento è dell'utente, in un turno successivo, su una bozza nuova.

Una lista di soppressione stretta (il solo identificativo, per non riacquisire il dato) è compatibile con la cancellazione. Chiedi che non venga usata per altro.

Termine: art. 12, senza ritardo ingiustificato e comunque entro un mese dal ricevimento. Il titolare può prorogare di due mesi solo se è necessario e se avvisa entro il primo mese, con i motivi. Non allungare tu la scadenza. Nel registro la scadenza è lo stesso giorno del mese successivo, oppure l'ultimo giorno di quel mese se il giorno non esiste.

Prima di qualsiasi invio mostra oggetto, destinatario, corpo e allegati. Il destinatario è solo la casella o il modulo appena riverificati con `trova-canale-broker`. Invia solo dopo un sì esplicito in questo turno. Se l'utente cambia una virgola, mostra di nuovo la bozza e chiedi un altro sì.

Dopo l'invio registra lo stato `inviata`, la data, il canale e la scadenza. Vedi `registro-e-dashboard`. Non mettere il testo compilato nel repo.
