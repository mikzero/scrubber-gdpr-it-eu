# Italia, fase 1

Le schede dei titolari sono in `data/brokers.yaml` (fonte `it-2026`). Questo file è il testo di ricerca, in italiano.
`rpo-it` e `garante-it` non sono duplicati lì: le note stanno in `data/registries.yaml`.
`crif-it`, `creditsafe-it` e `cribis-dnb` restano titolari distinti dalle voci UK, globale e tedesca.

# Copertura Italia, fase 1: note di ricerca

Data della verifica: 27 ottobre 2026. File collegato: `it.yaml` (49 voci).
Non è consulenza legale. Nel file non ci sono dati di persone fisiche né caselle nominative.

## Metodo e fonti

- Ogni canale (URL, modulo, casella email) viene da una pagina o da un PDF del titolare stesso: informativa privacy, modulo DBU dell'operatore, pagina di supporto. In più ci sono le pagine istituzionali di Garante, AGCOM, RPO e ANCIC.
- `dpo_email` è compilata solo quando la casella compare nel testo della pagina privacy (o informativa ufficiale) con un ruolo chiaro: DPO o RPD (`named-dpo`), oppure "scrivi qui per esercitare i diritti" (`rights-contact`). Quando ci sono solo contatti generici, il campo resta `null` e la casella, se utile, va nelle note.
- Le caselle a cui va inviato il modulo elenchi di un operatore (per esempio documenti119@…, PEC del servizio clienti) **non** sono DPO: stanno in `known_issues`.
- Gli articoli di terzi, le guide e i riassunti di ricerca sono serviti solo a trovare le pagine. Due caselle viste solo su siti di terzi (Consodata, Infobel) non sono state copiate.
- Il 27/10/2026 tutti i 65 URL del file rispondevano 200, tranne due: Tiscali (timeout dal box, ma letto con fetch) e MXT (202 senza contenuto).
- Sono escluse le caselle nominative trovate nell'elenco ANCIC e il nome del responsabile privacy di tellows.

## Schema

Il file usa gli stessi campi di `data/brokers.yaml` più due campi nuovi:
- `verified_source`: la pagina esatta da cui viene il canale;
- `uncertain`: true quando la voce va controllata a mano.

Ho aggiunto quattro valori di `category` (directory, telco, registry, authority), che vanno aggiunti anche a `scripts/validate_repo.py` prima del merge.

## Conteggio per categoria

| categoria | voci |
|---|---|
| telco (revoca dagli elenchi, DBU) | 11 |
| people-search / caller ID | 9 |
| lists (liste, lead generation, concorsi) | 8 |
| credit | 7 |
| directory | 5 |
| registry | 4 |
| b2b (dati camerali) | 3 |
| authority | 2 |
| **totale** | **49** (5 da verificare) |

## Rapporto con il repo

- Nessun doppione con `brokers.yaml`. Le voci vicine sono distinte apposta:
  - `creditsafe-it` è il titolare italiano, mentre `creditsafe` è la pagina UK;
  - `cribis-dnb` è il partner italiano di D&B, mentre `dun-bradstreet` è la voce globale;
  - `crif-it` è un titolare diverso da `crif-de`.
- Acxiom IT è già nel repo e non è stata ripetuta.
- `rpo-it` e `garante-it` riassumono cose che stanno già in `registries.yaml` (`rpo-it`, `it-garante`). Al merge conviene tenerle lì e copiare solo le note nuove sulla copertura del RPO.

## Cosa si è imparato

1. **Il DBU è la radice degli elenchi.** PagineBianche, 89.24.24, 1254 e Infobel prendono i numeri dal database unico. La rimozione vera si fa revocando il consenso presso l'operatore. Italiaonline e Infobel lo scrivono loro stessi.
   - Sul modulo DBU vanno chieste tre cose: NO all'elenco, NO ai servizi di informazione abbonati, NO alla posta pubblicitaria.
   - Con la portabilità restano le scelte fatte con il vecchio operatore.
2. **Le scelte sull'elenco si fanno dall'operatore, e il canale cambia da uno all'altro:**
   - area clienti: Iliad, Fastweb;
   - sito: Vodafone (voda.it/elenchipubblici);
   - email: TIM, Kena, CoopVoce;
   - PEC: WINDTRE, Very;
   - solo posta: ho.
   Quasi tutti i moduli chiedono un documento. Qui l'identificazione è legittima (serve a provare che sei l'intestatario), ma il bot propone prima l'area clienti, dove l'identità è già verificata.
3. **Il RPO dal 2022** copre fissi e cellulari, anche non in elenco, e le chiamate automatiche. L'iscrizione annulla i consensi dati prima, tranne i contratti continuativi (luce, gas, telefono) e i consensi dati dopo. Non copre SMS, email, chat né i call center abusivi o esteri.
4. **Le liste per il telemarketing** arrivano da "editori" (concorsi, co-registrazione) e passano a list provider. Nei provvedimenti il Garante oscura i nomi dei provider ("XX"), quindi la mappa si costruisce dai siti degli stessi venditori: Digital Metrics, Foryou, Concorsi Web/CWmedia, MXT. Restano i casi nominati in chiaro: Ediscom, Realmaps e Toleadoo.
5. **Con il portale ANCIC** una sola richiesta raggiunge circa 30 società di informazione commerciale. È la leva più efficiente per il credito e il B2B.
6. **Caller ID e spam.** In Italia contano tellows, MiChiama, GhostCallers, NoCall, Truecaller, Getcontact, Sync.ME, CallApp e Hiya. Qui il danno è doppio: il numero è esposto e, se l'etichetta è sbagliata, le chiamate dell'utente vengono bloccate.

## Priorità: le 15 voci più rilevanti per il numero di telefono

1. `rpo-it`: iscrizione al RPO (la fa l'utente)
2. operatore dell'utente, una sola di queste voci: `tim-elenchi`, `vodafone-elenchi`, `windtre-elenchi`, `iliad-elenchi`, `fastweb-elenchi`, `postemobile-elenchi`, `kena-elenchi`, `homobile-elenchi`, `very-elenchi`, `coopvoce-elenchi`
3. `italiaonline-elenchi` (PagineBianche, 89.24.24, TuttoCittà in un'unica richiesta)
4. `infobel-it`
5. `truecaller`
6. `tellows-it`
7. `michiama`
8. `ghostcallers`
9. `getcontact`
10. `digital-metrics`
11. `concorsiweb`
12. `ediscom`
13. `foryou`
14. `realmaps` (se le chiamate sono di agenzie immobiliari)
15. `hiya`

Subito dopo vengono `mxt-international` e `consodata`, appena verificati, poi CRIF ed Experian per i dati di contatto nel SIC.

## Lacune e voci da verificare

- **Da verificare a mano** (`uncertain: true`):
  - Tiscali: oggi non pubblica un modulo elenchi;
  - MXT International: pagina privacy vuota;
  - Consodata: forse in liquidazione, titolare attuale non chiaro;
  - Tinexta Visura: pagina informative in JavaScript;
  - TIM 1254: canale dedicato non trovato, quindi si passa dal DBU.
- **Senza casella DPO verificata:** Iliad, Fastweb, ho., Kena (vale il DPO TIM) e CoopVoce. Le loro pagine privacy sono caricate in JavaScript: vanno lette in un browser.
- **Operatori virtuali non coperti:** Spusu, Lyca, Fastweb Mobile, Tiscali Mobile, 1Mobile, Optima, Sky Mobile, Digi. Vanno aggiunti per completare l'Italia.
- **Liste e lead generation:** mancano i comparatori che raccolgono il numero per farti richiamare (Facile.it, Segugio, SuperMoney) e i grandi call center. Il Garante li cita spesso, ma non vendono liste.
- **Caller ID:** Eyecon non ha una pagina di unlisting leggibile, mentre il modulo di Hiya blocca i controlli automatici (403).
- **Garante:** oggi la pagina "segnalazione" separata risponde 404. Il canale è il reclamo.

## Nota sulla concorrenza

L'idea che "Incogni non copre l'Italia" resta vera, ma non siamo soli. **Vindicis** (vindicis.org) pubblica guide di rimozione GDPR per 167 titolari, molti italiani: CRIF, Cerved, Cribis, CTC, Consodata, Italiaonline, Infobel, InfoCamere, tellows, Truecaller, gli operatori, banche, assicurazioni, energia e grande distribuzione. Il suo servizio a pagamento risulta "coming soon".

Due differenze a nostro favore:
- noi copriamo il DBU operatore per operatore e i list provider del telemarketing;
- loro però coprono banche, assicurazioni, utility e retail, che da noi mancano.

Suggerisco una fase 1b dedicata a queste aziende "con cui l'utente ha un contratto", usando la lettera di revoca consensi che c'è già.
