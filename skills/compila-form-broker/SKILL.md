---
name: compila-form-broker
description: Use when il titolare usa un modulo web, con anteprima, OTP dell'utente e piano se l'SMS non arriva.
---

# Compilare un modulo

Non è consulenza legale. Il modulo è un invio. Trattalo come una lettera.

1. Parti dal canale trovato con `trova-canale-broker`. Leggi `known_issues` di quel `id`.
2. Compila solo i campi necessari. Stessi limiti di `richiesta-gdpr-art21-17`: niente documento, data di nascita o indirizzo postale se l'utente non ha detto sì su quella richiesta precisa.
3. Prima del submit mostra l'anteprima di ogni campo, compreso menu a tendina e caselle spuntate. Di' quale diritto stai chiedendo. Se il modulo non ha una voce per l'opposizione al marketing, dillo e prepara in parallelo la lettera art. 21 par. 2.
4. Invia il modulo solo dopo un sì esplicito in questo turno. Non riusare un sì vecchio se hai cambiato un campo.
5. L'OTP, il captcha e il link di verifica li legge e li esegue l'utente. Chiedi il codice a lui. Non indovinarlo, non leggerlo da un canale che non ti ha indicato, non aggirare il captcha e non creare account paralleli per saltare il controllo.
6. Se l'OTP è un SMS e non arriva, in particolare verso numeri italiani su moduli OneTrust (caso noto: Samba, id `samba`), non riprovare molte volte. Passa al piano di riserva, in quest'ordine: OTP via email se il modulo lo offre; lettera alla casella di ruolo se è ancora sulla pagina ufficiale; avviso nel registro che il modulo è bloccato. Vedi `docs/casi-difficili.md`.
7. Kaspr (`kaspr`) e gli altri moduli SayMine, fra cui Cognism: se la pagina risponde con errore HTTP 400 o mostra un captcha, fermati. L'utente completa il captcha nel suo browser. Se non c'è la voce art. 21 par. 2, usa la lettera e avvisa che in passato le email a Kaspr sono state rifiutate.
8. Apollo (`apollo`): il modulo chiede un'email aziendale. Non inventare un dominio e non trasformare l'email personale in una email di lavoro. Se l'utente non ha un'email aziendale da usare, dillo e cerca un altro canale sulla stessa pagina ufficiale.
9. Acxiom: se il modulo chiede l'indirizzo postale, fermati e applica la minimizzazione. LexisNexis: stessa regola per data di nascita e documento.
10. North Data: incolla solo l'URL del profilo che l'utente ti ha dato.
11. Dopo l'invio, o dopo uno stop, aggiorna il registro. Un modulo rifiutato dal sito non è uno stato `rifiutato` del titolare: è un blocco tecnico. Scrivilo nelle note, con stato `in attesa`, senza dati personali nelle note se il registro può uscire dal dispositivo.

Non è un successo il messaggio generico «richiesta ricevuta» se non indica i diritti trattati. Conserva la conferma che l'utente vede e chiedigli di inoltrarla all'etichetta `scrubber`.
