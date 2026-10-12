"""Invented diary (denník) texts. Blog entries on kyberia are long; the blogs overview shows ~250 chars."""

# drienka's diary: full entries (title, when, views, replies, paragraphs)
DRIENKA = [
    ("hmla nad Dunajom", "12.10.2026 07:12", 242, 3, [
        "Budík o pol šiestej, čaj do termosky, foťák do bundy. Keď som vychádzala z domu, bola tma a hmla taká hustá, že som nevidela lampu na konci ulice. Presne na to som čakala celý týždeň.",
        "Na Apollo moste som bola o šiestej. Ľudia v autobuse spali, ja som si rozkladala statív na chodníku a pán so psom sa na mňa pozeral, akoby som tam chcela niečo ukradnúť. Dvadsať minút sa nedialo nič. Potom sa hmla nad vodou začala dvíhať, pylón mostu vystúpil ako tieň a na pár sekúnd bolo všetko presne také, ako som si to predstavovala.",
        "Jedno políčko. Na film nefotím sériu, fotím jedno a dúfam. Doma som zistila, že som mala zle nastavenú clonu o pol stupňa, ale hmla to zachránila. Fotka je vo fotke dňa, plné rozlíšenie v datách.",
        "Ruky mi rozmrzli až o deviatej. Stálo to za to.",
    ]),
    ("prvý film z novej Nikon FM2", "05.10.2026 21:40", 180, 6, [
        "Kúpila som ju vo Foto bazári od pána, ktorý ju mal dvadsať rokov v skrini. Povedal, že ju kúpil na svadbu, nafotil jeden film a odvtedy ju nevytiahol. Svetelný meter ide, uzávierka ide, tesnenia som vymenila sama podľa návodu z fóra.",
        "Prvý film bol test. Tri políčka ostré, päť krivých, štyri prepálené a zvyšok sú moje topánky, lebo som nevedela, že som stlačila spúšť. Ale tie tri ostré: Kamzík v hmle, schody na Hrade a kocúr zo susedného balkóna, ktorý pózoval lepšie ako ktokoľvek, koho som kedy fotila.",
        "Je to iná rýchlosť. Na digitál som fotila všetko, na film rozmýšľam, či si to políčko zaslúži. Asi preto mám z jedného filmu viac fotiek, ktoré si pamätám, než z celého minulého leta.",
    ]),
    ("Petržalka v novembri", "28.09.2026 18:05", 95, 2, [
        "Panelové domy v hmle vyzerajú ako lode. Prešla som od Draždiaka až k Chorvátskemu ramenu a fotila len okná, v ktorých sa svieti. Každé je iná izba, iná večera, iný televízor.",
        "Najkrajšie svetlo je okolo piatej, keď ešte nie je úplne tma a v kuchyniach už svietia žiarovky. Teplé žlté štvorčeky na studenom šedom panely. Fotila som z ulice, z diaľky, nikomu do okna, len tú mozaiku.",
        "Doma som zistila, že som celý film exponovala o stupeň menej, ako treba. Vyšlo to tmavšie a lepšie. Niekedy je chyba to najlepšie rozhodnutie dňa.",
    ]),
    ("prečo stále analóg", "14.09.2026 22:30", 412, 19, [
        "Pýtali sa ma to v diskusii už trikrát, tak to napíšem raz a poriadne.",
        "Lebo každé políčko niečo stojí. Rolka je drahá, vyvolanie je drahé, a tak si každú fotku rozmyslím. Nefotím sériu desiatich záberov s nádejou, že jeden vyjde. Fotím jeden a buď vyjde, alebo nie.",
        "Lebo nevidím výsledok hneď. Medzi tým, keď stlačím spúšť, a tým, keď uvidím fotku, sú dva týždne. Keď sa film vráti z labu, je to ako list od seba samej z minulosti. Polovicu fotiek si už nepamätám a teším sa na ne ako na darček.",
        "A lebo digitál mi dal tisíc fotiek z dovolenky a žiadnu som si nepozrela dvakrát. Z filmu mám tridsaťšesť a poznám každú. Neviem, či je to lepšie. Viem, že je to moje.",
    ]),
    ("Dunaj pri Devíne", "01.09.2026 06:50", 133, 4, [
        "Zase hmla, zase skoro ráno, tentoraz so statívom a s kamarátkou, ktorá zaspala v aute ešte skôr, než sme vystúpili. Hrad bol schovaný úplne, videli sme len spodok skaly a vodu, ktorá sa leskla ako olej.",
        "Fotila som dlhú expozíciu, osem sekúnd, voda sa vyhladila do zrkadla. Keď vyšlo slnko, hmla zmizla za päť minút a bol to úplne obyčajný pekný deň. Tie najlepšie chvíle trvajú presne tak dlho, aby si ich stihol odfotiť, ak už stojíš na mieste.",
    ]),
]

# blogs overview: newest entries from everyone (user, title, when, views, replies, excerpt ~250 chars)
OVERVIEW = [
    ("drienka", "hmla nad Dunajom", "12.10.2026 07:12", 242, 3,
     "Budík o pol šiestej, čaj do termosky, foťák do bundy. Keď som vychádzala z domu, bola tma a hmla taká hustá, že som nevidela lampu na konci ulice. Na Apollo moste som bola o šiestej a dvadsať minút sa nedialo nič. Potom sa hmla nad vodou začala dvíhať…"),
    ("kremeň", "slová, ktoré sa nedajú preložiť", "11.10.2026 11:28", 180, 4,
     "Zbieram ich do zošita už tri roky: „ľúbozvučný“, „prieberčivý“, „otupený“. Kamarátka z Lipska mi za každé slovenské pošle nemecké, ktoré sa tiež nedá preložiť, a tak máme spoločný slovník vecí, ktoré sa nedajú povedať inak než v pôvodnom jazyku…"),
    ("ode", "október v knihách", "10.10.2026 22:40", 96, 2,
     "Tri knihy, dve dočítané. Tokarczuk je pomalá ako rieka a presne preto ju nechcem dočítať, lebo viem, že potom bude dlho nič také dobré. Tretia bola detektívka z antikvariátu, ktorú som si kúpila kvôli obálke a ľutujem iba to, že som ju nekúpila skôr…"),
    ("lemur", "keď mačka vytiahne kábel", "09.10.2026 23:12", 310, 11,
     "Päť rokov uptime, Nextcloud, Jellyfin, zálohy na externý disk raz za mesiac (teda raz za rok, keď si spomeniem). Jediný výpadok za celý ten čas spôsobila mačka, ktorá si pod posteľou našla nový obľúbený kábel. Zálohy som dovtedy riešil teoreticky…"),
    ("sova", "lávka, november, vietor", "08.10.2026 19:05", 74, 1,
     "Nová lávka cez Dunaj je krásna, to jej nikto neberie. Ale kto ju navrhol bez strechy a bez jedinej zábrany proti vetru, nikdy nešiel cez ňu v novembri o šiestej večer s nákupom v oboch rukách. Dnes som stretol troch ľudí, ktorým odletel dáždnik…"),
    ("paprika", "kvások, deň štrnásty", "07.10.2026 08:30", 201, 9,
     "Volá sa Gertrúda, žerie ražnú múku a vodu z kohútika, lebo filtrovanú odmieta. Prvé dva týždne smrdela ako starý syr a ja som ju trikrát takmer vyhodila. V sobotu konečne upiekla chlieb, ktorý sa dá jesť, a v nedeľu ďalší, ktorý sa dá aj ponúknuť…"),
    ("kvasar", "langoš tour, prvá zastávka", "05.10.2026 21:15", 158, 7,
     "Liptovský Mikuláš, stánok pri stanici. Cesnak povinný, syr hojný, kečup len na požiadanie, čo je správne. Čakanie dvadsať minút, lebo pred nami bol autobus dôchodcov z Poľska, ktorí vedeli presne, čo chcú. Hodnotenie: dobrý, ale nie najlepší…"),
    ("hmlovina", "Wittgenstein vo štvrtok", "03.10.2026 21:50", 88, 5,
     "Prvé stretnutie čitateľskej skupiny. Prišlo nás šesť, prečítali sme dve strany a hádali sa dve hodiny o tom, čo znamená prvá veta. Nikto nemal pravdu, všetci odchádzali spokojní. Na budúci týždeň ďalšie dve strany, ak sa dovtedy nepohádame…"),
    ("mrazik", "elektrické auto, mesiac prvý", "01.10.2026 18:20", 140, 8,
     "Kúpil som ojazdené elektrické auto a prvý mesiac som strávil hľadaním nabíjačiek, ktoré fungujú. Aplikácia hovorí, že je voľná, realita hovorí, že na nej parkuje dodávka. Na druhej strane, ráno je auto vždy teplé a v garáži nesmrdí benzín…"),
    ("tichá_voda", "prečo dávam silence", "28.09.2026 22:05", 266, 23,
     "Pýtate sa ma to často, tak to napíšem raz. Silence nie je trest, je to pauza. Dávam ho, keď sa dvaja ľudia prestanú baviť o téme a začnú sa baviť o sebe navzájom. Vždy na krátko, vždy s odôvodnením v arXive, a vždy obom, nie jednému…"),
]
