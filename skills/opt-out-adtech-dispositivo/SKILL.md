---
name: opt-out-adtech-dispositivo
description: Use when il titolare è adtech e va fatto l'opt-out sul dispositivo o va azzerato l'ID pubblicitario.
---

# Opt-out adtech sul dispositivo

Non è consulenza legale. Molti titolari con `category: adtech` e `phone_relevance: low` non hanno il numero di telefono. Hanno un cookie, un identificativo pubblicitario del telefono (GAID o IDFA) o un identificativo simile. L'opt-out sul dispositivo limita la pubblicità profilata su quel browser o telefono. Non cancella un'email o un telefono conservati altrove: per quelli resta la richiesta `richiesta-gdpr-art21-17`.

Fai fare all'utente questi passi, uno alla volta. Non cliccare al posto suo su un account che non ti ha aperto.

1. Browser: apri YourOnlineChoices dalla URL in `data/registries.yaml` (`device_opt_out`) e, se l'utente usa account Google, le impostazioni annunci indicate lì. Disattiva la pubblicità personalizzata delle società elencate. È un opt-out del browser, non una lettera.
2. Android: Impostazioni, Google, Annunci, oppure il percorso equivalente della versione in uso. Azzera l'ID pubblicitario e disattiva la personalizzazione. I nomi dei menu cambiano: leggi quello che c'è sullo schermo, non un percorso imparato a memoria se non coincide.
3. iPhone: Impostazioni, Privacy e sicurezza, Tracking, e il menu della pubblicità Apple. Chiedi all'app di non tracciare e azzera l'identificativo se il sistema lo offre.
4. Televisori e app che compaiono nei `known_issues` (per esempio Samba): usa anche i controlli sul dispositivo indicati nella loro notice, oltre al modulo.

Se un titolare chiede l'ID pubblicitario dentro un modulo, l'utente lo copia dalle impostazioni del telefono dopo aver deciso di farlo. Non è un dato da mettere nel repo.

Questo opt-out non produce da solo uno stato `cancellato`. Nel registro puoi annotare `opt-out dispositivo` nelle note della riga adtech, con la data. Lo stato della richiesta GDPR resta quello della lettera o del modulo.

Se per completare l'opt-out il sito invia un'email o un modulo precompilato, mostralo. Serve un sì esplicito prima dell'invio. Un opt-out fatto di persona dall'utente nelle impostazioni del telefono non è un invio tuo: chiedi comunque conferma che vuole procedere, poi lascia fare a lui.
