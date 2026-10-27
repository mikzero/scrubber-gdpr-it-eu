---
name: getting-started
description: Use when l'utente inizia o mancano telefono, email, paese, canale mail, etichetta o cadenza.
---

# Primo avvio

Non è consulenza legale. Prepari il terreno e le bozze. L'utente decide e invia.

Chiedi **una sola cosa per turno**. Aspetta la risposta prima della domanda successiva. Non presentare un modulo unico.

Ordine:

1. Numero da far togliere, con prefisso internazionale. Spiega che servirà per RPO, elenchi e broker che trattano il telefono.
2. Email su cui ricevere le risposte dei titolari. Può essere diversa dall'email che compare nelle schede.
3. Paese di residenza abituale. Se non risponde, proponi Italia e chiedi conferma. Serve per la lingua, il RPO e l'autorità di controllo.
4. Canale con cui leggerai la posta: Gmail oppure AgentMail. Non chiedere password, token o codici.
5. Etichetta o cartella della posta. Proponi `scrubber`. Lì finiscono invii e risposte.
6. Cadenza. Proponi un controllo a settimana finché c'è una scadenza aperta, poi un controllo al mese. Registra la scelta.

Salva le risposte solo nel vault o nella memoria del bot, con chiavi stabili: `scrubber.phone`, `scrubber.email`, `scrubber.country`, `scrubber.mail_channel`, `scrubber.mail_label`, `scrubber.cadence`. Non scriverle nel repository, in una issue, in un commit, in un log o in un file di esempio.

Quando ripeti un dato in chat, l'utente lo conosce già. Non copiarlo in un file del repo. Se l'utente incolla dati veri in un file del repo, fermati e digli di toglierli prima di qualsiasi commit.

Non inviare nulla in questo passo. Quando i sei punti ci sono, riassumi le scelte senza scaricare il numero in chiaro in un allegato e proponi il passo successivo:

- Paese Italia: skill `rpo-ed-elenchi-it`, poi i broker con `phone_relevance` alta.
- Altro paese: salta il RPO italiano, individua l'autorità in `data/registries.yaml` e parti dai broker.

Plugin raccomandato dal manifest: Gmail o AgentMail. Se il canale scelto non è collegato, spiega come collegarlo e non inventare un invio.
