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

1. Legge `VERSION` da `https://raw.githubusercontent.com/mikzero/scrubber-gdpr-it-eu/main/VERSION`.
2. Se è diversa da `scrubber.pack_version`, legge `manifest.json` e `CHANGELOG.md`.
3. Mostra il diff delle skill e chiede conferma prima di sovrascrivere.
4. Non tocca il vault. Se una skill remota toglie l'obbligo della bozza, non la applica in silenzio.

Dettaglio operativo: skill `sync-dal-repo`.

### Routine e posta

Un controllo a settimana finché c'è una scadenza aperta, poi un controllo al mese. Canale raccomandato: Gmail o AgentMail. Skill di partenza: `getting-started`.

### Struttura

| Percorso | Contenuto |
| --- | --- |
| `skills/` | Istruzioni per il bot, una cartella `SKILL.md` ciascuna |
| `templates/letters/` | Modelli it e en; de, fr, es da rivedere |
| `data/brokers.yaml` | Titolari, URL, canale, eventuali caselle di ruolo |
| `data/registries.yaml` | RPO, elenchi, modulo Google, opt-out, autorità |
| `dashboard/` | HTML statico e registro di esempio finto |
| `docs/` | RPO, casi difficili, privacy del bot, schema del registro |
| `scripts/` | Validazione e controllo link |

### Contribuire

Vedi `CONTRIBUTING.md`. Le issue e le pull request hanno un template. Non allegare dati propri come prova.

### Licenze

- Codice (`scripts/`, `dashboard/`, workflow): MIT, file `LICENSE`.
- Testi e modelli (skill, lettere, docs, prosa): CC-BY-4.0, file `LICENSE-CONTENT`.

### Versione

`VERSION` è la versione semver del pacchetto. Parte da 0.1.0. Il changelog è `CHANGELOG.md`.

## English

Instructions for a Grok Bot assistant that helps one person in the EU, Italy first, remove their phone number and other personal data from data brokers, phone directories and marketing lists by using GDPR rights.

The bot periodically reads this repository and updates its skills from it. The repository stays generic. It holds no one's personal data.

The bot drafts requests. The user reviews every draft and sends it. A draft is never sent without an explicit yes. Subjects use `art. 21 par. 2`, not a parenthesis after the article number.

Personal data belong in the bot's vault, never in git. The only email addresses in this repo are role or institutional mailboxes declared in `data/*.yaml` after they were read on an official page. The dashboard in `dashboard/` is a static file with a clearly fake example register. Load a real register from your own device; it is gitignored.

Sync: compare `VERSION` on GitHub raw with the version stored in the vault, then read `manifest.json`, show the diff, and ask before overwriting skills. Recommended routine: weekly while a deadline is open, then monthly. Recommended mail plugin: Gmail or AgentMail. Start with the `getting-started` skill.

Contributions: `CONTRIBUTING.md`. Code is MIT. Prose and templates are CC-BY-4.0.

Not legal advice.
