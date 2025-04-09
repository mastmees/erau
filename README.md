# Raadioamatööri õppematerjalide andmekogu

## Üldist

Kasuta UTF8-t ja unix-i stiilis reavahetusi. 

## Miks on muutunud peatükkide ja küsimuste numbrid?

Kuna eesmärgiks on andmestikust genereerida nii sisu kui küsimused kõigi
amatöörklasside jaoks siis tuleb nagunii nii peatükid kui küsimused iga
jaoks uuesti nummerdada, sõltuvalt sellest milline materjal ja millisted
küsimused vastava klassi jaoks olulised on. Seepärast pole peatüki ja
küsimuste numbritel mingit tähtust peale anmestiku struktuuri loomise ja
küsimuste failinimede unikaalsuse tagamise igas peatükis või sektsioonis.

## C01? S01?

Chapters/Sections. Lõpptulemuse genereerimisel pole plaanis neid üldse
sellisel kujul näidata, sisu toimetamise ajal on kasulik näha, et küsimused
või tekst üles leida.

## Miks selline formaat?

Selleks, et sisu toimetamine oleks võimalikult lihtne ja tavalise
tekstieditoriga tehtav. Igasuguseid muid formaate on võimalik programselt
genereerida. Sisu failid on Markdown formaadis. Eeldus on, et sellest on
pythonis võimalik lihtsalt PDF-i ja/või HTML-i teha.

## Miks .et failid?

Tulevikus tõlkimise huvides. Tõlked lähevad paraleelselt eksisteerivatesse
.en, .ru jne. failidesse.

## meta faili formaat

Parserid peaks ridu mida nad ei tunne lihtsalt ignoreerima, sest erinevat infor võib aja jooksul juurde tulla.

>T title  
>A author  


## qxxx faili formaat

Parserid peaks ridu mida nad ei tunne lihtsalt ignoreerima, sest erinevat infor võib aja jooksul juurde tulla.

>? Küsimus  
>A. vale vastusevariant  
>B*. õige vastusevariant  
>. AB  
>\# kommentaar toimetajatele

punktiga real on kirjas millise klassi eksami küsimuseks see sobib

