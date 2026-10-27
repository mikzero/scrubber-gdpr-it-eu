# Contribuire

Non è consulenza legale. Questo repository è il pacchetto che il bot legge. Non è il registro di una persona.

## Cosa si può proporre

- Un titolare nuovo, con la URL della pagina privacy o del modulo **sul sito del titolare**.
- Una URL morta (HTTP 404), un modulo che non offre l'opposizione, una casella di ruolo vista sulla pagina ufficiale.
- Una correzione a una skill, a un modello o alla dashboard.
- Una traduzione, marcata come traduzione di comunità finché qualcuno non la rivede.

## Cosa non va messo

Niente dati personali: niente numeri di telefono, email di persone, nomi, indirizzi, codici fiscali, screenshot di schede, risposte ricevute, OTP. I placeholder restano `{{NOME}}`, `{{TELEFONO}}`, `{{EMAIL}}`, `{{PAESE}}`.

Una `dpo_email` si aggiunge solo se è una casella di ruolo (`dpo@`, `privacy@` e simili) letta sulla pagina ufficiale, con `dpo_email_basis` (`named-dpo`, `rights-contact` o `cookie-withdrawal`) e `last_verified` aggiornata. Non si copiano caselle di persone fisiche.

## Come

1. Apri una issue dal template «Broker o URL» o «Correzione a skill o modello».
2. Per una modifica, lavora su un branch e apri una pull request. Il template della PR è la checklist.
3. Aggiorna `CHANGELOG.md`. Se cambia il comportamento del bot, aumenta `VERSION`, `manifest.json` (`version` e la `version` delle skill toccate) e, se aggiungi una skill, la voce nel manifest.
   - Patch: URL, casella, errore di testo.
   - Minor: skill nuova o modello nuovo, compatibile.
   - Major: cambia il senso di uno stato del registro o di una chiave che il bot già legge.
4. In locale: `pip install -r scripts/requirements.txt`, poi `python scripts/validate_repo.py`.
5. I link si controllano con `python scripts/check_links.py`. Un 404 fa fallire il comando. Un 403 è un avviso.

## Licenze

I testi e i modelli sono CC-BY-4.0 (`LICENSE-CONTENT`). Il codice è MIT (`LICENSE`). Vedi il README.

## Lingua

Le skill sono in italiano, all'imperativo, rivolte al bot. I modelli principali sono in italiano e in inglese. Tedesco, francese e spagnolo vanno marcati come traduzioni da rivedere.
