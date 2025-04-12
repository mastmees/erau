# Raadioamatööri õppematerjal
# B-kategooria
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
* Mida tähendab termin impedants?
* Milline on reaktiivtakistuse mõõtühik?
* Milline on impedantsi mõõtühik?
## S03 Oomi seadus
Oomi seadus määrab kindlaks pinge U, voolutugevuse I ja takistuse R vahelise seose:

U=I*R või I=U/R või R=U*I

I on ahelaosa läbiva voolu tugevus, mida mõõdetakse amprites (A);
U on pinge, mida mõõdetakse voltides (V);
R on vooluahela lõigu takistus, mida mõõdetakse oomides (Ω).

Vahelduvvoolu korral kehtib seos

I=U/Z

kus Z on vahelduvvooluahela näivtakistus.

Oomi seadusega on lähedalt seotud võimsus, mida saab arvutada:

P = U * I = I * I * R = U * U * R

---
***Kordamisküsimused***
* Kui suur on kasutatav võimsus kui 400 V pingega vooluallikas ühendatakse 800 oomise koormusega?
* Kui suur on 12 V 0,2 A vooluga indikaatorlambi võimsus?
* Kui suur võimsus eraldub 100 oomisel takistil, kui tema jalgadel mõõdetud pinge on 5 V?
## S04 Detsibellid
Detsibell (tähis dB) on kümnendlogaritmiline mõõtühik, mis väljendab kahe füüsikalise
suuruse (sageli võimsuse või pinge) suhet või ühe suuruse taset võrreldes mingi
võrdlus- ehk baassuurusega. Detsibell on Belli osaühik, 1B = 10 dB.

Kuna väljendatakse kahe suuruse suhet, mille ühikud on samad, siis on detsibell
dimensioonita suurus. Detsibellides mõõdetakse näiteks helirõhutaset, elektrisignaali
võimendust või nõrgendust jms.

Selle ühiku eeliseks on väga suurte ja väga väikeste suhtarvude lihtne esitamine,
mille tingib logaritmiline skaala. See lubab meil näiteks väga suurt ja väga väikest
signaalitasemete suhet kergesti ja arusaadavalt kirjeldada tülikalt pikki arve kasutamata.

Bellide arvutusvalemid on erisugused olenevalt sellest, kas on tegemist energiasuurustega
näiteks energia, võimsus, heliintensiivsus, või väljasuurustega
(amplituudidega), näiteks elektrivälja tugevus, elektripinge, voolutugevus, helirõhk.

Energiaühikute korral korral on N (dB) = 10 * lg ( P1/P2) ja väljaühikute
korral on N (dB) = 20 * lg (F1/F2) kus P1 või F1 on ette määratud
baasväärtus.

Mõned sagedasti kasutatavad dB väärtused:

| dB | Võimsuste suhe | Amplituudide suhe |
|----|----------------|-------------------|
| 60 | 1000000 | 1000 |
| 40 | 10000 | 100 |
| 20 | 100 | 10 |
| 10 | 10  | 3,162 |
| 6 | 3.981 ≈ 4 | 1,995 ≈ 2 |
| 0 | 1 | 1 |
| -3 | 0,501 ≈ 1⁄2 | 0,708 |
| −6 | 0,251 ≈ 1⁄4 | 0,501 ≈ 1⁄2 |
| −10 |	0,1 | 0,3162 |
| −20| 0,01 | 0,1 |
| −40 |	0,0001| 0,01 |
|−60 | 0,000001|0,001 |

Näiteks -3 dB signaalikadu koaksiaalkaablis tähendab, et pool saatja
väljundvõimsusest läheb kaablis kaduma. Saatevõimsuse kümnekordistamine
tähendab +10dB muutust, aga +20dB muutus tähendab juba saatevõimsuse
sajakordistamist. 

Vastuvõtjate S-meetri skaalal tähendab üldiselt iga samm 6dB muutust,
ehk siis S8-lt S9-le minek tähendab võimsuse neljakordistumist või antennist
tulev signaali pinge kahekordistumist.

1 dB on väikseim helitugevuse muutus, mida kõrv eristada suudab. See on võimalik
ainult ideaalsetes tingimustes, kui inimene kuulab keskmisel muutumatul
sagedusel "puhast" tooni ja tema ümber ei ole teisi mürasid. On kokku lepitud,
et normaalsetes tingimustes saab terve kõrv vaevu aru 3-detsibellisest helimuutusest.

Detsibelli tähisele lisatakse sufikseid (järelliiteid), selleks et viidata baastasemele,
millega mõõdetud väärtust võrreldakse.

Elektrotehnikas kasutatav dBm (dBmW) väljendab signaali võimendust või nõrgendust
1millivati suhtes, mis on baasväärtus ehk nullnivoo (0 dB). Seega kui öeldakse, et
signaali tugevus on ‒63 dBm, siis on see sama, kui öelda, et see signaal on 63 detsibelli
võrra nõrgem kui 1-millivatine signaal. Kui öeldakse, et saatja
väljundvõimsus on 40 dBm siis see tähendab, et väljundvõimsus on 10000 mW
ehk 10W.

Stuudiotehnikas on tuntud tähis dBu – signaalipinge suhe 0,775 voldi suhtes,
koduses audiotehnikas on kasutusel dBV - signaalipinge suhe 1 voldi suhtes.

---
***Kordamisküsimused***
* Mis on Bell?
* Mis on detsibell?
* Ligikaudu mitu detsibelli on vaevaltmärgatav helitugevuse muutus?
* Kui suur on Võimsuse suurenemine kaks korda detsibellides?
* Mitu korda suureneb võimsus 6 dB puhul?
* Mitu korda suureneb võimsus 3 dB puhul?
* Signaali raport on ”10 dB üle S9”.Kui saatja võimsust vähendatakse 1500 vatilt 150 vatini kui suur on uus signaali tugevuse raport?
* Signaali raport on “20 dB üle S9”.Kui saatja võimsust vähendatakse 1500 vatilt 15 vatini kui suur on uus signaali tugevuse raport?

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
* Kuidas mõjub ümbruskonna temperatuur süsiniktakisti takistusele?
* Mis tüüpi kondensaatorit kasutatakse tihti võrgutoitealaldi silumisfiltris?
* Millised kondensaatorid lülitatakse rööbiti transformaatori sekundaarmähisega pingeimpulsside vähendamiseks?
* Mis tekitab poolide omaresonantsi?
## S02 Aktiivkomponendid

---
***Kordamisküsimused***
* Mis on toiteseadme alalduselemendi vastupinge?
* Millist dioodi parameetrit ei tohi ületada?
* Miks peavad alaldi dioodid olema termaalselt kaitstud?
* Mis on Zener dioodi (stabilitroni) peamine omadus?
* Mis tüüpi diood on võimeline ostsilleerima ja ka võimendama?
* Mis on varikapi peamine omadus?
* Milleks kasutatakse PIN dioodi?
## S03 Transformaatorid

---
***Kordamisküsimused***
* Milline vooluringi komponent võimaldab suurendada vahelduvvoolu pinget 100 voldilt 1000 voldini?
* Kuidas nimetatakse transformaatori primaarmähises voolavat voolu, kui sekundaarmähise külge pole koormust lülitatud?
* Mis suurustega iseloomustatakse tavaliselt jõutransformaatori primaar- ja sekundaarmähiseid?
* Kui suur on pinge transformaatori 500 keerust koosneva sekundaarmähise klemmidel, kui 2200 keerust koosnev primaarmähis on lülitatud 220 V vahelduvvooluvõrku?
## S05 Raadiolambid

---
***Kordamisküsimused***
* Miks on mõningates lampvõimendites vajalik neutralisatsioon?

# C03 Raadio- ja elektrotehnika ahelad

## S01 Alalis- ja vahelduvpinge

---
***Kordamisküsimused***
* Kuidas nimetatakse mahtuvust ja induktiivsust sisaldava vooluringi poolt vahelduvvoolule osutatavat takistust?
* Kuidas nimetatakse induktiivsuse poolt vahelduvvoolule osutatavat takistust?
* Kuidas nimetatakse mahtuvuse poolt vahelduvvoolule osutatavat takistust?
* Kuidas reageerib induktiivsus vahelduvvoolule?
* Kuidas reageerib mahtuvus vahelduvvoolule?
## S02 Paralleel- ja jadaühendused

---
***Kordamisküsimused***
* Kui 1 amprilise vooluallikaga on ühendatud kaks paralleelselt lülitatud 10 oomist takistit kui suur vool läbib kumbagi takistit?
* Kui suur on mitmest takistist koosneva jadalülituse kogutakistus?
* Kui suur on kahe võrdse paralleelselt lülitatud takistist koosneva ahela kogutakistus?
* Kui suur on kahe paralleelselt ühendatud induktiivsuse koguväärtus?
* Kui suur on kahe paralleelselt lülitatud kondensaatori kogumahtuvus?
## S03 Toiteahelad

---
***Kordamisküsimused***
* Miks ühendatakse toitealaldi dioodidega paralleelselt kondensaator ja takisti?
* Milline on täislaine alaldi väljundpinge filtreerimata kuju?
* Millised komponendid moodustavad toitealaldi filtri?
* Milline peab olema ühefaasilise sildalaldi alaldusdioodi vastupinge suurus?
* Milline peab olema silumiskondensaatoriga poolperioodalaldi alaldusdioodi väikseim vastupinge?
* Kuhu ühendatakse toitealaldi šunttakisti?
* Mitu kraadi siinuslainest kasutab poolperioodalaldi?
* Mitu kraadi siinuslainest kasutab täisperioodalaldi?
* Mis funktsiooni täidavad kõrgepingealaldis dioodidega paralleelselt lülitatud kondensaatorid ja takistid?
* Miks kasutatakse raadiosaatja kõrgepingealaldis šunttakistit?
## S05 Sobitusahelad

---
***Kordamisküsimused***
* Milline peab olema transmissiooniliiniga ühendatud madalpääsfiltri impedants liini impedantsiga võrreldes?
* Millal annab toiteallikas maksimaalse väljundenergia?
* Mida tähendab termin impedantside sobitamine?
* Mis juhtub kui elektrilise koormuse impedants on võrdne toiteallika impedantsiga?
* Miks on impedantside sobitamine raadiotehnikas väga oluline?
* Kui suur on 200 oomise väljundtakistusega helisagedusvõimendi sobitamiseks 10 oomise valjuhääldiga vajaliku transformaatori mähiste keerdude suhe?

# C04 Raadiovastuvõtuseadmed

## S01 Raadiovastuvõtja ehitus

---
***Kordamisküsimused***
* Mida nimetatakse segustusprotsessiks?
* Mis eelised on sagedusmuundusprotsessil?
* Millised kaks faktorit määratlevad vastuvõtja tundlikkuse?
## S02 Kõrgsagedusvõimendi

---
***Kordamisküsimused***
* Miks on kasulik omada vastuvõtja sisendis attenuaatorit?
* Mis on vastuvõtja kõrgsagedusvõimendi esmane ülesanne?
## S03 Seguaste

---
***Kordamisküsimused***
* Millised on põhilised seguastme väljundis esinevad sagedused?
* Mis vastuvõtjas juhtub kui väga tugev signaal jõuab seguastmeni?
## S04 Vahesagedus

---
***Kordamisküsimused***
* Mis on vahesagedusvõimendi?
* Kui suur on SSB telefonitööks vajaliku hea kvartsfiltri pääsuriba laius?
## S05 Detektor

---
***Kordamisküsimused***
* Mis on produkt-detektor?
* Mida nimetatakse detekteerimiseks?
* Mis on sagedusdiskriminaator?
* Mida kasutatakse FM signaali detekteerimiseks?
## S06 S-meeter

---
***Kordamisküsimused***
* Kui palju tuleb suurendada saatja väljundvõimsusust, et saatja läheduses asuva vastuvõtja S-meetri näit suureneks S8-lt S9-ni ?

# C05 Raadiosaateseadmed

## S01 Raadiosaatja ehitus

---
***Kordamisküsimused***
* Mida on vaja omada telefonitööks ettenähtud amatöörraadiojaamas?
## S05 Raadiohäired

---
***Kordamisküsimused***
* Mis tüüpi filter tuleb installeerida amatöörsaatjasse harmooniliste sageduste kiirguse vältimiseks?
* Monteerisite oma autosse VHF või UHF FM raadiojaama. Milline on antenni jaoks parim koht vältimaks juhi ja reisijate ülikõrgsagedusliku kiirituse ohtu?
* Mis on saatjas kasutatavate ekraanide otstarve?
* Miks kasutatakse nn. pii-filtrit saatja väljundis?
## S06 Saatja kontrollimine

---
***Kordamisküsimused***
* Mis tüüpi sisendsignaali kasutatakse SSB saatja lineaarsuse kontrollimiseks?
* Mida saab kontrollida kahe tooni testi abil?
* Milliseid kaht helisagedust võib kasutada SSB telefonisaatja lineaarsuse kontrollimiseks?
* Kuidas saab raadiojaama häälestamisel eetrisoleku aega viia miinimumini?

# C06 Antennid ja fiidrid

## S01 Antennide omadused

---
***Kordamisküsimused***
* Miks kasutatakse sagedasti Yagi antenni 50 MHz sagedusalal?
* Kuidas saab suurendada parasiitelementidega suundantenni sagedusriba laiust?
* Kui suur on dipoolantenni võimendus võrreldes isotroopse kiirgajaga?
* Mida tähendab termin ette-taha suhe?
## S02 Antenni ühendamine ja sobitamine

---
***Kordamisküsimused***
* Milline meetod on parim ebasümmeetrilise koaksiaalkaabli sobitamiseks Yagi antenniga?
* Kui suur on sobitatud ja resonantsis oleva poollaine dipoolantenni toitepunkti impedants vabas ruumis?
* Miks vahel mähitakse antenni koaksiaalkaabel umbes 10-keeruliseks pooliks?
* Mis ühikutes väljendatakse kõrgsagedusliku toiteliini kadusid?
* Mis juhtub dielektrikus kadudega toiteliinis töösageduse suurenemisel?
* Kuidas mõjutab koaksiaalkaablit läbiva signaali sageduse suurenemine sumbuvust?

# C07 Raadiolevi

## S02 Ionosfäär

---
***Kordamisküsimused***
* Milline raadiolainete levimehhanism võimaldab saadet vastu võtta pinnalaine ulatusest kaugemal kuid lähemal ionosfäärist peegeldunud lainest?
* Mis on raadiolainete levi kriitiline nurk?
* Soovite suvise päeva õhtupoolikul sidet saada amatööriga, kes asub teist ligikaudu 2000 km eemal. Milline laineala sobiks edukaks sidepidamiseks kõige rohkem?
## S03 Levihäired

---
***Kordamisküsimused***
* Mis iseloomustab nn. “backscatter” signaale?
* Mis on päikesevoog (solar flux)?
* Mida nimetatakse geomagnetiliseks häireks?
* Kui kiiresti jõuab Päikeselt kiirguv laetud osakeste vool Maale?
* Millises ionosfääri kihis kutsuvad äkilised ionosfääri häired esile raadiolainete suurenenud sumbuvuse?
* Kuidas mõjutab geomagnetiline torm raadiolainete levi?
* Kui kaua tavaliselt kestavad ootamatud ionosfääri häired?
* Millistel laiuskraadidel esineb tavaliselt rohkem geomagnetilisi häireid?

# C08 Mõõtetehnika ja selle kasutamine

## S03 Ostsilloskoop

---
***Kordamisküsimused***
* Milline mõõteriist sisaldab horisontaal- ja vertikaalkanali võimendit?
* Mis tüüpi signaale on võimalik ostsilloskoobi abil vaadelda?
* Mis seade on ostsilloskoop?
* Mis võib põhjustada ostsilloskoobi kineskoobi luminofoori riknemise?
## S04 Väljatugevuse mõõtja

---
***Kordamisküsimused***
* Mis seade on väljatugevuse mõõtja?
* Milline on kõige sobivam lihtne instrument antenni kiirguse suunadiagrammi määramiseks horisontaaltasapinnas?
## S05 Mürasild

---
***Kordamisküsimused***
* Mis seade on antenni mürasild?
* Kuhu ühendatakse antenni mürasild?
## S06 Spektrianalüsaator

---
***Kordamisküsimused***
* Millist seadet saab kasutada saatja väljundsignaalis esinevate intermodulatsioonimoonutustes tekitatud parasiitsignaalide uurimiseks?

# C09 Raadiohäired ja elektromagnetiline ühildatavus (EMC)

## S01 Raadiohäirete tekkepõhjused

---
***Kordamisküsimused***
* Mis on atmosfääriliste raadiohäirete peamine tekkepõhjus?
* Mis tüüpi interferentshäireid võib kiirata mitmebandi antenn, mis on ühendatud valesti häälestatud raadiojaama väljundisse?
* Mida tähendab väljend "harmooniliste kiirgus" ?
## S02 Raadiohäirete vähendamine

---
***Kordamisküsimused***
* Kuidas on võimalik kindlaks teha, kas raadiohäireid tekitav elektriliin asub teie majas?
* Kuidas on võimalik vähendada auto elektrigeneraatori poolt tekitatavaid raadiohäireid?
* Kuidas saab vähendada väga tugeva signaali toimel vastuvõtjas tekkivaid intermodulatsioonihäireid?
* Teie naaber teatab, et tekitate häireid televisioonivastuvõtule. Teie olete aga kindel, et teie aparatuur töötab korralikult. Mida peate tegema?
* Mis tüüpi filter tuleb kõigepealt paigaldada amatöörraadiojaama harmooniliste sageduste kiirguse vältimiseks?
* Milline filter tuleb paigutada televiisori sisendisse esmase abinõuna amatöörraadiojaama poolt tekitatud kõrgsagedusliku ülekoormuse vähendamiseks?

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
* Kui suur võib maksimaalselt olla inimkeha läbiv vahelduvvool, mis endast ei kujuta veel ohtu?
* Mida tuleb teha kõigepealt kui näed voolujuhtmetesse kinnijäänud inimest?
## S02 Raadiokiirgus


Elektromagnetkiirguse energia neeldumisel eluskoes tekib soojus. Kui organismi soojusregulatsioon
ei suuda enam kompenseerida kiirguse neeldumisel kehas tekitatavat soojust, hakkab keha
temperatuur tõusma ja põhjustada vigastusi rakkudes. Silmad võivad muudest kudedest kergemini
kahjustada saada, sest silmade vereringe ei võimalda organismil temperatuuri reguleerimist.
Sageduse tõusuga suureneb ka energia neeldumine koes ja soojusteke, seesama mehhanism
võimaldab mikrolaineahjude toimimise.

Kõrgendatud elektromagnetväljas viibimine võib pikema aja möödudes mõjutada inimese organismi
ka muul moel, on märgatud üleväsimust, iiveldust, peavalu. Väga suurte
väljatugevuste korral on võimalikud südame- ja ajuhäired, samuti ka kesknärvisüsteemi
häired. Pikaajaline kiirgus võib mõjutada inimese psüühikat.

Selleks, et end kiirguse eest kaitsta on kõige lihtsam mitte olla pikalt
seal kus kiirgustase on kõige suurem, näiteks saateantenni juures mida
kasutatakse suure võimsusega saatja küljes. Kindlasti tasub hoolitseda
selle eest, et kasutatavates seadmetes oleks kõik varjestusekraanid paigas
ja korralikult kinnitatud. Autos paikneva saatja küljes olevast antennist
lähtuva kiirguse eest saab end varjestada paigutades antenni auto
katusele, sellisel juhul töötab katus mingil määral varjestusekraanina.

---
***Kordamisküsimused***
* Milline inimese keha organ on kõige tundlikum kõrgsagedusliku energia poolt põhjustatud kudede kuumenemise suhtes?
* Tugev kõrgsagedusenergia kiirgus võib olenevalt lainepikkusest, kõrgsagedusvälja intensiivsusest ja muudest teguritest rikkuda inimkeha kudesid. Kuidas mõjub kiirgus keha kudedele?
* Kui tahad teha mõningaid häälestusoperatsioone oma VHF/UHF raadiojaama juures, mida peab tegema enne jaama sisselülitamist?
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
* Mida peab silmas pidama, kui taod antennimasti tõmmitsate kinnitusvaiu maasse?
* Mida tuleb jälgida raiudes puid välipäeva või kokkutuleku lõkke jaoks?
* Mida tuleb silmas pidada antennimasti püstitamisel või antenni vedamisel majade vahele?
* Mida tuleb jälgida tehes tööd kõrgel antennimasti otsas?
* Mida peab silmas pidama kui oled autoga sõitnud välipäevale?

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
* Kuidas tuleb veerimistabeli abil saata kutsung ES9A ?
* Kuidas veeritakse kutsungit AE0LQY ?
## S02 Q-kood
Q-koodil on veerimistabelile vastupidine eesmärk: see on välja töötatud selleks,
et mõne tähe abil edastada teavet, mis sõnades väljaöelduna läheks liiga pikaks,
seda eriti telegraafiside puhul. Tunduvalt lihtsam on telegraafis edastada
"PSE QSY 14250" kui "PSE CHANGE UR FREQ TO 14250" 

Samas ei tasu harvaesinevaid Q-koode pruukida telefonisides: ajavõidu asemel
Te hoopis kaotate aega, kuna korrespondent peab mõistatama, mida öelda taheti.
Q-koodi saab esitada nii küsimusena kui ka vastusena. Esimesel juhul lisatakse
lõppu küsimärk, telefonisides tõstetakse hääletooni.

|Lühend|Küsimus (selgitus)|Vastus (selgitus)|
|------|------------------|-----------------|
| QRL  | Kas olete hõivatud? (või) Kas sagedus on hõivatud? | Olen hõivatud. (või) Sagedus on hõivatud, palun ärge segage. |
| QRM  | Kas teid segatakse? Kas esineb häireid? | Mind segatakse. |
| QRN  | Kas teil esineb staatilisi häireid ? | Siin on staatilisi häireid.  |
| QRO  | Kas ma peaksin suurendama saatevõimsust? | Suurendage saatevõimsust. |
| QRP  | Kas ma peaksin vähendama saatevõimsust? | Vähendage saatevõimsust. |
| QRQ  | Kas ma peaksin edastama kiiremini (telegraaf)? | Edastage kiiremini. |
| QRS  | Kas ma peaksin edastama aeglasemalt ? | Edastage aeglasemalt |
| QRT  | Kas ma peaksin saate lõpetama ? | Lõpetage saade. |
| QRX  | Millal te mind uuesti kutsute ? (kasutatakse ka lühikese pausi alguses) | Kutsun teid hiljem uuesti.|
| QRZ  | Kas keegi kutsub mind ? | Teid kutsub ... (kutsung) sagedusel ... kHz (MHz).|
| QSB  | Kas minu (jaama) signaali tugevus kõigub ? | Teie (jaama) signaali tugevus kõigub. |
| QSL  | Kas kinnitate info vastuvõttu ? (kasutatakse ka sidet kinnitava kaardi nimetusena) | Kinnitan info vastuvõttu. |
| QSO  | Kas teil on otseühendus ... (kutsung) jaamaga või saate temaga ühendust läbi vahendusjaama ? | Mul on otseühendus ... (kutsung) jaamaga - kasutan vahendusjaama. (kasutatakse ka sõnade "side" ja "ühendus" asemel) |
| QSY  | Kas ma peaksin vahetama töösagedust ? | Vahetage töösagedust. |
| QTH  | Milline on teie asukoht ? | Minu asukoht on ... (asukoht või muud asukohta määravad andmed). |

Täielik Q-koodide nimekiri http://www.kloth.net/radio/qcodes.php


---
***Kordamisküsimused***
* Mida tähendab "CQ" ?
* Mida tähendab lühend QRS ?
* Mida tähendab lühend QTH ?
* Mida tähendab lühend QSL?
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
* Mis on kõige olulisem tegur kutsesageduse valikul teil kasutada lubatud sagedusalal?
* Kuulete oma sagedusel Haiitis toimunud maavärina päästjate teabevahetust. Mida teete?
* Milline on standardse telefoniväljakutse formaat?
* Kuidas te vastate raadiotelefoni väljakutsele?
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
* Mida tähendab R RST signaali raportis?

# C12 Amatöörraadioside siseriiklik ja rahvusvaheline õiguslik regulatsioon

## S01 Raadioamatörism

---
***Kordamisküsimused***
* Mida loetakse amatöörraadiojaamaks?
* Mis kuulub Amatöörraadiojaama tehniliste seadmete kogumikku?
* Mida loetakse Amatöör-vahendusraadiojaamaks?
* Mida loetakse Amatöörraadiomajakaks?
* Mida loetakse Ühiskasutusega amatöörraadiojaamaks?
* Mida loetakse Amatöörraadiojaama registreeritud asukohaks?
* Mida loetakse Amatöörraadiosideks?
* Kuidas tohib kasutada Amatöörraadiosidet?
* Keda loetakse Raadioamatööriks?
* Mille alusel tohib Amatöörraadiojaama kasutada?
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
* Millist varianti saab kasutada Eesti amatöörjaama kutsungi moodustamiseks?
* Kuidas algab Haapsalus registreeritud amatöörraadiojaama kutsung?
* Kuhu kuulub piirkondlikult Kutsung ES9Z?
* Millise klassi Eesti amatöörraadiojaamale võib kuuluda Kutsung ES2XX ?
* Milline järelliide omistatakse Ühiskasutusega (raadioklubi) amatöörraadiojaamale?
## S03 Seadusandlus

---
***Kordamisküsimused***
* Mis tingimustel tohib Amatöörraadiosides edastada sihituseta või korrespondendita saateid?
* Kes võib olla ühiskasutusega (raadioklubi) amatöörraadiojaama vastutavaks järelevaatajaks?
* Millise maksimaalse kestvusega võib olla Tarbijakaitse ja Tehnilise Järelevalve Ameti poolt väljastatav Amatöörjaama luba?
* Kus tuleb hoida Amatöörraadiojaama tööluba?
* Mida tuleb teha tööloale kantud andmete muutumisel?
* Kui pikalt on lubatud Amatöörraadiojaama alaline (kohtpaikne) kasutamine väljaspool selle registreeritud asukohta ilma tööloa muutmiseta?

