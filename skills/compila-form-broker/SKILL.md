---
name: compila-form-broker
description: Use when il titolare usa un modulo web, con anteprima, OTP dell'utente e piano se l'SMS non arriva.
---

# Compilare un modulo

Non è consulenza legale. Le regole sono il capitolo 6 di `docs/metodo.md` e `docs/sicurezza.md`. Il modulo è un invio. Il codice OTP non si ripete in chat né nei log.

1. Usa questa skill se `channel` è `form` o `portal`. Leggi `form_notes`, `form_url` se c'è, `known_issues` e la pagina ufficiale (`trova-canale-broker`).
2. Scheda in stato `bozza`, con `case_id`, prima di toccare il modulo. Il modulo non porterà l'id nell'oggetto: ti servirà dopo, insieme al dominio e al ticket.
3. Checklist del minimo. Lascia vuoti data di nascita, documento, selfie, codice fiscale e indirizzo postale. Se uno è obbligatorio, non compilarlo: stato `blocco-modulo` e lettera art. 12 con `richiesta-gdpr-art21-17`, che spiega il rifiuto.
4. Mostra l'anteprima di ogni campo, tendina e casella, e la `form_url`. Di' se manca la voce sull'opposizione art. 21 par. 2. Submit solo dopo un sì esplicito su quell'anteprima.
5. Se compare un OTP, chiedi se arriva via SMS o via email. Stato `verifica-otp` e `verification_status` `attesa-otp`. Il codice lo incolla l'utente. Non ripeterlo. Se non arriva, dopo due tentativi lo stato è `blocco-modulo`, non resta `verifica-otp`.
6. SMS verso un numero italiano, in particolare OneTrust (Samba, id `samba`): al massimo due invii. Se non arriva, `verification_status` `fallito-sms`, stato `blocco-modulo`, lettera di riserva che cita il mancato arrivo. Stesso stop dopo due codici rifiutati dal sito.
7. Captcha o HTTP 400, in particolare SayMine (Kaspr, Cognism): l'utente risolve il captcha nel suo browser. Al massimo due submit. Poi `fallito-captcha` o `fallito-http` e `blocco-modulo`. Non aggirare il captcha.
8. Apollo: se il campo chiede un'email aziendale e l'utente non ne ha una, lascialo vuoto. Non inventare un dominio. Se il submit è impossibile, `blocco-modulo`.
9. Submit riuscito: `submitted_at` e `sent_at` uguali, scadenza da quel momento, `ticket_id` se visibile, `proof_path` sul dispositivo (screenshot della conferma o file della mail), `verification_status` `verificato` o `non-richiesto`. Stato `inviata`, oppure `portale-ticket` se resta solo un portale. Etichette `Scrubber/tipo/modulo` e lo stato. La mail di conferma si aggancia con dominio del mittente più ticket, poi riceve le etichette della scheda.
10. Nel ciclo settimanale, se lo stato è `portale-ticket`, controlla il portale e scrivi in `history` solo l'esito.

Un errore tecnico del sito non è lo stato `rifiutato`. È `blocco-modulo`.
