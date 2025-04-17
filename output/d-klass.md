# Raadioamatööri õppematerjal
# D-kategooria
Madis Kaal <mast@nomad.ee> 2025

Käesolev dokument on kogu erinevatest allikatest kokku korjatud
materjalidest ning ERAÜ raadioamatööri kvalifikatsioonieksamil
esitatavatest küsimustest. Dokument on programselt kokku pandud
andmekogust mis sisaldab nii õppematerjali kui küsimusi.

Sellise uue andmekogu loomise eesmärke on mitu:

1. Küsimuste süstematiseerimine, korrastamine ja sünkroniseerimine erinevate
allikate vahel.
2. Eksamiks õppimise lihtsamaks tegemine, koondades kõik eksami
sooritamiseks vajalikud teadmised ühte kohta ja jättes välja kõik
mis ei ole selleks vajalik.
3. Võimaldada sisse viidud muudatuste järel automaatselt uuendada
erinevates keskkondades kasutatavaid küsimustikke ja õppematerjale.
4. Tagada, et kvalifikatsiooniklassi küsimused puudutaksid ainult sellele
kvalifikatsiooniklassile vajalikku materjali (näiteks B-klassi küsimustes ei
peaks olema morsekoodi puudutavaid küsimusi).
5. Luua üks koherentne algallikas mille baasil saab olemasolevaid
eksamiküsimusi üle vaadata, muuta ja täiendada.

Suur osa selle andmekogu sisust pärineb järgmistest allikatest:

Eksamiküsimused

* ERAÜ koduleht https://erau.ee/
* ES2ICE kodulehelt https://es2ice.era.ee/

Õppematerjal
 * Jüri Ruudu (ES5JR) Algaja raadioamatööri teatmik http://www.bumpclub.ee/~jyri_r/Teatmik
 * Wikipedia https://et.wikipedia.org/




# C01 Raadio- ja elektrotehnika teooria

## S01 Mõõtühikud
Elektrivoolu tugevus ehk voolutugevus ***I*** on füüsikaline suurus, mis
võrdub ajaühikus elektrijuhi ristlõike pinda läbinud elektrilaenguga, selle
mõõtühik on Amper (***A***). Voolutugevust mõõdetakse ampermeetriga,
kusjuures ampermeeter ühendatakse vooluringi jadamisi.

Pinge (***U***) on füüsikaline suurus, mis iseloomustab kahe punkti vahelist
elektrivälja potentsiaalide erinevust. Eristatakse alalispinget (püsiva polaarsusega)
ja vahelduvpinget (vahelduvasuunalise polaarsusega). Pinge mõõtühik on Volt
(***V***). Pinget mõõdetakse voltmeetriga.

Takistus ***R*** iseloomustab elektrijuhi omadust avaldada elektrilaengute
liikumisele takistavat mõju. Takistuse mõõtühik on oom (***Ω***).

Sagedus ***f*** on võrdsete ajavahemike tagant korduvate sündmuste (nt. võngete, impulsside) arv ajaühikus.
Sageduse ühik on herts (***Hz***), 1 sündmus sekundis on 1 Hz.

Periood ehk võnkeperiood ***T*** on korduva muutuse tsükli kestus. Periood
on sagedusega pöördvõrdelises seoses, T=1/f. Perioodi ühik on sekund
(***s***).

Lainepikkus ***λ*** on kaugus kahe teineteisele lähima samas faasis võnkuva punkti vahel.
Siinuslaines on lainepikkuseks näiteks vahemaa kahe lähima laineharja või lainenõo
vahel. Lainepikkuse mõõtühik on meeter (m).

Lainepikkus on võrdne laine levimiskiiruse ***v*** ja laine sageduse ***f*** jagatisega:

λ=v/f

Helilainete puhul on levimiskiiruseks helikiirus (õhus umbes 330 m/s).
Elektromagnetlaine levib vaakumis valguse kiirusega c=299792458m/s.

Elektrimahtuvus ***C*** (lühemalt mahtuvus) iseloomustab elektrit juhtiva keha või kondensaatori
võimet salvestada elektrilaengut. Mahtuvuse mõõtühik on farad (***F***).

Induktiivsus ***L*** on elektromagnetilist induktsiooni iseloomustav füüsikaline suurus.
Induktiivsuse mõõtühik on henri (***H***).

Igal elektrijuhil (nt juhtmekeerul, poolil jm juhtival kontuuril) on teatav
induktiivsus, sest juhti läbiva
vooluga kaasneb alati magnetväli. Induktiivsus avaldub võimena takistada eneseinduktsiooni tõttu
voolu muutumist. Näiteks mida suurem on pooli induktiivsus, seda aeglasemalt alalisvool
sisselülitamise järel poolis tugevneb. Vahelduvvooluahelas suureneb koos induktiivsuse
ja sagedusega pooli induktiivtakistus.

Juhul kui voolu muutus ühes kontuuris (näiteks trafo mähises) indutseerib vastastikuse
induktsiooni teel elektromotoorjõu ka teises kontuuris (teises mähises), on tegemist
vastastikuse induktiivsusega. Vastastikuse induktiivsuse tähis on M või, mõõtühik
ikka henri.

Näivtakistus ehk impedants ***Z*** on elektriahela kahe punkti vahel perioodilisele siinuselisele
vahelduvasuunalisele elektrivoolule ehk vahelduvvoolule avalduv takistus, mis koosneb kahest
põhikomponendist:

* aktiivtakistus ehk resistants ***R***  ‒ iseloomustab elektrienergia muundumist teist liiki energiaks, näiteks soojuseks;
* reaktiivtakistus ehk reaktants ***X*** - iseloomustab elektrienergia perioodilist kadudeta toimuvat muutumist magnetvälja või elektrivälja energiaks.

Induktiivsete ahelaelementide reaktiivtakistus on induktiivtakistus ja mahtuvuslike elementide
reaktiivtakistus on mahtuvustakistus. Impedants on sagedusest on sõltuv
suurus. Induktiivtakistus suureneb sageduse suurenemisel, mahtuvustakistus
väheneb sageduse suurenemisel. Induktiivtakistust loetakse positiivseks ja
mahtuvustakistust negatiivseks.

Impedantsi mõõtühik on oom (***Ω***).

Elektrotehnikas eristatakse hetk-, aktiiv-, reaktiiv- ja näivvõimsust.
Elektriseade kas muundab mingit liiki energiat elektrienergiaks
(näiteks elektrigeneraator) või elektrienergiat teist liiki energiaks
(näiteks elektripliit soojuseks). Seadme elektrivõimsus väljendab
ajaühikus toodetava või tarbitava elektrienergia hulka.
Tarbiva elektriseadme ehk elektritarviti võimsust nimetatakse ka
võimsustarbeks.

* Hetkvõimsuseks ***p*** nimetatakse pinge ja voolutugevuse hetkväärtuse korrutist.
* Aktiivvõimsus ***P*** on vahelduvvoolu hetkvõimsuse keskväärtus ühe perioodi kestel.
* Reaktiivvõimsus ***Q*** iseloomustab kiirust, millega energia salvestub reaktiivtakistusega elektriahelaelementidesse, näiteks kondensaatorisse ja induktiivpooli, samuti energiavahetust ahelaosade vahel.
* Näivvõimsus ***S*** on aktiiv- ja reaktiivõimsuse geomeetriline summa.

Aktiivtakistusega R elektritarviti võimsus P on arvutatav pinge U ja voolu I kaudu järgmiselt:

P = U * I = I * I * R = U * U * R 

Aktiivvõimsuse mõõtühik on vatt (***W***), reaktiivvõimsuse ühik varr
(***var***) ja näivvõimsuse ühik voltamper (***V•A***).


---
***Kordamisküsimused***
* Mis ühikutes mõõdetakse raadiolaine pikkust?
* Mis ühikutes mõõdetakse raadiolaine sagedust?
* Mida mõõdetakse vattides?
* Mida mõõdetakse voltides?
* Mida mõõdetakse oomides?
* Mida mõõdetakse amprites?
* Mida mõõdetakse hertsides?
* Mida mõõdetakse meetrites?
* Miks mõõdetakse lainepikkust meetrites?
## S02 Mõõtühikute eesliidetest
Raadioamatörismis, nagu teistelgi tehnikaaladel, on vajalik nii väga suurte
kui ka väga väikeste arvude väljendamine.

Selleks, et see kergem oleks ja poleks vaja paljusid nulle loendada, kasutatakse eesliiteid,
mis vastava mõõtühiku ette lisatakse.

Suurte arvude väljendamine eesliidete abil:

|Kordaja|Eesliide|Tähis|Näide|
|-------|--------|-----|-----|
| 1000 | kilo | k | 1 kHz = 1000 Hz |
|1 000 000 | mega | M | 1 MHz = 1000000 Hz == 1000 kHz |
|1 000 000 000 | giga | G | 1 GHz = 1000 MHz = 1000000000 Hz |
|1 000 000 000 000 | tera | T | 1 THz = 1000 GHz = 1000000000000 Hz |

Väikeste arvude väljendamine eesliidete abil:

|Kordaja|Eesliide|Tähis|Näide|
|-------|--------|-----|-----|
| 0,001 | milli | m | 1 mm= 0,001 m |
| 0,000001 | mikro | μ | 1 μm = 0,001 mm |
|0,000000001 | nano| n | 1 nm = 0,001 μm |
| 0,000000000001 | piko | p | 1 pm = 0,001 nm |


---
***Kordamisküsimused***
* Miks kasutatakse mõõtühikute ees liiteid “piko-”, “nano-”, “mikro-”, “milli-”, “kilo-“, “mega-“, “giga-”, “tera”?
* Miks kasutatakse mõõtühikutes eesliidet “mega”?
* Kuidas on seotud sagedused 5 000 000 hertsi ja 5 megahertsi?
* Kuidas on seotud sagedused 5 000 hertsi ja 5 megahertsi?
* Kuidas on seotud sagedused 5 mHz ja 5 MHz?
* Mis on võrdne 1 kilovatiga?
* Te töötate sagedusel 14250 kHz ja tahate sagedust muuta 5 kHz ülespoole. Mis on teie uueks töösageduseks?
* Kuidas on seotud suurused 10 kilohertsi ja 10 millivolti?
## S05 Elektromagnetlained ja raadiolained
Raadiolained on lähedased sugulased valgusele, soojusele ja röntgenikiirtele. Kõik
nad kuuluvad elektromagnetlainete hulka, kujutades endast elektri- ja magnetvälja
võnkumisi. Peale valguse on elektromagnetlained inimesele nähtamatud.

Kõik elektromagnetlained levivad valguse kiirusel, ligikaudu 300000 km/s. 

Heli, mida me vastuvõtjast kuuleme, on samuti laine, kuid mitte
elektromagnet-, vaid helilaine, mis kujutab endast õhu võnkumist.
Peale õhu suudab heli levida ka vedelikes ja tahketes kehades,
kuid mitte vaakumis. Helilaine kiirus õhus on 330 m/s, see on umbes
miljon korda väiksem kui elektromagnetlainetel.

Elektromagnetlainete omadused sõltuvad nende lainepikkusest. 
Raadiolained on elektromagnetlainetest kõige suurema lainepikkusega, see võib ulatuda
tuhandetest meetritest mõne sentimeetrini. Vastavalt sellele jaotatakse raadiolained
pikk-, kesk-, lühi- ja ultralühilaineteks.

---
***Kordamisküsimused***
* Milliseid laineid kasutatakse raadiosides?
* Millise ajaga läbivad raadiolained 300 000 kilomeetrit?
* Mis vahe on elektromagnetlainetel ja raadiolainetel?
* Mida ühist on elektromagnetlainetel ja raadiolainetel?
* Mida ühist on valgusel ja raadiolainetel?
* Mis vahe on raadiolainetel ja helilainetel?
* Kui kiire on raadiolaine?
* Mille poolest sarnanevad pikklained, kesklained, lühilained ja ultralühilained?
* Mis vahe on pikklainetel, kesklainetel, lühilainetel ja ultralühilainetel?
* Mis on lainepikkus?
* Mis on sagedus?
* Kuidas on seotud elektromagnetlaine lainepikkus ja sagedus?
* Kui saadetava raadiolaine sagedus suureneb 2 korda, kuidas muutub lainepikkus?

# C02 Raadio- ja elektrotehnika komponendid

## S01 Passiivkomponendid
Passiivkomponentideks loetakse takistid, kondensaatorid ja induktiivkomponendid, sealhulgas ka transformaatorid.

### Takistid

Takistite abil saab anda elektriahelale vajaliku takistuse.

Takisteid on palju erinevaid, kõige tavalisem neist on aktiivtakisti mida
nimetatakse ka lihtsalt takistiks. Takisti kõige olulistemateks parameetriteks on
nominaalväärtus, võimsustaluvus ja materjal, sest sellest sõltuvad veel
mõned olulised parameetrid. Takistite takistus ei vasta pea kunagi
täpselt nominaalväärtusele, tootmisvigade ja takistitele omase takistuse
muutumise temperatuuri kõikumisel tüüpiliselt takistite takistus kasvab
temperatuuri tõustes. Takistuse muutumise suuruse määrab takisti
materjalist sõltuv temperatuuritegur.

Muuttakistite takistust saab sujuvalt muuta, kõige tuttavam on kõigile
potentsiomeeter, seda kasutatakse näiteks raadiovastuvõtja helitugevuse
reguleerimiseks.

Oluline takistite rühm on termotaksitid ehk termistorid, need on ehitatud
selliselt, et nende takistus muutub temperatuuri kõikumisel väga suurtes
piirides. Sealjuures on olemas nii sellised mille takistus temperatuuri
tõustes kasvab kui sellised, mille takistus temperatuuri tõustes langeb.
Neid saab kasutada temperatuuri mõõtmiseks aga ka näiteks
jahutusventilaatori kiiruse reguleerimiseks sõltuvalt seadme temperatuurist.

### Kondensaatorid

Kondensaatorite põhiomadus on mahtuvus, ehk võime salvestada elektrilaengut.
Põhimõtteliselt koosnevad nad kõik kahest elektroodist ja neid eraldavast
elektrit mitte juhtivast kihist. Kondensaatori mahtuvuse määrab elektroodide
pindala ja neid eraldava dielektriku paksus, seepärast teakse nii
elektroodid kui dielektrik võimalikult õhukesed. Sõltuvalt vajalikest
omadustest valmisatakse kondensaatoreid erinevatest materjalidest.

Ka kondensaatoreid on püsiva väärtusega ja muudetava väärtusega, sagedamini
leiavad kasutust püsiva väärtusega kondensaatorid. Kondensaatorite
olulisimad parameetrid on mahtuvus ja pingetaluvus. Nagu takistid, ei ole ka
kondensaatorid ideaalsed ja erinevad nominaalväärtusest, nende mahtuvus võib
ajas või näiteks temperatuuri kõikumisel oluliselt muutuja ja nad võivad
omada ka arvestatavat aktiivtakistust. Tänapäeval on õpitud väga väikeseid
ja suhteliselt suure mahtuvusega keraamilisi kondensaatoreid tegema, nende
headeks omaduseks on ka vähene sisetakistus ja induktiivsus, seepärast
sobivad nad hästi igasuguste järskude impulsside ja muude mürade filtreerimiseks
ning kõrgsagedusahelates kasutamiseks.

Eraldi mainimist väärivad elektrolüütkondensaatorid, sest neile saab
suhteliselt väikese ruumala juures anda väga suure mahtuvuse. Dielektrikuks
on nende sees imeõhuke oksiidikiht mille tekitamiseks ja püsimiseks on
kondensaatori sisu immutatud elektrolüüdiga. Aja jooksul võib elektrolüüt
neist välja lekkida, selle tulemusena rikneb kondensaator aga korrosiivne
elektrolüüt võib kergesti rikkuda ka teised läheduses olevad komponendid või
trükkplaadi millel komponendid paiknevad. Suure mahtuvuse tõttu kasutatakse
neid sageli toiteahelates pinge silumiseks.
 
Muutkondensaatorid võimaldavad elektroode teineteise suhtes nihutada, muutes
niiviisi kondensaatori mahtuvust. Vanades raadiotes kasutati pea alati suurt
pöördkondensaatorit mis koosnes üksteisega vaheliti metall-lehtedest.

### Indiktiivelemendid

Kõige lihtsam induktiivelement on induktiivpool, selle põhiline tunnus on
elektriline induktiivsus. Pool koosneb mingist hulgas traadikeerdudest mis
võivad olla mähitud poolialusele. Poolide induktiivsuse suurendamiseks
kasutatakse ferromagnetilisi poolisüdamikke, kõrgsageduspoolid on sageli
ilma aluseta ja südamikuta traadikeerud. Ka poolide induktiivuse saab
muudetavaks teha, selleks tehakse poolisüdamik pooli sees liigutatavaks.

Ka induktiivelemendid ei ole ideaalsed, nende mähisetraat omab aktiivtakistust
mis tekitab poolis energiakadu, lisaks sellele moodustavad mähisekeerud ja
kondensaatori mille tõttu on poolidel soovimatu omaresonantsisagedus.

Kui ühele südamikule mähkida mitu induktiivpooli siis moodustub
transformaator, kus südamik moodustab mähiseid omavahel siduva magnetahela.
Ühele mähisele antav vahelduvpinge tekitab südamikus muutuva magnetvoo mis
indutseerib teises mähiseks vahelduva elektromotoorjõu, kui mähisega
ühendada elektriahel siis läbib seda eletrivool.

---
***Kordamisküsimused***
* Milleks kasutatakse takisteid?
## S02 Aktiivkomponendid

Tänapäevased aktiivkomponendid põhinevad pooljuht-tehnoloogial. Pooljuht on
aine mille elektrijuhtivus on halvem kui elektrijuhil ja parem kui dielektrikul.
Tuntimad pooljuhid on räni ja germaanium aga tegelikult on neid materjale
palju, kõrgsageduslikes elementides kasutatakse palju galliumarseniidi
(GaAs). Pooljuhtide oluline omadus on nende suur tundlikkus välismõjudele ja
keemilistele lisanditele. Aluskristalli struktuuri teisi elemente lisades
moodustatakse pooljuhtsiirded mis on aktiivkomponentide ehitusplokid.

## Dioodid

Diood on kõige lihtsam, ühe siirde ja kahe kontaktiga pooljuhtseade.
Tavaline alaldusdiood juhib elektrit ainult ühes suunas ja blokeerib
elektrivoolu vastassuunas. Dioodid ei ole ideaalsed, juhtivas suunas tekib
dioodil pingelang (päripinge) mis on tavalistel ränidioodidel 0.7-1.7V
vahemikus, see tõuseb tavaliselt voolu kasvades. Dioodidel on piir kui suurt
vastusuunalist pinget (vastupinget) nad on võimelised taluma. Selle
ületamisel tekib dioodis pinge läbilöök.

Lisaks on dioodidel ka sisemine mahtuvus mille tõttu voolu suuna
vahetumisel pärisuunalisest vastusuunaliseks voolab ahelas lühikese
aja (taastumisaja) jooksul vastassuunaline vool. Selle tõttu
tekib alaldites impulssmüra ja kõrgepingealaldis kus on mitu dioodi
järjestiklülituses võib teistes varem sulguvale dioodile tekkida
ülemäära suur vastupinge. Nende impulsside silumiseks ühendatakse dioodidega
paralleelselt väikese mahtuvusega kondensaatorid. 

Väikese sisemise mahtuvusega dioode millel on hästi lühike taastumisaeg nimetatakse
impulssdioodideks. Schottky dioodid on väikese päripingega ja oluliselt
kiiremad kui tavalised ränidioodid aga nende lubatud vastupinge on
suhteliselt madal.

Leiutatud on ka mitmeid eriotstarbelisi dioode, neist kõige silmahakkavamad
on valgusdioodid ja laserdioodid mis päripinge all olles helendavad.
Mahtuvusdiood ehk varikap on selline diood mille sisemine mahtuvus on sõltuv
dioodile rakendatud vastupingest, see teeb neist omamoodi muutkondensaatorid.
Tunneldioodid omavad mingis päripinge vahemikus negatiivset takistust,
see võimaldab neid kasutada signaalide lülitamiseks, võimendamiseks ja
genereerimiseks. Suurte pingeimpulsside summutamiseks kasutatakse
suppressordioode (TVS) mille põhiomaduseks on taluda suuri impulssvoole
vastupinge piiri ületamisel.

Väga oluline diooditüüp on stabilitron ehk Zeneri diood. Stabilitronidel on
täpselt ette antud vastupinge mille juures diood hakkab vastassuunas voolu
läbi laskma, selle juures jääb vastupinge üsna muutumatuks. See teeb
stabilitronist pinget stabiliseeriva komponendi, voolu piiramiseks lubatud
piiridesse ühendatakse stabilitroni ja toiteallika vahele tavaliselt takisti.
Sõltumata toiteallika pinge kõikumisest jääb stabilitronile stabiilne
vastupinge eeldusel, et toiteallika pinge ületab alati stabilitroni
vastupinget.

## Transistorid

Transistorid on mitme, tavaliselt kahe siirdega pooljuhtelemendid. Nad
jagunevad kaheks suureks perekonnaks - bipolaartransistorid ja
väljatransistorid.

Bipolaartransistoril on kolm väljaviiku (kollektor, baas, emitter) ja nende
vahel kaks siiret, emittersiire ja kollektorsiire. Transistori juhtakse
baasi ja emitteri vahel voolava vooluga, kollektori ja emitteri vaheline
vool on juhtvool korrutatud transistori võimendusteguriga eeldusel, et
transistor töötab oma aktiivses tööpiirkonnas. Mingist hetkes alates
kollektorvool enam ei suurene, transistor on sellisel juhul küllastunud
seisus. Nagu dioodil on ka transistori siiretel päripingelang, sellest
väiksem pinge emittersiirdel ei saa transistori juhtida ja ka küllastumiseni
avanenud transistorile jääb päripinge. Transistore on kahtpidi polaarsusega,
NPN transistor juhib voolu kollektori poolt emitteri poole, PNP transistor
juhib voolu emitteri poolt kollektori poole.

Väljatransistorid on pingega juhitavad transistorid millel on samuti
tavaliselt kolm väljaviiku. Neid nimetatakse lätteks, neeluks ja
paisuks (source, drain, gate). Paisule rakendatud pinge muudab lätte ja
neelu vahelise voolu tugevust, kusjuures lätte ja neelu vaheline siire
käitub rohkem takistina kui tavalise pooljuhtsiirdena, seepärast ei räägita
nende puhul päripingest vaid täiesti avatud transistori takistusest.
Väljatransistore on samuti kahtpidi polaarsusega, N-kanali ja P-kanali tüüpi. 

On olemas ka nende kahe transistoritüübi hübriid, isoleeritud paisuga
transistor, tavaliselt bipolaartransistori tüüpi emitter-kollektor siirdega
mida saab paisule antava pingega juhtida. Neid kasutatakse sageli suurte
pingete ja voolude puhul, näiteks elektrimootoreid juhtivates
sagedusmuundurites.

## Türistor

Türistor pooljuhtseade mis käitub nagu juhtav diood mis on vaikimisi mõlemas
suunas suletud aga mida saab pärisuunas avada tüürelektroodile rakendatava
pingeimpulsiga. Tavaline türistor jääb selle juures avatuks kuni pärisuunaline vool
langeb alla piirväärtuse mille juures türistor uuesti sulgub, on olemas ka
tüürelektroodi abil suletavad türistorid.

Väga kasulik seade on sümmeetriline türistor ehk sümistor, mis avatuna juhib
voolu mõlemas suunas. Selle omaduse tõttu on ta sobiv vahelduvpinge
lülitamiseks.

Türistoriga väga sarnane komponent on dioodtüristor ehk diiak, sellel pole
juhtimiseks tüürelektroodi vaid ta avaneb mingist kindlast talle rakendatud
pingest.

---
***Kordamisküsimused***
* Mis on pooljuhi põhiomadus?
## S04 Ühendused

---
***Kordamisküsimused***
* Mispärast kasutatakse raadiotehnika detailide valmistamiseks vaske?
* Mis on kaablite ja juhtmete ümber oleva plastmassikihi ülesanne?
* Miks kasutatakse isolaatorite valmistamiseks portselani?
* Mida kasutatakse antennikaabli ühendamiseks transiiveriga?
* Miks kasutatakse raadiodetailide monteerimisel jootmist?
* Kuidas ühendaksite omavahel kaks vasktraati?
* Miks kasutatavad juhtmed ei või olla liiga väikese läbimõõduga?
## S05 Raadiolambid

---
***Kordamisküsimused***
* Mida saab öelda raadiolampide kohta?

# C03 Raadio- ja elektrotehnika ahelad

## S01 Alalis- ja vahelduvpinge

---
***Kordamisküsimused***
* Mida võib öelda alalisvooluahela pinge kohta?
* Mida võib öelda vahelduvooluahela pinge kohta?
## S03 Toiteahelad

---
***Kordamisküsimused***
* Mida teete kui transiiver vajab toiteks 12-voldilist alalispinget?
* Mis on toiteploki ülesandeks?
* Mida teete akude laadimiseks?
## S04 Maandus

---
***Kordamisküsimused***
* Mis materjali kasutate kui teil on vaja valmistada maanduskontuur?
* Milleks on vajalik maandusjuhe?
* Mis on Maandusjuhtme paigaldamisel kõige olulisem?
## S06 Kaitseahelad

---
***Kordamisküsimused***
* Mida teete kui sulavkaitse läbi põleb?
* Milleks kasutatakse raadioseadmetes sulavkaitsmeid?

# C04 Raadiovastuvõtuseadmed

## S01 Raadiovastuvõtja ehitus

---
***Kordamisküsimused***
* Millist seadet saab kasutada raadiolainete vastu võtmiseks?
* Milliseid laineid võtab vastu raadiovastuvõtja?
* Kuidas jõuab antenni juurde saabunud helisignaal vastuvõtjasse?
* Mis on vajalik raadiolainete vastuvõtuks?
* Mida kasutatakse vastuvõtja häälestamiseks soovitavale jaamale?
* Kuidas tekib operaatori poolt kuuldav signaal?
* Milliseid laineid kuuleb operaator kõrvaklappidest?
* Mida muudetakse transiiveri helivaljusregulaatori nupu keeramisel?
* Mis on kõrvaklappide kasutamise eeliseks vastuvõtul võrreldes valjuhääldiga?
## S06 S-meeter

---
***Kordamisküsimused***
* Mida näitab transiiveri S-meeter?
* Kuidas saab operaator hinnata signaali tugevust kui vastuvõtjal pole S-meetrit?

# C05 Raadiosaateseadmed

## S01 Raadiosaatja ehitus

---
***Kordamisküsimused***
* Millist seadet saab kasutada raadiosignaali saatmiseks?
* Mida on vaja omada telefonitööks ettenähtud raadiojaamas?
* Mis on mikrofoni otstarve?
* Mis on käsitelegraafivõtme otstarve?
* Mis juhtub transiiveri laineala häälestusnupu keeramisel?
## S02 Saatevõimsus

---
***Kordamisküsimused***
* Mida nimetatakse raadiosaatja võimsuseks?
* Kuidas muutub korrespondedi poolt vastu võetav signaal Kui raadiosaatja võimsust suurendada?
* Mida teete naabermajas oleva amatööriga jutu ajamiseks?
## S05 Raadiohäired

---
***Kordamisküsimused***
* Mis on saatjas kasutatavate ekraanide otstarve?
## S06 Saatja kontrollimine

---
***Kordamisküsimused***
* Mida teete Kui teile öeldakse, et Teie signaal on moonutatud?

# C06 Antennid ja fiidrid

## S01 Antennide omadused

---
***Kordamisküsimused***
* Miks on transiiverile vaja antenni?
* Milline allpooltoodud teguritest on antenni juures oluline?
* Millised on üldjuhul lühilaineantenni mõõtmed?
* Mida nimetatakse suundantenniks?
* Miks suundantenne tavaliselt pööratakse?
* Miks on raske valmistada antenni 160 meetri lainealale?
* Miks on raske valmistada ultralühilaineantenni?
* Miks ultralühilaineantenni ei saa kasutada lühilainealal?
## S02 Antenni ühendamine ja sobitamine

---
***Kordamisküsimused***
* Miks on antenni ja transiiveri vahel antennikaabel?
* Miks antenn lahutatakse äikese ajaks transiiverist?

# C07 Raadiolevi

## S01 Raadiolainete levimine

---
***Kordamisküsimused***
* Mis on raadiolevi?
* Mis teeb võimalikus lühilainete kauglevi?
* Kuidas on võimalik suurendada raadiolainete otsenähtavuse leviala?
## S02 Ionosfäär

---
***Kordamisküsimused***
* Mis mõjutab kõige rohkem Ionosfääri seisundit ja raadiolainete levi?
* Mille poolest on Ionosfäär raadiosides oluline?
* Milliseid jaamu saate saate 160 m ja 80 m lainealal päevasel ajal tõenäoliselt kuulda?
* Milliseid jaamu saate öisel ajal 10 m lainealal tõenäoliselt kuulda?
* Millise laineala peaksite valima kui soovite sellel ööpäev läbi kaugsidesid teha?
* Mis tingumustel on kauglevi ultralühilainetel võimalik?
## S03 Levihäired

---
***Kordamisküsimused***
* Milline mõju on päikeselt saabuvate osakeste tõttu tekkivatel magnettormidel?

# C08 Mõõtetehnika ja selle kasutamine

## S01 Mõõteseadmete kasutamine

---
***Kordamisküsimused***
* Mida tuleb jälgida mõõteriista kasutamisel?
* Kuidas mõõteriistu kontrollitakse?
* Mis on digitaalnäiduga mõõteriista eeliseks osutiga mõõteriista ees?
* Kas digitaalnäiduga mõõteriista näidu õigsust on vaja kontrollida?
* Millist tööriista kasutatakse antennielemendi pikkuse mõõtmiseks?
## S02 Tester

---
***Kordamisküsimused***
* Mida kasutate, et kontrollida kas elektrivõrgust saadav pinge on 230 volti?
* Mis on testri kasutamise põhieeliseks?
* Mida tuleb jälgida testriga elektrivõrgust saadava pinge mõõtmisel?
* Mida tuleb meeles pidada Testriga takistuse mõõtmisel?
## S06 Spektrianalüsaator

---
***Kordamisküsimused***
* Kas saatja poolt kiiratava raadiolainete pikkuse mõõtmiseks saab kasutada joonlauda?

# C09 Raadiohäired ja elektromagnetiline ühildatavus (EMC)

## S01 Raadiohäirete tekkepõhjused

---
***Kordamisküsimused***
* Milliseid raadiohäireid võib sidepidamine põhjustada?
* Mis võib olla häirete põhjuseks amatöörsides?
* Kas päike võib põhjustada atmosfäärihäireid?
* Kui raadiojaam asub suures linnas, siis kas see muudab olukorda raadiohäirete osas?
## S02 Raadiohäirete vähendamine

---
***Kordamisküsimused***
* Mida teete kui Teie naabrid kaebavad raadiojaama poolt põjustatud raadiohäireid?
* Mida teete kui Teie naabrid kaebavad raadiojaama poolt põhjustatud liiga suure võrgupinge üle?
* Mida tehakse teiste raadiojaamade poolt põhjustatud häirete kõrvaldamiseks?
* Mida teete kui Kui ultralühilainel hakkavad Teid segama kauged jaamad?

# C10 Ohutustehnika

## S01 Elektriohutus
Inimese keha juhib elektrivoolu. Kui inimene puudutab elektriseadme pinge all olevat osa
või isolatsioonirikke tõttu pinge alla sattunud osa, läbib tema keha vool. Seda voolu nimetatakse
rikkevooluks. Rikkevoolu suurus sõltub keha elektritakistusest ja voolu kulgemise teest läbi keha. 

Üldiselt loetakse inimesele ohutuks 10…20 mA voolu. Suurem vool kutsub esile lihaste krampe,
hingamishäireid ja halvemal juhul ka südamelihaste värelemise ehk fibrillatsiooni, mille tagajärjel võib
lakata vereringe ning aju verevarustus. Kui aju ei saa umbes 5 minutit verd, võib järgneda surm. 

Ohtlikkus sõltub voolu suurusest ja kestusest. Kõige ohtlikumaks peetakse voolu läbi parema käe ja
vasaku jala, sest see läbib südame piirkonda. Alla 10 mA voolu loetakse igal juhul ohutuks,
ükskõik kui kaua ta kestab. 50 mA vool loetakse juba ohtlikuks kui see
kestab kauem kui 1 sekund.

Tänapäeval on elektrikiplides rikkevoolukaitsed mis rakenduvad 10..30 mA
rikkevoolu juures mõnekümne millisekundiga, kaitstes suure tõenäosusega
inimest.

Vahelduvpinget alla 50 V sagedusel 50 Hz ja alalispinget alla 120 V loetakse
üldiselt ohutuks, sest keha läbiv vool ei kasva eluohtliku tasemeni.

Elektritöödel:

* Mõelge eelnevalt tehtavad tööd hoolega läbi. Kui Te täpselt ei tea, mida peate tegema, ärge kiirustage, vaid võtke järelemõtlemisaega või küsige nõu kelleltki teiselt.
* Varustage oma tööruum pealülitiga, mis võimaldab ühekorraga kõikjalt elektri välja lülitada. Andke sellest teada ka teistele, et nad oskaksid võimaliku õnnetuse korral reageerida.
* Kaitske elektrijuhtmeid ja –kaableid vigastuste eest: ärge pange nende peale asju või mööblit, ärge sikutage pistikut pesast juhetpidi välja. Juhtmed paigutage nii, et keegi neisse neile peale astuda, takerduda või komistada ei saaks. Kahjustatud kaabel asendage uuega.
* Maandage metallkastides olevad raadioseadmed, et vältida seadme korpuse pinge alla sattumist, kasutades selleks suure juhtmeristlõikega maanduskontuuri. Ärge ühendage maandusjuhet keskküteradiaatori või veetoru külge: see ei taga maandust, vaid teised inimesed võivad saada löögi!
* Ärge asendage sulanud kaitsmeid seadmetes või elektrikilbis traadi, naela või muu metallesemega: niimoodi võite ühel hetkel avastada, et kaitsme asemel sulab või läheb põlema midagi hoopis hinnalisemat.
* Eeldage alati, et vooluring on pinge all, kui kindlalt vastupidist ei saa tõestada. Pingetust kontrollige proovilambiga.
* Parandus- ja hooldustööde tegemisel lülitage aparatuur vooluvõrgust välja. Seejuures tühjendage ka alaldi filterkondensaatorid, sillates toiteallika mõnesaja-oomise takistiga.
* Kui mõõtetöid tuleb siiski teha pingestatud seadmeil, pidage meeles järgmist:
 - Enne mõõtma asumist kontrollige, et olete valinud õige mõõtepiirkonna.
 - Esmalt ühendage mõõteriista üldjuhe.
 - Seiske kuival alusel.
 - Kuivatage hoolikalt käed.
 - Ärge töötage üleskääritud käistega;
 - Sooritage ohtlikud operatsioonid ainult ühe käega. Nii on väiksem tõenäosus, et kätest moodustub vooluring läbi südame. Ärge lubage tööpaika kõrvalisi isikuid.

Seadmete akud või patareid:
 
* Hoidke töövalmis seade eemal lastest või ettevalmistuseta isikutest.
* Seadme puhastamisel või detailide vahetamisel eemaldage akud või patareid.
* Kõik patareid tuleb vahetada ühel ajal. Ärge kasutage segamini eritüübilisi või värskeid ja tühje patareisid.
* Jälgige, et akude ja patareide vahetamisel ühendate nad õigesti.
* Ärge kunagi lühistage akusid: see võib tekitada kõrge temperatuuri, lekke või plahvatuse;
* Ärge lammutage akusid lahti: elektrolüüt võib Teid söövitada.
* Kasutage ainult soovitatud tüüpi akulaadijat;
* Laadige akusid kuivas paigas, eemal radiaatoritest, puhuritest, ahjudest jms.
* Kasutage ainult soovitatud tüüpi akusid, et tagada nende ja laadimisseadme ühilduvus.
* Ärge kunagi proovige laadida primaarelemente: see võib lõppeda lekke või plahvatusega.


---
***Kordamisküsimused***
* Miks on vaja aparatuur maandada?
* Miks hoitakse töötades üks käsi selja taga, kui võib karta elektrilöögi saamist?
* Miks pinge all olevatest juhtmetest haaranud inimene ei suuda neist lahti lasta?
* Miks on oluline, et kogu raadiojaama elektrivarustust saaks välja lülitada ühekorraga ja kiiresti?
* Mida teete kui Teie kaaslane saab elektrilöögi ja kaotab teadvuse?
## S03 Jaama kasutamine

---
***Kordamisküsimused***
* Mida tuleb silmas pidada äikese ajal töötades?
* Mida tuleb silmas pidada, kui soovite reisilennukis amatöörsidet pidada?
## S04 Ohutus välitöödel
Kui töötate elektritööriistadega välitingimustes:

* Võrgutoite korral kasutage ainult topeltisolatsiooniga tööriistu, mis on märgistatud kahe teineteise sees asuva ruuduga:
* Kasutage lekkevoolukaitset;
* Lülitage nad sisse ainult vajaduse korral;
* Lülitage seade välja ja pange kaitseriivi, kui vahetate lõiketeri vms;
* Kasutage neid ainult siis, kui kõik kaitsevahendid on paigas. Lõiketerad või kiiresti liikuvad osad võivad sõrmed maha lõigata.
* Ärge jätke seadmeid järelevalveta, isegi kui lahkute ainult lühikeseks ajaks.
* Jälgige, et lapsed neid omapäi kasutada ei saaks.
* Ärge kasutage seadmeid märja ilmaga. Kui tööriist kukub vette, ärge hakake seda välja õngitsema, vaid kõigepealt eemaldage toitejuhe vooluallikast.
* Ärge kandke tööriistu juhtmeidpidi.
* Jälgige, et toitejuhe ei saaks viga, minnes vastu teravaid servi.

Lukksepatöödel:

* Veenduge enne töö alustamist, et tööriistad oleksid korras ja kindlalt pidemes;
* Kontrollige, et haamer oleks varrele kiilutud.
* Ärge kasutage “krooniga” meislit.
* Käia või ketaslõikurit kasutades kandke kaitseprille. Ärge käiake kinnastes.
* Puurimisel hoidke puuritavat eset mitte näppudega, vaid tangidega.
* Puurige lehtmaterjale erikujulise lõiketeraga vineeripuuridega.
* Ärge eemaldage pöörlevalt puurilt laastu.

Antennitöödel:

* Enne antennitöödele asumist mõelge hästi läbi, mida tegema hakkate. Kontrollige, kas vajalikud tööriistad ja materjalid on olemas. Kui Teile tundub, et midagi jääb arusaamatuks, ärge häbenege teistelt nõu küsida.
* Kui vähegi võimalik, ärge tehke antennitöid üksi. Kõik töötegijad peavad teadma, mis on nende ülesandeks. Valige endi seast töödejuhataja, kes jagab korraldusi ja leppige kokku märguannetes.
* Kasutage haarduva tallaga jalatseid. Riietus peaks olema mugav ja katma ka jäsemeid. Jälgige, et saapapaelad oleksid korralikult seotud ja et midagi teie küljest ei tolkneks.
* Külma ilmaga pange end võimalikult soojalt riidesse. Tuleb arvestada, et sageli tuleb pikka aega paigal püsida. Kontrollige, et Teil oleksid olemas kindad ja müts, pikk aluspesu ei tee ka paha.
* Vältige töötamist pimedas.
* Ärge tehke antennitöid, kui sajab lund või vihma ning on tugev tuul. Tööde tegemise ajal ärge mingil juhul kasutage antenni saatmiseks.
* Ärge kunagi töötage märjal või jäätunud katusel või tornis: sel juhul on isegi lamedal plekk-katusel raske püsti püsida.
* Trossiga töötamisel kasutage alati kindaid, et trossi kiud kätt ei vigastaks. Kindad olgu käes ka nööriga töötamisel, kui on oht, et nöör võib käes libisema hakata ja nahka põletada.
* Traadi, nööri või trossiga töötades ärge astuge selle keerdude sisse: Teid võidakse nende liikumahakkamisel kaasa haarata.
* Õppige selgeks enamkasutatavamad sõlmed: “umbsõlm” ei sobi enese julgestamiseks ja raskuste tõstmiseks
* Ärge kunagi paigutage antenni elektriliinide vahetusse lähedusse. Ärge kinnitage antenni elektripostide külge.
* Jälgige, et antenn jääks piisavale kõrgusele, et inimesed sinna otsa ei jookseks.
* Kui antenn hakkab kukkuma, siis laske tal minna, hoidke võimalikult kaugele ja hoiatage teisi. Kui Te üritate langevat antenni pidurdada, siis lisaks antenni purunemisele võite ka ise raskesti viga saada.

Töö mastis:

* Ärge minge masti tööle, kui sajab lund või vihma, või kui ligineb äike. Ärge töötage märjas või jäätunud tornis.
* Jälgige, et riietusel ei lotendaks ega ripuks.
* Kui temperatuur on alla –10 C, siis on parem masti otsa mitte minna. Alajahtunud ja külmast kangete liikmetega võib enese kinnihoidmine, rääkimata ronimisest, võimatu olla.
* Ronides kasutage alati julgestusvööd, isegi siis, kui ohtu ei tundu olevat. Enne ronimahakkamist katsetage julgestuse vastupidavust end poole meetri kõrguselt kukutades. Vöö ümberhaakimisel jälgige, et te oleksite kogu aeg masti külge kinnitatud.
* Ronimisel jälgige, et oleks alati vähemalt 3 toetuspunkti: kas 2 kätt ja üks jalg või 2 jalga ja üks käsi.
* Veenduge, et kõik tööriistad oleksid kaasas ja paigutatud nii, et ronimist ei segaks ega alla kukuks. Ärge hoidke ronimise ajal midagi käes.
* Mast all olijad peavad hoiduma väljapoole ala, kuhu ülevalt võivad kukkuda tööriistad või antenn ise. Juba meetri kõrguselt pähe kukkunud väike mutrivõti põhjustab suurt valu, kui ta tabab teid mitmekümne meetri kõrguselt, on tõenäosus üliraske trauma saamiseks väga suur.

---
***Kordamisküsimused***
* Miks antenn ei tohi olla elektriliinide vahetus läheduses?
* Mida tuleb silmas pidada, kui paigaldate antenni järsu kaldega jäätunud plekk-katusele?
* Mida teete kui katusele antenni paigaldades hakkab antenn kukkuma?
* Mida tuleb kindlasti kasutada antennimasti ronides?

# C11 Amatöörraadiojaama opereerimise reeglid ja protseduurid
* Säilitage alati viisakus, rahu ja hea tuju, sõltumata olukorrast. Kui see pole võimalik, siis ärge mine eetrisse.
* Ärge kunagi töötage amatööridele ettenähtud sagedusalast väljaspool.
* Ärge kunagi hõivake teistele tööliikidele ettenähtud sagedusi.
* Ärge segage kedagi meelega, ja ära pange tähele meelega segajaid: tähelepanu püüdmine ongi nende eesmärk.
* Saateaparatuuri häälestades kasutage fiktiivkoormust (dummy load). Kui see pole võimalik, siis veenduge, et sagedusel pole kedagi teist.
* Kutsumist alustades veenduge alati, et sagedusel kedagi poleks.
* Kui kaks jaama peavad omavahel sidet, siis oota kutsumisega seni, kuni side on lõppenud.
* Ärge kutsuge saatesagedusest erineval sagedusel kuulavat jaama tema saatesagedusel: ta ei kuule seda, niimoodi segate ainult teisi amatööre. Jälgige, et see sagedus, mille kutsumiseks valite, oleks vaba.
* Oluline info: raport, nimi ja QTH edastage esimese saatekorraga.
* Side jooksul edastage oma jaama ja korrespondendi kutsungit vähemalt iga 10 minuti tagant, kindlasti edastage kutsungid side lõpus.
* Saatmiste vahel katsuge võimalikult palju kuulata, seda eriti pile-up-is: sageli juhtub, et ihaldatav jaam kutsub ja kutsub jaama, kes ei kuule, kuna on pidevalt hõivatud oma kutsungi saatmisega.
* Vastates “lühikesi sidesid” pidavale korrespondendile, andke sama hulk infot, mis Teile antakse.
* Ärge mängige “eetripolitseinikku”, kes kõikvõimalikel põhjustel teisi amatööre hurjutab. Segage vahele ainult siis, kui seda on hädasti vaja, ja säilitage seejuures viisakus.
* Ärge rääkige liiga pikalt: korrespondent tahab ka midagi öelda. Halvemal juhul võib ta Teie monoloogi peale lahkunud olla.
* Proovige korrespondendiga rääkida ka millestki muust kui raadioamatörismist: niimoodi saate üksteist rohkem tundma.
* Aidake teisi amatööre, eriti uustulnukaid. Ärge naeruvääristage neid ja ärge virisege.

---
***Kordamisküsimused***
* Töötate sagedusel, kui keegi ütleb: “Oled loll”. Mida teete?
* Algaja amatöör on Teiega side pidamisel hädas. Mida teete?
* Kuulete telefonilainealal morsesignaali. Milline alljärgnevatest tegevustest on õige?
* Kuulete telegraafialal jaama, kes telefoni teel edastab CQ. Milline alljärgnevatest tegevustest on õige?
## S01 Veerimistabel
Telefoniside pidamisel ei piisa informatsiooni korrektseks edastamiseks
lihtsalt selle ette lugemisest. Indiast pärit korrespondent ei pruugi
näiteks nimest “Jaan” üldse aru saada, sama raske on eestlasel
aru saada nimest “Vishvanathan”. 

Seetõttu tuleb kutsungid, nimed ja muu teave tähthaaval edastada.
Üksikute häälikute edastamine, eriti kui sagedusel on häired,
on samuti problemaatiline, näiteks ei tee korrespondent SSB-side
puhul vahet, kas talle öeldi “ess” või “eff”.

Seetõttu on telefonisides kasutusele võetud veerimistabel, kus igale
tähele vastab teatud sõna, millest eetris on kergem aru saada kui
üksikust tähest. Nimi “Jaan” edastatakse niimoodi: “Juliet, Alfa, Alfa, November”.

Kasutusel on mitmed veerimistabelid. Inglise keele, aga ka teiste
keelte puhul on raadioamatööridele soovitatav rahvusvaheline veerimistabel.

Numbrid edastatakse nagu tavaliselt. Erandiks on “9”, mida võidakse hääldada
“niner”, et eristada teda “5”-st (five). “0” vasteks on “zero”, kirjapildis
tõmmatakse nullist läbi kriips (Ø), et teda eristada “o”-st.

Tuleks meeles pidada, et kõige kiiremini saab vajaliku info edastatud paraja
veerimiskiiruse korral: ülemäära kiirustades suudab saatja küll mõnevõrra
kiiremini info ettelugemisega hakkama saada, ajavõidu võib aga nullida
korrespondent, kes palub kõik otsast peale üle korrata.

Rahvusvaheline veerimistabel:
|Täht|Sõna|
|----|----|
|A| Alfa |
|B| Bravo |
|C| Charlie |
|D| Delta |
|E| Echo |
|F| Foxtrot |
|G| Golf |
|H| Hotel |
|I| India |
|J| Juliet |
|K| Kilo |
|L| Lima |
|M| Mike |
|N| November |
|O| Oscar |
|P| Papa |
|Q| Quebec |
|R| Romeo |
|S| Sierra|
|T| Tango |
|U| Uniform |
|V| Victor |
|W| Whisky |
|X| X-ray |
|Y| Yankee |
|Z| Zulu |

---
***Kordamisküsimused***
* Kuulete, kuidas sagedusel kutsuv jaam edastab oma kutsungit “EchoSierra-one-Alfa-Charlie”. Mida see teile ütleb?
## S04 Sidepidamise reeglid
Telefonisidele minnes:

* Lülitage transiiver sisse ja veenduge, et vastuvõtt toimib häireteta.
* Kui telefonisignaalid on loetamatud, kontrollige, kas olete õigel töörežiimil.
* Kontrollige, et asute lubatud sagedusalas.
* Kui hakkate kutsuma:
 - Valige vaba sagedus ja kuulake seda mõnda aega, veendudes, et keegi seal ei tööta.
 - Küsige mõned korrad: “Is this frequency in use?”, küsimuste vahel kuulates. Kui öeldakse, et sagedus on kasutusel, otsige teine sagedus.
 - Kui sagedus on vaba, hakake kutsuma CQ. Jälgige et Te ei kutsuks liiga kaua: piisab, kui edastada 3 korda CQ ja 3 korda oma kutsungit, korrates seda kõike veel ühe korra.
* Kui leiate kutsuva jaama:
 - kui jaam kuulab teisel sagedusel kui saadab, häälestage oma saatesagedus vastavaks;
 - oodake, kuni jaam on kutsumise lõpetanud; edastage oma kutsungit 1..2 korda.
* Vahetage korrespondendiga rutiinne teave: raport, nimi, QTH. “Lühikese side” puhul edastage ainult raport.
* Rääkige selgesti ja mõõduka kiirusega, eriti kui korrespondent on tundmatu. 
* Kiirustamisega võidetud aeg läheb kaduma, kui korrespondent edastatud infot korrata palub.
* Ärge kasutage telefonisides amatöörižargooni ja Q-koode üleliia: lihtsam on väljenduda “inimese moodi”.
* Katsuge aevastada ja köhida nii, et see ei satuks eetrisse.
* Edastage vähemalt iga 10 minuti tagant enese ja korrespondendi kutsungit.
* Kindlasti andke need edasi side alguses ja lõpus.
* Kui jututeema otsa saab, lõpetage viisakalt side. Ärge hüvastijättu liiga pikaks venitage.
* Pärast side lõppu ärge hakake kohe saatma, vaid kuulatage, kas keegi kutsub.

---
***Kordamisküsimused***
* Te kuulete Soome jaama kutsumas “CQ DX”. Mida teete pärast kutsumise lõppu?
* Teie CQ-le vastanud jaam edastas oma kutsungi liiga kiiresti, nii et Te ei suutnud seda vastu võtta. Mida teete?
* Töötate sagedusel, kui keegi küsib: “Kas sagedus on hõivatud?”. Mida teete?
* Töötate sagedusel, kui Saksa jaam hakkab küsimata kutsuma “CQ DX”. Mida teete?
* Küsite sagedusel: “Kas sagedus on hõivatud?” ja saate jaatava vastuse. Mida teete?
## S05 Side ajal edastatav info
Selleks, et side toimuks, on korrespondentidel vaja vahetada kutsungid ja RST-raport.
Viimane on numbrikombinatsioon, mis iseloomustab vastuvõetud signaali loetavust
(R=readability, 5-palli skaala), tugevust (S=strength, 9-palli skaala) ja
tooni (T=tone, 9-palli skaala).

Telefoniside puhul jäetakse raporti T-osa ära ja raport on kahekohaline.

DX-peditsioonidel ja võistlustel kasutatakse aja kokkuhoiuks raportina tavaliselt
ainult 599 või 59, vaatamata tegelikule signaalile. Kui saadud raporti R- või 
T-osa on korduvalt maksimaalsest väiksemad, tuleks kontrollida aparatuuri
korrasolekut, sest tavaliselt kipuvad raportid olema paremad kui tegelik
signaal, loetavuse ja tooni  hinde alandamiseks peab olema tõsisem põhjus.

### RST skaala

R (loetavus)
1. Loetamatu
2. Vaevalt loetav
3. Raskesti loetav
4. Raskusteta loetav
5. Selgesti loetav

S (tugevus):
1. Vaevalt kuuldav
2. Väga nõrk signaal
3. Nõrk signaal
4. Pingutusega kuuldav signaal
5. Rahuldava kuuldetugevusega signaal
6. Mugava kuuldetugevusega signaal
7. Mõõdukalt tugev signaal
8. Tugev signaal
9. Väga tugev signaal

T (toon):
1. Väga toorelt urisev
2. Ebamusikaalne vahelduvvoolutoon
3. Vahelduvvoolutoon
4. Keskmiselt musikaalne vahelduvvoolutoon
5. Musikaalne vahelduvvoolutoon
6. Vahelduvvooluga märgatavalt moduleeritud toon
7. Nõrga vahelduvvoolumodulatsiooniga toon
8. Peaaegu modulatsioonita toon
9. Eeskujulik moduleerimata toon
                                                    
Iga tugevuse aste vastab kahekordsele signaali intensiivsuse suurenemisele.
Signaali tugevuseks võib olla ka üle 9 palli: sellisel juhul väljendatakse
seda “9+” või S-meetrilt üheksat palli ületava detsibellide arvuna (“9+20”).

Lisaks kohustuslikule edastatakse ka täiendavat teavet:
Operaatori nimi; Jaama QTH (asukoht); Kasutatav aparatuur; Ilm; QSL-info.
---
***Kordamisküsimused***
* Kolm sidet järjest on korrespondendid andnud raportiks 39. Mida teete?
* Teile on kolm Jaapani korrespondenti järjest andnud raportiks 59. See tähendab, et:

# C12 Amatöörraadioside siseriiklik ja rahvusvaheline õiguslik regulatsioon

## S01 Raadioamatörism

---
***Kordamisküsimused***
* Mida tähendab lühend ERAÜ?
* Kes saavad olla ERAÜ liikmeteks?
## S02 Raadioamatööride kutsungid
Igal raadioamatööril on tähtedest ja numbri(te)st koosnev kutsung, mis on maailmas ainuke ja on talle teise nime eest.

Tõsi, riikides, kus amatööre on palju, lastakse juba kasutusel olnud kutsungid mõne aja pärast uuesti käiku.

Iga kutsungi esimene osa ehk prefiks näitab, millisest riigist amatöör töötab. Eesti amatööride kutsungid
algavad tähekombinatsiooniga “ES”, sellele järgnev number näitab, millisest Eesti piirkonnaga on tegemist.

* ES1 Tallinn
* ES2 Harjumaa
* ES3 Rapla- ja Läänemaa
* ES4 Ida-Virumaa ja Lääne-Virumaa
* ES5 Tartu- ja Jõgevamaa
* ES6 Põlva-, Võru- ja Valgamaa
* ES7 Viljandimaa
* ES8 Pärnumaa
* ES9 ERAÜ erikutsung
* ES0 Saare ja Hiiu maakond

Viimane osa ehk sufiks annab Eesti jaamade puhul informatsiooni raadioamatööri kvalifikatsioonist ja jaama otstarbest.

Üldreegliks on: mida lühem kutsung, seda parem operaator. Kutsungi lühenemisega kahaneb
ka võimalike kutsungite arv, ka kõige parema tahtmise juures pole võimalik kõigile Eesti
amatööridele väljastada ühetähelise sufiksiga kutsungeid.

Päris algajate, D-klassi amatööride kutsungi sufiksis on neli tähte. Edasijõudnute, B-klassi amatööride kutsungis
on pärast numbrit kolm tähte. Kaks tähte on sufiksis A-klassi amatööridel ja klubijaamadel. 
Viimastel on võimalik TTJA-lt taotleda ka ühetähelist sufiksit.

Kui amatöör ei tööta oma tavalises asukohas, saab seda näidata kaldjoonega (ingl. k. “stroke” või “slash”)
eraldatud kutsungi lisa abil:

* ES4LB/6 jaam töötab ajutisest asukohast teises kutsungipiirkonnas
* ES5RY/p jaam töötab ajutisest asukohast samas kutsungipiirkonnas (“portable”)
* ES5MG/m jaam töötab autolt (“mobile”)
* ES0IC/mm jaam töötab merelt (“maritime mobile”)
* ES5PC/am jaam töötab lennukilt (“aeroplane mobile”)

Kui välismaa amatöör tuleb lühiajaliselt Eestisse, lisatakse tema kutsungi ette “ES”+kutsungipiirkond + “/”. 
Näiteks Timo, OH1NOA, töötades Lõuna-Eestist, võtab kutsungiks ES6/OH1NOA. Pikemaajalisel peatumisel
(üle kuue kuu) peab amatöör taotlema Eesti kutsungit.

---
***Kordamisküsimused***
* Kuidas ära tunda eetris töötavat Eesti D-klassi amatööri?
* Kuidas ära tunda eetris töötavat Eesti A-klassi amatööri?
* Mis näitab, et eetris töötab alaealine?
* Mida näitab raadioamatööri poolt kasutav kutsung ES9B?
* Te kuulete kutsumas jaama kutsungiga ES5/DJ0IB. Mid see tähendab?
* Te kuulete kutsumas jaama kutsungiga ES5JR/6. Mida see tähendab?
* Te kuulete kutsumas jaama kutsungiga ES5YL/M. Mida see tähendab?
## S03 Seadusandlus

---
***Kordamisküsimused***
* Millistele tingimustele peab vastama raadioamatöör?
* Miks raadioamatöörid sooritavad kvalifikatsioonieksami?
* Mida peab raadioamatöör tegema kutsungi saamiseks?
* Kes annab välja raadiojaama tööloa ja kutsungi?
* Miks D-klassi amatöörid ei tohi töötada amatöörlainealast väljaspool?
* Milleks amatöörsidet ei tohi kasutada?
* Mida peab raadioamatöör silmas pidama, kui ta soovib eetris edastada muusikat?
* Mida saab D-klassi amatöör teha töötades klubijaamast?
* Kui suurt saatevõimsust võib kasutada raadioamatöör?

