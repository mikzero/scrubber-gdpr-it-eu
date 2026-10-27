# Changelog

Tutte le versioni rilevanti di questo pacchetto sono elencate qui.
Il bot confronta il file `VERSION` e, se è cambiato, legge questo changelog
prima di applicare l'aggiornamento.

Il formato segue [Keep a Changelog](https://keepachangelog.com/) e il pacchetto usa [SemVer](https://semver.org/).

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
