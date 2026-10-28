# Roadmap

Non è consulenza legale. Obiettivo: un servizio di rimozione per l'Europa, poi per il resto del mondo, con un metodo trasparente e che minimizza i dati.

Un'analisi pubblica di Incogni, non un elenco copiato da loro, indica circa 420 titolari, di cui 45 con copertura UE (soprattutto adtech) e nessuno italiano. Il punto forte riportato è il ricontrollo: ogni 60 giorni per i people-search e ogni 90 per i broker privati, salvo che la persona sia già in lista di soppressione (rilievo Deloitte ISAE 3000, agosto 2025, come citato in quell'analisi). I punti deboli che questo pacchetto non replica: segnare «completato» anche «nessun dato» senza prova; mandare nome e indirizzo a tutti i titolari di un'area; bloccarsi quando chiedono un documento. Qui i tre esiti finali richiedono una prova, l'invio è solo l'identificativo necessario, e la richiesta sproporzionata ha un modello (art. 12 par. 6 e art. 11).

Gli intervalli stanno in `manifest.json`, chiave `coverage.recheck_days`. Si cambiano lì, non a mano nelle schede.

## Fase 1 — Italia

Stato: `partial`.

Completare i titolari italiani, gli elenchi, il Registro Pubblico delle Opposizioni e i passi con gli operatori telefonici. Il file `data/countries/it.yaml` è il punto di partenza. I broker internazionali già in `data/brokers.yaml` non bastano a dire che l'Italia è coperta.

## Fase 2 — UE, SEE, Regno Unito e Svizzera

Un file `data/countries/<cc>.yaml` per ciascuno dei 27 Stati membri, per Islanda, Liechtenstein e Norvegia, e per Regno Unito e Svizzera. Dentro: titolari locali, elenchi, registri di opposizione (liste Robinson e equivalenti), autorità, lingue delle lettere. Lo stato parte da `todo` finché il file non ha fonti ufficiali verificate. La metrica di copertura confronta i titolari con rilevanza UE in questo repository con il riferimento di 45 citato sopra: è un conteggio nostro, non una copia della loro lista.

## Fase 3 — Resto del mondo

Stati Uniti (CCPA/CPRA e leggi dei singoli Stati, più people-search), Canada (PIPEDA), Brasile (LGPD), poi gli altri. I modelli di legge stanno in `templates/letters/` solo quando esistono e sono marcati come bozza. Oggi US, CA e BR sono `todo`: non c'è ancora una lettera specifica, per non presentare un testo incompleto come se fosse pronto.

## Tabella

| Codice | Fase | Stato |
| --- | --- | --- |
| IT | 1 | partial |
| AT BE BG HR CY CZ DK EE FI FR DE GR HU IE LV LT LU MT NL PL PT RO SK SI ES SE | 2 | todo |
| IS LI NO GB CH | 2 | todo |
| US CA BR | 3 | todo |

Lo stato vero è nel file del paese e in `manifest.json` (`coverage.countries`). Se divergono, conta il file e va allineato il manifest.

## Come contribuire un paese

1. Nessun dato personale. URL solo se l'hai aperta sul sito ufficiale.
2. Copia la struttura di `data/countries/it.yaml`. `status` è `todo`, `partial` o `done`. `done` richiede registri, autorità e almeno un canale verificato.
3. `verified_source` sui titolari nuovi, come in `data/brokers.yaml`.
4. Le lettere nuove portano il disclaimer. Tedesco, francese e spagnolo restano traduzioni di comunità finché qualcuno non le rivede.
5. Aggiorna `CHANGELOG.md`, `coverage` nel manifest e la tabella di questo file.
6. `python scripts/validate_repo.py` e `python scripts/security_lint.py`.

Il bot non apre la pull request: propone il testo in chat. Lo committa una persona.
