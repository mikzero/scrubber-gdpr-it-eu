---
name: getting-started
description: Use when l'utente inizia o mancano telefono, email, paese, canale mail, etichette o cadenza.
---

# Primo avvio

Non è consulenza legale. Il ciclo è `docs/metodo.md`. I limiti sui dati sono `docs/sicurezza.md`, skill `sicurezza-e-minimizzazione`. Il repository è in sola lettura.

Chiedi una sola cosa per turno e di' perché serve. Non inviare nulla. Non chiedere data di nascita, documento, codice fiscale, IBAN, indirizzo, salute o famiglia.

Ordine:

1. Nome da usare nelle bozze, solo se l'utente lo accetta. Serve a firmare la lettera. Se rifiuta, le schede useranno solo l'identificativo. Chiave `scrubber.display_name`.
2. Numero con prefisso internazionale. Serve alle schede dei titolari che trattano il telefono, non a tutti. Chiave `scrubber.phone`.
3. Email su cui ricevere le risposte dei titolari. Non è detto che vada anche nel testo di ogni richiesta. Chiave `scrubber.email`.
4. Paese di residenza abituale. Serve a scegliere autorità, lingua e registri. Proponi Italia e aspetta conferma. Chiave `scrubber.country`.
5. Canale posta: Gmail o AgentMail. Serve a leggere le risposte. Non chiedere password o token. Chiave `scrubber.mail_channel`.
6. Cadenza: un controllo a settimana finché c'è una scadenza o un ricontrollo aperto, poi uno al mese. Chiave `scrubber.cadence`.
7. Email di lavoro, solo se l'utente ne ha una e vuole usarla con i broker di contatti aziendali. Non inventarne una. Chiave `scrubber.work_email`. Si può saltare.
8. Identificativo pubblicitario, solo se l'utente vuole includere l'adtech a bassa rilevanza. Si può saltare. Chiave `scrubber.ad_id`.

Prima di creare qualcosa, controlla se esistono già una routine, un registro o le etichette `Scrubber`. Se ci sono, proponi di migrarle. Poi deve restare una sola routine, con id fisso `scrubber-main`, e un solo file di registro scritto da un solo bot. La parola `STOP` ferma subito ogni invio in coda.

`scrubber.retention_days` resta 30 se l'utente non dice altro. Il comando `cancella tutto` è in `docs/sicurezza.md`.

Poi crea, se mancano, l'etichetta padre `Scrubber`, le etichette di stato e quelle di tipo elencate in `docs/metodo.md`. Su AgentMail sono tag con gli stessi nomi. Azzera `scrubber.case_seq` solo se non esiste: non rimettere a zero un progressivo già usato.

Salva tutto nel vault. Non scrivere questi valori nel repository. Se l'utente li incolla in un file del repo, fermati e faglieli togliere.

Quando i punti ci sono, riassumi le scelte senza allegare il numero e proponi il passo successivo:

- Italia: `rpo-ed-elenchi-it` e l'ordine delle prime 15 voci in `docs/italia.md`. Salta le voci `uncertain` e quelle con `phone_flow: skip-unless-ties`, salvo un legame detto dall'utente.
- Altro paese: autorità in `data/registries.yaml`, poi i broker.

Ogni titolare avrà una scheda caso con id `GDPR-` anno `-` progressivo, creata al momento della prima richiesta, non ora. Il minimo da mettere in quella richiesta è nel capitolo 1 di `docs/metodo.md`.
