---
name: scrubber-registro-e-dashboard
description: Use when aggiorni il registro locale, il diario delle skill o il JSON della dashboard.
---

# Registro e dashboard

Non è consulenza legale. Il registro segue `docs/metodo.md` e lo schema `docs/registro.md` (`scrubber-registro/2`). Non è un invio. Se occorre scrivere, passa alla skill della lettera o del modulo e chiedi un sì esplicito sulla bozza.

Tieni il JSON nel vault o in `dashboard/registro.local.json`, ignorato da git. Non sovrascrivere `dashboard/example-registro.json` con dati veri.

Per ogni scheda: `case_id`, broker, `channel`, `identifier_mask`, `sent_at`, `deadline`, `extended_deadline`, `status`, `labels`, `last_reply_at`, `next_action`, `next_action_due`, `next_recheck_at`, `cycle_count`, `proof`, `history`. Per un modulo anche `form_url`, `submitted_at`, `ticket_id`, `proof_path`, `verification_status`. `identifier_mask` non è il dato intero. `cancellato`, `nessun-dato` ed `escluso` richiedono una prova. `escluso` non ha ricontrollo. Gli intervalli 60 e 90 giorni sono in `coverage.recheck_days`. `proof_path` resta sul dispositivo.

Stati ammessi: `bozza`, `inviata`, `in-attesa`, `risposta-da-leggere`, `richiesta-info`, `verifica-otp`, `blocco-modulo`, `portale-ticket`, `cancellato`, `nessun-dato`, `escluso`, `rifiutato`, `sollecito`, `reclamo`, `chiuso`. Una transizione è ammessa solo se è nella tabella di `docs/metodo.md`.

La dashboard (`dashboard/index.html`) è per una persona non tecnica: tre numeri, la barra «quanto sei protetto», il riquadro «Cosa devi fare tu» e un semaforo per azienda. La scheda Skill elenca origine, versione, ultimo cambiamento e avvisi, leggendo `skill_log`. Niente numeri di articolo in prima vista. Identificativi, cronologia, prove, date di ricontrollo e il caricamento del JSON stanno in Dettagli. Si apre sull'esempio finto. Nessun backend e nessuna chiamata esterna.

Il diario delle skill segue `docs/registro-skill.md`. Sta in `skill_log` nello stesso JSON, oppure in `skill-log.json` nello store del bot. Non sta nel repository e non contiene dati della persona. Non sovrascrivere l'esempio con un diario vero.

Alla fine del ciclo settimanale, o mensile se non ci sono scadenze, scrivi il report del capitolo 7 di `docs/metodo.md`. Prima del ciclo esegui `scrubber-sync-dal-repo`. Nel report non ripetere il numero di telefono.
