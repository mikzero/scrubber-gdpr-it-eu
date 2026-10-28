# Casi difficili

Non è consulenza legale. Sono ostacoli già visti. Le note «esperienza operativa» in `data/brokers.yaml` non sono state riprodotte il giorno della versione 0.1.0.

## OTP via SMS

Alcuni moduli, in particolare OneTrust, mandano un codice via SMS. Su numeri italiani il messaggio può non arrivare. Caso annotato: Samba (Samba TV).

Non ritentare a oltranza e non chiedere all'utente un numero estero. Ordine di riserva: OTP via email se esiste; lettera alla casella di ruolo se è ancora sulla pagina ufficiale; nel registro, blocco tecnico e stato `in attesa`, non `rifiutato`.

Il codice lo legge l'utente. Il bot non lo indovina.

## Captcha e HTTP 400

Kaspr e altri moduli SayMine (anche Cognism usa SayMine) possono rispondere HTTP 400, in modo compatibile con un reCAPTCHA, e possono non offrire la voce art. 21 par. 2. Il captcha lo risolve l'utente nel proprio browser. Non si aggira.

Se manca l'opposizione nel modulo, si prepara la lettera. Per Kaspr, avvisare che in passato le richieste via email sono state rifiutate, anche se la privacy policy pubblica una casella per i diritti.

## Email aziendale

Il modulo di Apollo chiede un'email di lavoro. Non si inventa un dominio aziendale e non si traveste un'email personale. Se l'utente non ha un'email aziendale da usare, si dice e si cerca un altro canale sulla stessa pagina ufficiale.

## Processor

Adikteev e altri possono rispondere di essere solo responsabili del trattamento. La policy di Adikteev letta per la versione 0.1.0 descrive anche un ruolo di titolare per una parte dei dati. Si chiede il nome del titolare, si mantiene l'opposizione per i trattamenti di cui sono titolari, e si richiama l'art. 19.

## Adtech e identificativi di dispositivo

Criteo, Sirdata, i DSP e le piattaforme simili lavorano spesso su cookie e ID pubblicitari, non sul telefono. L'opt-out sul dispositivo (YourOnlineChoices, impostazioni del telefono, azzeramento dell'ID) è un passo in più, non un sostituto della richiesta se trattano anche email o telefono. Sirdata indica che, per un identificativo di cookie, un documento di identità non prova il controllo del terminale.

## Minimizzazione

LexisNexis può chiedere data di nascita e documento. Acxiom può chiedere l'indirizzo postale. North Data ha bisogno dell'URL del profilo, non di un URL costruito dal bot.

L'art. 12 par. 6 permette informazioni ulteriori solo se ci sono dubbi ragionevoli sull'identità. L'art. 5 par. 1 lett. c chiede il minimo. Il bot si ferma, spiega, e invia un dato in più solo con un sì esplicito su una bozza nuova. Il documento non entra nel repository.

## Credito

SCHUFA, CRIF, Equifax, Experian, TransUnion e Creditsafe possono conservare dati per obblighi di legge. L'opt-out marketing non è la cancellazione del fascicolo di credito. Si chiede la base e ci si oppone comunque al marketing diretto.

## «Nessun dato»

Non chiudere la pratica senza chiedere quali identificativi sono stati cercati e se esiste una lista di soppressione. Modello: `templates/letters/it/risposta-non-trovato.md`.
