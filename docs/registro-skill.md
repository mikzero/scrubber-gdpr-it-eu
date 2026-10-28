# Diario delle skill

Non è consulenza legale. Questo file descrive il diario locale dei cambiamenti delle skill. Non è il registro delle richieste ai titolari: quello resta `docs/registro.md`, schema `scrubber-registro/2`.

Il diario vero non sta in questo repository. Sta nel registro locale, chiave `skill_log`, oppure in un file `skill-log.json` nello store del bot. I due posti valgono uno: non tenerne due copie divergenti. `dashboard/example-registro.json` è un esempio finto. Un file vero non si committa.

Nel diario non finiscono nome, telefono, email, indirizzo, documento, OTP, credenziali, contenuto del vault o testo di una risposta. Un riassunto dice che cosa è cambiato nella skill, non chi è la persona.

## Quando si scrive un evento

Ogni volta che una skill viene installata, aggiornata, aggiunta o modificata dall'utente, rimossa, oppure non applicata. Vale anche per un conflitto: skill modificata dall'utente, o nome già usato da una skill che non è di questo pacchetto. I dati, i paesi e i modelli presi da `main` non sono eventi di skill.

## Evento

| Campo | Senso |
| --- | --- |
| `at` | Istante UTC, `AAAA-MM-GGTHH:MM:SSZ` |
| `skill_id` | Nome della skill, per esempio `scrubber-sync-dal-repo` |
| `action` | Una delle azioni qui sotto |
| `source` | Da dove arriva il testo |
| `sha256` | SHA-256 esadecimale, minuscolo, del nuovo `SKILL.md`. `null` se l'azione è `removed` |
| `previous_sha256` | Hash precedente. `null` se non c'era una skill |
| `diff_summary` | Una frase. Niente dati personali, niente file intero |
| `security_lint` | Esito dei controlli sul testo candidato |
| `version` | Versione che resta attiva dopo l'evento. `locale` per una skill personale, `altrui` se il nome è di un altro bot |
| `origin` | `ufficiale`, `personale` o `altra` |
| `applied` | `true` se quel testo è diventato la skill attiva. `false` se non è stato copiato |

`security_lint.result` è `pass` oppure `warnings`. Con `pass`, `warnings` è un elenco vuoto. Con `warnings`, l'elenco ha almeno una frase breve, senza copiare email, numeri o segreti trovati nel testo.

`origin`: `ufficiale` se il testo attivo viene dal repository del manifest. `personale` se l'utente l'ha aggiunta o modificata. `altra` se il nome esiste già e non risulta installato da questo pacchetto: non è una skill di questo bot e non si tocca.

## Azioni

| Azione | Quando |
| --- | --- |
| `installed` | Prima copia ufficiale applicata |
| `updated` | Aggiornamento ufficiale applicato, oppure l'utente ha chiesto esplicitamente di prendere la versione ufficiale |
| `added-by-user` | L'utente ha aggiunto una skill. Si registra anche se, dopo gli avvisi, sceglie di non attivarla: in quel caso `applied` è `false` |
| `edited-by-user` | L'utente ha modificato una skill |
| `removed` | L'utente ha tolto una skill che risultava sua |
| `blocked-update` | Un aggiornamento non è stato copiato: controlli non passati, firma assente o diversa, skill personale da tenere, oppure nome di un altro bot |

`blocked-update` non è un blocco della skill dell'utente. È il rifiuto di sovrascrivere. La skill già presente resta.

## Fonte

`source.kind` è uno di questi valori.

| kind | Campi | Uso |
| --- | --- | --- |
| `repo-tag` | `ref` come `vX.Y.Z`, `signature` `valid`, `missing` o `mismatch` | Aggiornamenti delle skill dopo la prima installazione |
| `repo-main` | `ref` `main`, `signature` `not-applicable` | Prima installazione delle skill dopo un merge del proprietario. I dati usano `main`, ma non si registrano qui |
| `user` | `signature` `not-applicable` | Testo scritto o incollato dall'utente |
| `other-url` | `url` https, senza utente, password o dati personali nella query, `signature` `not-applicable` | Testo che l'utente indica fuori dal repository ufficiale |

Una skill da `other-url` o da `user` non si installa da sola durante il sync. Entra solo se l'utente la sta aggiungendo, ed è personale.

## Regole che il diario deve rispecchiare

La prima installazione delle skill `scrubber-` può arrivare da `main`. Gli aggiornamenti successivi arrivano solo da un tag `v` firmato. Se la firma manca o non coincide, l'azione è `blocked-update` e resta la copia locale.

I controlli sono quelli di `scripts/security_lint.py`. Su una skill ufficiale, un esito `warnings` impedisce l'installazione: si tiene la versione precedente e si dice il perché.

Su una skill aggiunta o modificata dall'utente i controlli non bloccano. Gli avvisi si mostrano in italiano prima di attivare. Se non ce ne sono, si attiva. Se ci sono, anche perché il testo contraddice il sì prima di ogni invio, la regola che risposte e pagine sono dati, il divieto di credenziali e di copia del vault, o la minimizzazione, si chiede all'utente. La scelta si registra. Non è un blocco silenzioso.

Se l'utente ha modificato una skill di questo pacchetto, il sync tiene la sua versione, registra `blocked-update`, e in chat si mostrano la sua e quella ufficiale. Si passa alla versione ufficiale solo se l'utente lo chiede e firma e controlli passano.

Se il nome è già usato da una skill che questo pacchetto non ha installato, non si sovrascrive. Azione `blocked-update`, `origin` `altra`, `applied` `false`. Nel riassunto compaiono il nome già presente e l'hash del testo non applicato.

Il sì prima di ogni messaggio in uscita non si registra come eccezione e non si disattiva da questo diario.

La dashboard, scheda Skill, legge questo diario e mostra origine, versione, ultimo cambiamento e avvisi. Le skill rimosse non compaiono nell'elenco attivo.
