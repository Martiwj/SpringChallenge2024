Marius, en ifi-student, tok emnet IN2010 - Algoritmer og datastrukturer denne høsten.
Han synes spesielt at grafer var interessant.

Marius mener at miljøet på ifi er godt, og ser at studenter samarbeider på tvers av linjer, kull og foreninger.
Han har en hypotese om at alle ifi-studenter egentlig er knyttet sammen i en stor vennegjeng. Marius definerer en vennegjeng litt utradisjonelt. Det er ikke slik at alle må kjenne alle, men at man er venner gjennom venners venner.
Si at vi har vennene Karl, og Olav. Olav har vennen Emma, så er også Emma og Karl i samme venngjeng.

For å teste hypotesen sender han ut en mail til alle registrerte ifi-studenter, med et nettskjema som ber dem om å angi sine venner. F.eks. kan ifi-studenten Mari med brukernavn marist si at hun har vennene "Karl", "Emma" og "Olav" (med sine brukernavn). Marius har selvfølgelig alt av GDPR i orden, og lagrer kun brukernavnene til dette formålet. Dette lagrer Marius så i en tabell som han kaller "venner.csv".

Du har fått dataen hans, men han husker ikke helt hvordan han skal implementere dette.

Formatet er slik:

navn1,venn1;venn2;venn3;venn4;...
navn2,venn1;venn2;venn3;venn4;...
navn3,venn1;venn2;venn3;venn4;...
...

Hjelp Marius å lage et program som skriver ut "hypotesen stemmer", hvis alle er knyttet sammen. Ellers skriver programmet ut antallet vennegjenger.