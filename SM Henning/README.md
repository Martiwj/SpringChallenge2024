# Sjenkeproblemet

<img src="img/henning.jpg" alt="Alt Text" width="150" align="right">

Henning er en kul SM og vil at så mange som mulig av deltakerne på Lyntaler skal få øl, og alle som deltar bør få MAKS en øl.

Hver deltaker `i` har en grådighetsfaktor `g[i]`, som er den minimale størrelsen på en øl som deltakeren vil være fornøyd med. Tilsvarende har hver øl `j` en størrelse `s[j]`. Hvis størrelsen på ølet `j` >= deltakerens grådighetsfaktor `g[i]`, kan vi gi øl `j` til deltaker `i`, og deltaker `i` vil være fornøyd. Målet er å maksimere antall fornøyde deltakere ved å tildele ølet på en optimal måte, og deretter returnere det maksimale antallet.

Skriv en funkjson som hjelper Henning med dette!

input formatet er som følger:
`g` og `s` skilles på mellorom slik at ved feks: 
1,2,3 1,1
vil g = [1,2,3] og s = [1,1]