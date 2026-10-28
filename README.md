# Scrubber GDPR IT-EU

Non è consulenza legale. This is not legal advice.

Pacchetto di istruzioni per un assistente Grok Bot che aiuta una persona, in Unione europea e in primo luogo in Italia, a togliere il proprio numero di telefono e altri dati da data broker, elenchi telefonici e liste di marketing, usando i diritti del Regolamento (UE) 2016/679.

Il bot legge questo repository e aggiorna le proprie skill da qui. Il repository resta generico: non contiene dati di una persona.

## Italiano

### Cosa fa

- Prepara l'iscrizione al Registro Pubblico delle Opposizioni e la revoca dell'elenco presso il proprio operatore. L'iscrizione la fa l'utente, dal proprio numero.
- Trova il canale ufficiale di un titolare (modulo o casella di ruolo già vista sulla pagina privacy) e prepara richieste di opposizione al marketing diretto (art. 21 par. 2), cancellazione (art. 17), comunicazione ai destinatari (art. 19) e accesso a destinatari e fonti (art. 15 par. 1 lett. c e lett. g).
- Tiene un registro locale delle richieste, con scadenza a un mese, e una dashboard statica.
- Per l'adtech, affianca l'opt-out sul dispositivo: molti di questi titolari non hanno il telefono, hanno un identificativo pubblicitario.

### Cosa non fa

- Non è un parere legale e non sostituisce un avvocato o l'autorità di controllo.
- Non invia nulla senza una bozza mostrata all'utente e un sì esplicito.
- Non aggira captcha, non indovina OTP, non chiede password SPID o della posta.
- Non promette la cancellazione dei dati di credito conservati per legge. L'opposizione al marketing e la cancellazione del fascicolo di credito non sono la stessa cosa.
- Nell'oggetto delle lettere si scrive `art. 21 par. 2`, mai con il paragrafo tra parentesi.

### Dati personali

Vietati in tutto il repository: numeri, email di persone, nomi, indirizzi, documenti, screenshot di schede. Si usano i placeholder `{{NOME}}`, `{{TELEFONO}}`, `{{EMAIL}}`, `{{PAESE}}`.

Le sole email ammesse sono caselle di ruolo o istituzionali dichiarate in `data/*.yaml`, copiate da una pagina ufficiale. I numeri di telefono del RPO stanno sul sito del Registro, non qui.

Il bot conserva telefono, email e registro nel vault, non in git. Vedi `docs/privacy-del-bot.md`.

### Come il bot si aggiorna

`bot_access` è `read-only`. Il bot fa solo GET pubblici su `raw.githubusercontent.com` (o su una release dello stesso repository), senza token. Non fa push, non apre issue, pull request, commenti o fork, e non scrive il registro nel repository.

All'inizio di ogni ciclo, e ogni settimana, confronta `VERSION`. Se è più nuova, applica da solo dati, paesi e modelli. Le skill si chiamano `scrubber-…`. La prima installazione può arrivare da `main` dopo un merge del proprietario; gli aggiornamenti successivi solo da un tag `v` firmato, e solo se passano `scripts/security_lint.py`. Una skill aggiunta o modificata dall'utente non si blocca: il bot avvisa in italiano e la segna come personale. Non sovrascrive in silenzio una modifica dell'utente, né una skill omonima che non è di questo pacchetto. Il sì prima di ogni messaggio in uscita resta. Dettaglio: `scrubber-sync-dal-repo`, `docs/sicurezza.md` e `docs/registro-skill.md`.

Il metodo operativo è `docs/metodo.md`. La direzione del prodotto è `ROADMAP.md`: prima l'Italia, poi Europa, poi il resto del mondo, senza invii in massa e senza esiti finali senza prova.

### Routine e posta

Un controllo a settimana finché c'è una scadenza aperta, poi un controllo al mese. Canale raccomandato: Gmail o AgentMail. Skill di partenza: `scrubber-getting-started`.

### Struttura

| Percorso | Contenuto |
| --- | --- |
| `skills/` | Istruzioni per il bot, una cartella `SKILL.md` ciascuna |
| `templates/letters/` | Modelli it e en; de, fr, es da rivedere |
| `data/brokers.yaml` | Titolari, URL, canale, eventuali caselle di ruolo |
| `data/registries.yaml` | RPO, elenchi, modulo Google, opt-out, autorità |
| `dashboard/` | HTML statico e registro di esempio finto |
| `docs/` | Metodo, sicurezza, registro, diario delle skill, RPO, casi difficili |
| `data/countries/` | Copertura per paese: `todo`, `partial` o `done` |
| `ROADMAP.md` | Fasi Italia, Europa, resto del mondo |
| `scripts/` | Validazione, controllo link, lint di sicurezza |

### Contribuire

Vedi `CONTRIBUTING.md`. Le issue e le pull request hanno un template. Non allegare dati propri come prova.

### Licenze

- Codice (`scripts/`, `dashboard/`, workflow): MIT, file `LICENSE`.
- Testi e modelli (skill, lettere, docs, prosa): CC-BY-4.0, file `LICENSE-CONTENT`.

### Versione

`VERSION` è la versione semver del pacchetto. La corrente è 0.3.3. Il changelog è `CHANGELOG.md`.

## English

Instructions for a Grok Bot assistant that helps one person in the EU, Italy first, remove their phone number and other personal data from data brokers, phone directories and marketing lists by using GDPR rights.

The bot periodically reads this repository and updates its skills from it. The repository stays generic. It holds no one's personal data.

The bot drafts requests. The user reviews every draft and sends it. A draft is never sent without an explicit yes. Subjects use `art. 21 par. 2`, not a parenthesis after the article number.

Personal data belong in the bot's vault, never in git. The only email addresses in this repo are role or institutional mailboxes declared in `data/*.yaml` after they were read on an official page. The dashboard in `dashboard/` is a static file with a clearly fake example register. Load a real register from your own device; it is gitignored.

The bot's access is read-only public HTTPS. It never uses a GitHub token and never pushes, opens issues or pull requests, comments, or forks. On each check, and weekly, it auto-updates data, country files and templates from the official repo. Skill folders use the `scrubber-` prefix because the library is shared by every bot. The first install may read skills from `main` after an owner merge. Later skill updates come only from a signed version tag, and only when the security lint passes. Skills the user adds or edits stay allowed: the bot warns in Italian and records the event. It never silently overwrites a user edit or a same-named skill that is not its own. The yes before every outgoing message stays mandatory. See `docs/sicurezza.md` and `docs/registro-skill.md`.

Recommended routine: weekly while a deadline or a recheck is open, then monthly. Recommended mail plugin: Gmail or AgentMail. Start with the `scrubber-getting-started` skill.

Contributions: `CONTRIBUTING.md`. Code is MIT. Prose and templates are CC-BY-4.0.

Not legal advice.
