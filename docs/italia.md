# Italia, fase 1 e 1b

Le schede sono in `data/brokers.yaml`. Questo testo è la nota di ricerca, in italiano.
`rpo-it` e `garante-it` restano solo in `data/registries.yaml`. Il reclamo è l'unico canale del Garante.
`crif-it`, `creditsafe-it` e `cribis-dnb` non vanno fusi con le voci di altri paesi.
Fastweb Mobile è la stessa scheda di `fastweb-elenchi`. Tiscali Mobile è la stessa scheda di `tiscali-elenchi`.
Le voci `uncertain` non hanno un canale automatico.

# Copertura Italia, fase 1: note di ricerca

Data della verifica: 27 ottobre 2026. File collegati: `it.yaml` (50 voci, fase 1) e `it-1b.yaml` (43 voci, fase 1b).
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

Le categorie `directory`, `telco`, `registry`, `authority` e `contract` sono già ammesse da `scripts/validate_repo.py`.

## Conteggio per categoria

| categoria | voci |
|---|---|
| telco (revoca dagli elenchi, DBU) | 11 |
| people-search / caller ID | 10 |
| lists (liste, lead generation, concorsi) | 8 |
| credit | 7 |
| directory | 5 |
| registry | 4 |
| b2b (dati camerali) | 3 |
| authority | 2 |
| **totale** | **50** (2 da verificare) |

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

Subito dopo vengono `mxt-international` e `consodata`, poi CRIF ed Experian per i dati di contatto nel SIC.

## Lacune e voci da verificare

Aggiornamento del 27 ottobre 2026 (seconda passata, pagine JavaScript lette con un browser headless):

- **Risolte:**
  - TIM 1254: il modulo DBU di TIM lo cita come alimentato dal DBU, quindi basta il DBU;
  - MXT International: titolare Mxt Ltd (Cipro), casella diritti sulla policy;
  - Tinexta Visura: informativa PDF 2026 con DPO e casella privacy;
  - caselle DPO di Iliad, Fastweb, ho. (oggi Fastweb S.p.A.), Kena e CoopVoce, lette sulle loro informative;
  - Hiya: modulo Zendesk ufficiale "update/remove caller ID";
  - Eyecon: aggiunta voce (Instabridge, Svezia), ma senza pagina di unlisting pubblica, quindi email.
- **Ancora da verificare** (`uncertain: true`):
  - Tiscali: DPO trovato, ma nessun modulo elenchi/DBU pubblicato;
  - Consodata: sito "in costruzione", la vecchia S.p.A. è in liquidazione e c'è una nuova S.r.l. Il titolare attuale non è chiaro.
- **Fusione Fastweb–Vodafone:** ho. Mobile ha ora come titolare Fastweb S.p.A. La voce `vodafone-elenchi` cita ancora la pagina Vodafone: va ricontrollata quando i canali verranno unificati.
- **Garante:** oggi la pagina "segnalazione" separata risponde 404. Il canale è il reclamo.

## Fase 1b: titolari con contratto (`it-1b.yaml`)

Questa fase copre le società con cui l'utente ha un rapporto, che possono contattarlo per marketing con il consenso dato al contratto: 43 voci.

- **Categorie:** 35 `contract` (nuova categoria) e 8 `telco`.
- **Settori dentro `contract`** (indicati tra parentesi quadre all'inizio delle note):
  - banche e credito al consumo: 10;
  - assicurazioni: 6;
  - energia, gas e acqua: 9;
  - GDO e fidelity: 7;
  - comparatori: 3.
- **Operatori aggiunti** (`telco`): Lycamobile, spusu, 1Mobile, Optima, Sky Mobile e Digi. Fastweb Mobile e Tiscali Mobile sono alias delle voci già presenti in `it.yaml`, perché il titolare è lo stesso.
- **Azione di default:** revoca dei consensi marketing, profilazione e cessione a terzi, più opposizione art. 21 par. 2, con le lettere esistenti `revoca-consensi-operatore.md` e `art21-17-19-15.md`. Il contratto non si tocca. Se viene chiesto un documento per una semplice revoca, si risponde con l'art. 12 par. 6.
- **Metodo:** vindicis.org è servito solo come elenco dei titolari da coprire. Ogni casella è stata letta sulla pagina privacy o sull'informativa ufficiale del titolare, con il link in `verified_source`. Ho usato solo caselle di ruolo o DPO: per 1Mobile il DPO è un professionista con casella nominativa, quindi non l'ho inserito.
- **Da verificare** (3 voci):
  - Facile.it: la pagina non si legge dal box;
  - Segugio: il sito risponde 401/403;
  - Tiscali Mobile: nessun modulo elenchi.

  Per Facile e Segugio le note non copiano le caselle viste solo in ricerche web.
- **Ancora scoperti:**
  - le altre cooperative Coop (Coop Lombardia, Unicoop Firenze, Nova Coop…);
  - Mediolanum, Poste Vita, Zurich, Crédit Agricole Italia, ING;
  - Edison Energia sul proprio sito (in manutenzione: verificato sulla pagina di gruppo edison.it);
  - l'informativa clienti contrattuale di Optima (letta solo quella del sito);
  - per Fineco solo la casella diritti (DPO non letto).
- La categoria `contract` è già ammessa dal validatore. Queste schede sono opt-in: si aprono solo se l'utente dice di essere cliente, senza numeri di conto, polizza o utenza.

## Nota sulla concorrenza

L'idea che "Incogni non copre l'Italia" resta vera, ma non siamo soli. **Vindicis** (vindicis.org) pubblica guide di rimozione GDPR per 167 titolari, molti italiani: CRIF, Cerved, Cribis, CTC, Consodata, Italiaonline, Infobel, InfoCamere, tellows, Truecaller, gli operatori, banche, assicurazioni, energia e grande distribuzione. Il suo servizio a pagamento risulta "coming soon".

Due differenze a nostro favore:
- noi copriamo il DBU operatore per operatore e i list provider del telemarketing;
- la fase 1b di questo pacchetto copre le banche, le assicurazioni, le utility e il retail con cui l'utente ha un contratto, con la lettera di revoca consensi già presente. La cancellazione del rapporto si prepara solo se l'utente dice che il contratto è finito.
