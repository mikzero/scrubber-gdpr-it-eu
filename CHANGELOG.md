# Changelog

Tutte le versioni rilevanti di questo pacchetto sono elencate qui.
Il bot confronta il file `VERSION` e, se è cambiato, legge questo changelog
prima di applicare l'aggiornamento.

Il formato segue [Keep a Changelog](https://keepachangelog.com/) e il pacchetto usa [SemVer](https://semver.org/).

## 0.3.2 — 2026-10-27

### Added

- Seconda passata Italia: TIM 1254, MXT, Tinexta Visura, Eyecon e le caselle di Iliad, Fastweb, ho., Kena e CoopVoce.
- Fase 1b: banche, assicurazioni, energia, fidelizzazione, comparatori e operatori mobili in più. Categoria `contract`.
- Per un contratto attivo la richiesta di default è la revoca dei consensi e l'opposizione al marketing, non la cancellazione del rapporto. Si parte solo se l'utente dice di essere cliente.

### Changed

- Hiya usa il modulo ufficiale. Fastweb Mobile e Tiscali Mobile non sono schede doppie.
- Restano da verificare, senza canale automatico: Tiscali, Consodata, Facile.it e Segugio.

Non è consulenza legale.

## 0.3.1 — 2026-10-27

### Added

- Copertura Italia fase 1: elenchi, operatori del database unico, liste, credito, caller ID e portale ANCIC. Le note sono in `docs/italia.md`.
- Categorie `directory`, `telco`, `registry` e `authority`. Le voci `uncertain` non si contattano.

### Changed

- RPO e Garante restano solo in `data/registries.yaml`. Il reclamo è l'unico canale del Garante: la pagina di segnalazione risponde 404.
- `crif-it`, `creditsafe-it` e `cribis-dnb` restano titolari distinti dalle voci di altri paesi.

Non è consulenza legale.

## 0.3.0 — 2026-10-27

### Added

- Più caselle per titolare, con base e pagina di verifica. L'email verificata per i diritti resta ammessa anche se esiste un modulo.
- Titolari italiani e di elenchi telefonici verificati in questa passata, più alcuni broker UE la cui casella è stata letta sulla pagina ufficiale.
- `country_scope` e `phone_flow`: un residente in Italia non parte dall'adtech a bassa rilevanza né dal credito DE/UK o da 192.com senza un legame.
- Autorizzazione singola, di gruppo o `STOP`. Report settimanale compatto in cinque righe.
- Modelli per canale non obbligatorio, scheda d'impresa, delega art. 80 e app di cui la persona non è utente.
- Le skill si installano solo da un tag firmato. L'allowlist dei domini è quella già installata. Il lint rifiuta «invia senza chiedere il sì».

### Changed

- Adloox resta un contatto solo per i cookie: non è un canale email per il GDPR.
- Samba punta al privacy center del consumatore. RampedUp e L.S Mobile Apps usano l'URL che risponde.
- Gli annunci Google puntano alla guida di My Ad Center.

Non è consulenza legale.

## 0.2.1 — 2026-10-27

### Changed

- Dashboard riscritta per chi non è tecnico: tre numeri, barra «quanto sei protetto», riquadro «Cosa devi fare tu» e semaforo sulle aziende. Identificativi, prove e caricamento del file stanno in Dettagli.

Non è consulenza legale.

## 0.2.0 — 2026-10-27

### Added

- Metodo operativo unico (`docs/metodo.md`, skill `metodo-operativo`): scheda caso, etichette, stati, moduli, report settimanale.
- Registro `scrubber-registro/2` con maschera dell'identificativo, prove, ricontrollo a 60 o 90 giorni e stato `escluso`.
- Sicurezza e minimizzazione: repository in sola lettura, aggiornamento automatico con lint, niente invii in massa.
- Roadmap Europa poi resto del mondo, e un file per paese in `data/countries/`.
- Modello per le richieste di documento sproporzionate (art. 12 par. 6 e art. 11), anche in tedesco, francese e spagnolo da rivedere.
- `scripts/security_lint.py` e workflow dedicato. `CODEOWNERS` su `skills/`.

### Changed

- I dati e i modelli si aggiornano da soli dal raw pubblico. Le skill solo se passano i controlli. Non si chiede più il sì per sovrascrivere il pacchetto. Il sì resta obbligatorio per ogni invio a un titolare.
- `cancellato`, `nessun-dato` ed `escluso` richiedono una prova. La dashboard mostra la copertura delle prove.

Non è consulenza legale.

## 0.1.0 — 2026-10-27

### Added

- Prima versione del pacchetto Scrubber GDPR IT-EU.
- Undici skill, modelli di lettera (it, en; de, fr, es da rivedere), elenco broker e registri.
- Dashboard statica con registro di esempio finto.
- Controllo mensile dei link in `data/*.yaml`.

Non è consulenza legale.
