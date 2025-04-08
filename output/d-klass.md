# Raadioamatööri õppematerjal
# D-kategooria
Madis Kaal <mast@nomad.ee> 2025

Käesolev dokument on kogu erinevatest allikatest kokku korjatud
materjalidest ning ERAÜ raadioamatööri kvalifikatsioonieksamil
esitatavatest küsimustest. Dokument on programselt kokku pandud
andmekogust mis sisaldab nii õppematerjali kui küsimusi.

Sellise uue andmekogu loomise eesmärke on mitu:

1. Küsimuste süstematisserimine, korrastamine ja sünkroniseerimine erinevate
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

---
***Kordamisküsimused***
* Milleks kasutatakse takisteid?
## S02 Aktiivkomponendid

---
***Kordamisküsimused***
* Mis on pooljuhi põhiomadus?
* Mida saab öelda raadiolampide kohta?
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

## S01 

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

---
***Kordamisküsimused***
* Miks antenn ei tohi olla elektriliinide vahetus läheduses?
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

---
***Kordamisküsimused***
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

