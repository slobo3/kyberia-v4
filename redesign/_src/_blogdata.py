"""Invented diary (denník) texts. Real kyberia blog entries range from a single photo to 10k+ characters;
most are 1-2k, some are long essays/travelogues. The blogs overview shows ~250 chars (+ photo if any)."""

P = "p"      # paragraph
IMG = "img"  # photo: (IMG, src, caption)

# drienka's diary: (title, when, views, replies, blocks)
DRIENKA = [
    ("hmla nad Dunajom", "12.10.2026 07:12", 242, 3, [
        (IMG, "img/k/hmla.gif", "Apollo, 6:20, Portra 400, jedno políčko"),
        (P, "Budík o pol šiestej, čaj do termosky, foťák do bundy. Keď som vychádzala z domu, bola tma a hmla taká hustá, že som nevidela lampu na konci ulice. Presne na to som čakala celý týždeň, odkedy predpoveď prvýkrát ukázala inverziu a vlhkosť nad deväťdesiat percent."),
        (P, "Na Apollo moste som bola o šiestej. Ľudia v prvom autobuse spali s hlavami opretými o okná, ja som si rozkladala statív na chodníku a pán so psom sa na mňa pozeral, akoby som tam chcela niečo ukradnúť. Pes bol priateľskejší. Dvadsať minút sa nedialo nič, len mi mrzli prsty a hmla bola rovnako hustá zo všetkých strán."),
        (P, "Potom sa nad vodou začala dvíhať. Najprv vystúpil pylón mostu, ako tieň niečoho, čo tam ráno ešte nebolo, potom laná, potom zábradlie na druhej strane. Trvalo to možno tri minúty. Na film nefotím sériu, fotím jedno a dúfam, takže som čakala, kým sa to celé neusporiada do obrazu, ktorý som mala v hlave, a stlačila som spúšť práve raz."),
        (P, "Doma som zistila, že som mala zle nastavenú clonu o pol stupňa. Hmla to zachránila, lebo v nej je všetko trochu presvetlené a nikomu to nevadí. Plné rozlíšenie je v datách, kto chce, môže si ho stiahnuť. Ruky mi rozmrzli až o deviatej. Stálo to za to."),
    ]),
    ("Lisabon, štyri dni s jedným filmom", "06.10.2026 22:15", 518, 14, [
        (P, "Do Lisabonu som letela s jedným pravidlom: jeden film na celé štyri dni. Tridsaťšesť políčok, žiadny telefón na fotenie, žiadne „ešte jedno pre istotu“. Kamarátka, s ktorou som letela, to považovala za hlúposť a mala na to právo, lebo ona sa vrátila s tisíc dvesto fotkami a ja s tridsiatimi štyrmi. Dve som omylom exponovala v lietadle."),
        (P, "Prvý deň som nefotila vôbec. Chodila som po Alfame hore a dole, po schodoch, ktoré nekončia, a čakala, kým mi mesto ukáže, čo z neho chcem mať. Ukázalo mi bielizeň. Všade, na každom balkóne, šnúry s bielizňou natiahnuté cez úzke uličky, plachty, košele, detské tričká, a nad nimi modré nebo, ktoré tam je asi stále. Do večera som mala tri políčka a všetky boli bielizeň."),
        (IMG, "img/k/aleja.gif", "platany pri Tejo, druhý deň ráno"),
        (P, "Druhý deň ráno som šla k rieke. Tejo je pri Lisabone taká široká, že vyzerá ako more, a ráno je nad ňou ten istý opar, aký máme my nad Dunajom, len teplejší. Pozdĺž nábrežia rastú platany so širokými korunami a pod nimi sedia starí páni, ktorí hrajú karty a nefotia sa radi. Spýtala som sa jedného, či môžem. Povedal áno, ak mu potom pošlem fotku. Mám jeho adresu na lístku od električky a fotku pošlem poštou, lebo e-mail nemá."),
        (P, "Električka 28 je presne taká preplnená, ako hovoria všetci sprievodcovia, a ešte o niečo viac. Fotiť sa v nej nedá, lebo sa nedá ani pohnúť rukou. Tak som sa na tú cestu len pozerala: okná, ktoré prechádzajú centimetre od stien domov, vodič, ktorý zvoní na turistov stojacich v koľajach, a pani s taškou zeleniny, ktorá celú cestu rozprávala do telefónu tak nahlas, že som jej rozumela, hoci neviem po portugalsky ani slovo."),
        (P, "Tretí deň pršalo. Celý deň, bez prestávky, teplý vytrvalý dážď, v ktorom lesklé dlaždice na chodníkoch klzali ako ľad. Strávila som ho v antikvariátoch na Chiade a v jednom som našla krabicu starých negatívov, niekoho rodinné fotky zo šesťdesiatych rokov, predávali sa po euru za pás. Kúpila som tri. Doma som ich naskenovala: svadba, pláž a muž, ktorý stojí pred novým autom a je na neho neuveriteľne hrdý. Nikdy nezistím, kto to bol."),
        (IMG, "img/k/film.gif", "kontakt z celého filmu, štyri dni na jednej strane"),
        (P, "Posledný deň som mala ešte osem políčok a to je presne ten moment, kedy sa jeden film zmení z obmedzenia na luxus. Osem fotiek na posledný deň znamená, že môžete byť vyberaví. Fotila som len svetlo: žltú stenu, na ktorú padal tieň z balkóna, schody, na ktorých svietilo slnko presne do polovice, a kocúra, ktorý ležal v jedinom teplom štvorci dlažby na celej ulici."),
        (P, "Doma, keď sa film vrátil z labu, som mala tridsaťštyri fotiek a poznala som každú. Vedela som, kde som stála, čo som cítila, prečo som stlačila spúšť práve vtedy. Kamarátka mi ukázala svojich tisíc dvesto a po stej sme obe prestali dávať pozor. Nehovorím, že je to lepšie. Hovorím, že po štyroch dňoch s jedným filmom si pamätám Lisabon, a nie svoj telefón."),
        (P, "Najlepšia fotka z celého výletu je mimochodom tá bielizeň z prvého dňa. Tri políčka toho istého a vyšlo to až na treťom."),
    ]),
    ("prvý film z novej Nikon FM2", "28.09.2026 21:40", 180, 6, [
        (P, "Kúpila som ju vo Foto bazári od pána, ktorý ju mal dvadsať rokov v skrini. Povedal, že ju kúpil na vlastnú svadbu, nafotil jeden film a odvtedy ju nevytiahol, lebo potom prišli digitály a potom deti a potom už nebol čas. Pýtala som sa, či mu nebude ľúto. Povedal, že bude, ale menej, ako keby ďalších dvadsať rokov ležala v skrini."),
        (P, "Svetelný meter ide, uzávierka ide na všetkých časoch, tesnenia som vymenila sama podľa návodu z fóra o analógovej fotografii (ďakujem, ihla, bez teba by som tam mala lepidlo všade). Jediná chyba je, že spúšť je citlivejšia, než som zvyknutá, takže prvý film obsahuje približne šesť fotiek mojich topánok."),
        (P, "Zvyšok prvého filmu: tri políčka ostré, päť krivých, štyri prepálené. Ale tie tri ostré: Kamzík v hmle, schody na Hrade a susedov kocúr, ktorý pózoval lepšie ako ktokoľvek, koho som kedy fotila. Je to iná rýchlosť. Na digitál som fotila všetko, na film rozmýšľam, či si to políčko zaslúži, a väčšinou si ho nezaslúži, a to je v poriadku."),
    ]),
    ("okná", "21.09.2026 18:05", 95, 2, [
        (IMG, "img/k/panelaky.gif", "Petržalka, piata večer, žiadne zväčšenie, len okná, v ktorých sa svieti"),
    ]),
    ("prečo stále analóg", "14.09.2026 22:30", 412, 19, [
        (P, "Pýtali sa ma to v diskusii už trikrát, tak to napíšem raz a poriadne, a potom už len budem posielať odkaz."),
        (P, "Lebo každé políčko niečo stojí. Rolka filmu stojí dnes takmer dvadsať eur, vyvolanie ďalších desať, skenovanie ďalších desať. Pri tridsiatich šiestich políčkach je to takmer euro a pol za jednu fotku. To je dosť na to, aby som si každú rozmyslela. Nefotím sériu desiatich záberov s nádejou, že jeden vyjde. Fotím jeden a buď vyjde, alebo nie. A keď nevyjde, poučím sa z toho viac, než keby som mala ďalších deväť na výber."),
        (P, "Lebo nevidím výsledok hneď. Medzi tým, keď stlačím spúšť, a tým, keď uvidím fotku, sú dva týždne, niekedy mesiac, ak sa mi nechce ísť do labu. Za ten čas zabudnem, čo presne som fotila, a keď sa film vráti, je to ako list od seba samej z minulosti. Polovicu fotiek si nepamätám a teším sa na ne ako na darček. Druhú polovicu si pamätám až príliš dobre a teším sa, či vyšli."),
        (P, "Lebo film je fyzický. Negatív môžem podržať proti oknu. Môžem ho stratiť, poškriabať, môže zhorieť. Digitálna fotka je všade a nikde, film je v jednej obálke v jednej zásuvke a keď ho nájdem po desiatich rokoch, je presne taký, aký bol. Moja stará mama mala krabicu negatívov zo šesťdesiatych rokov a vďaka nej viem, ako vyzerala jej svadba. Neviem, či moje deti budú vedieť, ako vyzerala moja, ak bude len v cloude."),
        (P, "A lebo digitál mi dal tisíc fotiek z každej dovolenky a žiadnu som si nepozrela dvakrát. Z filmu mám tridsaťšesť a poznám každú. Neviem, či je to lepšie. Viem, že je to moje. A viem, že keď idem fotiť s jedným filmom v taške, pozerám sa na svet inak, pomalšie a pozornejšie, a to by mi stačilo aj keby nevyšla ani jedna fotka."),
        (P, "Na záver praktická poznámka pre tých, čo chcú začať: kúpte si starý mechanický foťák (FM2, K1000, AE-1), jeden čiernobiely film a nefoťte nič, čo by ste fotili telefónom. To je celé. Zvyšok príde sám."),
    ]),
    ("susedov kocúr", "07.09.2026 19:20", 301, 9, [
        (IMG, "img/k/macka.gif", "sedí tam každý večer o siedmej, presne keď sa rozsvieti lampa"),
        (P, "Neviem, ako sa volá. Sused tvrdí, že Mikuláš, susedova žena tvrdí, že Fero. Kocúr na nič z toho nereaguje."),
    ]),
]

# blogs overview: newest entries from everyone (user, title, when, views, replies, excerpt ~250 chars, photo or None)
OVERVIEW = [
    ("drienka", "hmla nad Dunajom", "12.10.2026 07:12", 242, 3,
     "Budík o pol šiestej, čaj do termosky, foťák do bundy. Keď som vychádzala z domu, bola tma a hmla taká hustá, že som nevidela lampu na konci ulice. Na Apollo moste som bola o šiestej a dvadsať minút sa nedialo nič. Potom sa hmla nad vodou začala dvíhať…",
     "img/k/hmla.gif"),
    ("kremeň", "slová, ktoré sa nedajú preložiť", "11.10.2026 11:28", 180, 4,
     "Zbieram ich do zošita už tri roky: „ľúbozvučný“, „prieberčivý“, „otupený“. Kamarátka z Lipska mi za každé slovenské pošle nemecké, ktoré sa tiež nedá preložiť, a tak máme spoločný slovník vecí, ktoré sa nedajú povedať inak než v pôvodnom jazyku…",
     None),
    ("ode", "október v knihách", "10.10.2026 22:40", 96, 2,
     "Tri knihy, dve dočítané. Tokarczuk je pomalá ako rieka a presne preto ju nechcem dočítať, lebo viem, že potom bude dlho nič také dobré. Tretia bola detektívka z antikvariátu, ktorú som si kúpila kvôli obálke a ľutujem iba to, že som ju nekúpila skôr…",
     None),
    ("lemur", "keď mačka vytiahne kábel", "09.10.2026 23:12", 310, 11,
     "Päť rokov uptime, Nextcloud, Jellyfin, zálohy na externý disk raz za mesiac (teda raz za rok, keď si spomeniem). Jediný výpadok za celý ten čas spôsobila mačka, ktorá si pod posteľou našla nový obľúbený kábel. Zálohy som dovtedy riešil teoreticky…",
     None),
    ("sova", "lávka, november, vietor", "08.10.2026 19:05", 74, 1,
     "Nová lávka cez Dunaj je krásna, to jej nikto neberie. Ale kto ju navrhol bez strechy a bez jedinej zábrany proti vetru, nikdy nešiel cez ňu v novembri o šiestej večer s nákupom v oboch rukách. Dnes som stretol troch ľudí, ktorým odletel dáždnik…",
     None),
    ("rybár", "aleja pri Dunaji", "07.10.2026 08:40", 133, 2,
     "Platany pri Dunaji v októbri, jedno políčko, žiadna úprava. Chodím tadiaľ do práce každé ráno už dvanásť rokov a až teraz som si všimol, že tie stromy tvoria tunel, ktorý ráno presne o pol ôsmej prepúšťa svetlo len do stredu cesty…",
     "img/k/aleja.gif"),
    ("drienka", "Lisabon, štyri dni s jedným filmom", "06.10.2026 22:15", 518, 14,
     "Do Lisabonu som letela s jedným pravidlom: jeden film na celé štyri dni. Tridsaťšesť políčok, žiadny telefón na fotenie, žiadne „ešte jedno pre istotu“. Kamarátka, s ktorou som letela, to považovala za hlúposť a mala na to právo…",
     "img/k/film.gif"),
    ("paprika", "kvások, deň štrnásty", "05.10.2026 08:30", 201, 9,
     "Volá sa Gertrúda, žerie ražnú múku a vodu z kohútika, lebo filtrovanú odmieta. Prvé dva týždne smrdela ako starý syr a ja som ju trikrát takmer vyhodila. V sobotu konečne upiekla chlieb, ktorý sa dá jesť, a v nedeľu ďalší, ktorý sa dá aj ponúknuť…",
     None),
    ("kvasar", "langoš tour, prvá zastávka", "04.10.2026 21:15", 158, 7,
     "Liptovský Mikuláš, stánok pri stanici. Cesnak povinný, syr hojný, kečup len na požiadanie, čo je správne. Čakanie dvadsať minút, lebo pred nami bol autobus dôchodcov z Poľska, ktorí vedeli presne, čo chcú. Hodnotenie: dobrý, ale nie najlepší…",
     None),
    ("hmlovina", "Wittgenstein vo štvrtok", "03.10.2026 21:50", 88, 5,
     "Prvé stretnutie čitateľskej skupiny. Prišlo nás šesť, prečítali sme dve strany a hádali sa dve hodiny o tom, čo znamená prvá veta. Nikto nemal pravdu, všetci odchádzali spokojní. Na budúci týždeň ďalšie dve strany, ak sa dovtedy nepohádame…",
     None),
    ("tichá_voda", "prečo dávam silence", "28.09.2026 22:05", 266, 23,
     "Pýtate sa ma to často, tak to napíšem raz. Silence nie je trest, je to pauza. Dávam ho, keď sa dvaja ľudia prestanú baviť o téme a začnú sa baviť o sebe navzájom. Nikdy navždy a vždy obom, nie jednému. Keď sa upokojíte, zruším ho…",
     None),
    ("drienka", "susedov kocúr", "07.09.2026 19:20", 301, 9,
     "",
     "img/k/macka.gif"),
]
