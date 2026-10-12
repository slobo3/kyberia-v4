"""Invented content for the v4 showcase. Nobody here is a real kyberia user."""

# login -> avatar hue
USERS = {
    "anima": 40, "bgdny": 160, "kvasar": 20, "polly": 200, "lemur": 130, "drienka": 80, "sklo": 230,
    "tichá_voda": 260, "paprika": 10, "mrazik": 190, "ode": 300, "kremeň": 280, "sova": 55,
    "hmlovina": 320, "vlnka": 110, "papraď": 100, "cín": 30, "hobra": 350, "rybár": 210,
    "lastovička": 170, "mráz": 180, "k22": 0, "ihla": 150, "bubon": 25, "šiška": 60, "bocian": 5,
    "plachta": 240, "rezbár": 340, "mrak": 220, "kompas": 140,
}
FRIENDS = ["anima", "bgdny", "kvasar", "polly", "lemur", "ode", "kremeň", "drienka", "sova"]

# where people are right now (people page, friends online)
LOCATION = {
    "anima": "bookmarks", "bgdny": "Kyberia session 2026", "kvasar": "mail", "polly": "Lipsko na víkend",
    "lemur": "K", "ode": "Čo čítame v októbri", "kremeň": "Slovenčina pre profesionálov", "drienka": "fotka dňa",
    "sova": "bratislava", "paprika": "Gastronomický spolok", "mrazik": "people", "sklo": "last",
    "tichá_voda": "101 silence justification arXiv", "hmlovina": "Close reading group", "vlnka": "Slovenská politická scéna",
    "papraď": "Lyžovanie", "cín": "Mestá a doprava", "hobra": "Hudobné okienko", "rybár": "Foto bazár",
    "lastovička": "Grafický dizajn a typografia", "mráz": "BUGLIST", "k22": "Thinkpad yard", "ihla": "analógová fotografia",
    "bubon": "Slúchadlá a HiFi", "šiška": "Voľby 2027", "bocian": "bookmarks", "plachta": "registrations",
    "rezbár": "Hodiny a hodinky", "mrak": "Sprosto-vedecké otázky", "kompas": "pripomienky k systému",
}
IDLE = ["teraz", "1 min", "2 min", "4 min", "6 min", "9 min", "11 min", "14 min", "18 min", "22 min", "27 min",
        "31 min", "34 min", "40 min", "44 min", "51 min", "58 min", "1 h 5 min", "1 h 12 min", "1 h 20 min",
        "1 h 31 min", "1 h 40 min", "1 h 56 min", "2 h 3 min", "2 h 15 min", "2 h 30 min", "2 h 41 min",
        "2 h 50 min", "3 h 2 min", "3 h 20 min"]

# posts: (user, day, time, where, section, title or None, K, new, children, text)
# day: 0 = dnes (12.10.2026), 1 = včera, 2 = 10.10., …
POSTS = [
    ("bgdny", 0, "20:41", "Kyberia session 2026", "Hudba", None, 0, True, 1, "Idem. Vezmem aj dvoch ľudí z Trnavy, mám miesto v aute, odchod 18:30 od stanice."),
    ("paprika", 0, "20:22", "kde kúpiť dobrý chlieb v BA", "Gastronomický spolok", "Re[3]: kde kúpiť dobrý chlieb v BA", 33, True, 4, "Na Obchodnej, pekáreň v dvore za kníhkupectvom. Kváskový ražný, v sobotu do desiatej vypredané."),
    ("mrazik", 0, "19:42", "Elektromobilita", "Hobby a voľný čas", "nabíjanie na sídlisku", 3, True, 12, "Má niekto skúsenosť s nabíjaním z verejnej nabíjačky na sídlisku bez vlastnej garáže? Koľko to reálne vychádza na mesiac?"),
    ("vlnka", 0, "19:15", "Slovenská politická scéna", "Politika", "Re[12]: rozpočet na budúci rok", 9, True, 31, "Kto čakal, že sa bude škrtať na kultúre a nie na tendroch, ten tu asi nežije dlho."),
    ("mráz", 0, "18:50", "BUGLIST", "kyberia.sk", "bookmarks sa nenačítajú po polnoci", 14, True, 6, "Od včera po polnoci mi bookmarks visia aj minútu. Ráno je to v poriadku. Má to ešte niekto?"),
    ("hobra", 0, "17:33", "Hudobné okienko", "Hudba", "čo počúvate dnes", 11, True, 21, "Celý deň Boards of Canada, lebo prší a inak to nejde."),
    ("cín", 0, "16:05", "Mestá a doprava", "Politika", "električka do Petržalky: prvý mesiac", 27, False, 44, "Mesiac po spustení: ráno je plná, večer poloprázdna, a nikto nevie, prečo nejazdí po desiatej."),
    ("lastovička", 0, "14:47", "Grafický dizajn a typografia", "Photo & Visual", "Atkinson Hyperlegible: písmo pre všetkých?", 18, False, 9, "Font, ktorý vznikol pre slabozrakých, a zrazu ho chce každý. Je to dobré písmo, alebo len dobrý príbeh?"),
    ("drienka", 0, "07:12", "fotka dňa", "::graphics::design::photo", "hmla nad Dunajom", 28, False, 7, "Šiesta ráno z Apollo mosta. Dvadsať minút čakania, jedna fotka."),
    ("anima", 0, "09:14", "Veda a technológie", "Veda a technológie", "Prečo sa mestské stromy oplatia viac ako klimatizácia", 64, True, 48, "Prehľad troch štúdií z Viedne a Barcelony: koľko stupňov ušetrí jeden vzrastlý javor, koľko stojí jeho údržba, a prečo to radnice aj tak počítajú zle."),
    ("polly", 1, "21:40", "Hudba", "Hudba", "Kyberia session 2026: zostava, miesto, lístky", 51, True, 112, "Sobota 8. novembra, Bratislava. Štyri live sety, jeden DJ, a tentokrát aj šatňa."),
    ("ode", 1, "23:10", "Čo čítame v októbri", "L:teratúra", "Re: Čo čítame v októbri", 5, False, 0, "Tokarczuk, Pravek a iné časy. Pomalé ako rieka, a presne preto to funguje."),
    ("polly", 1, "22:15", "Lipsko na víkend", "Cestovanie", "Re[2]: Lipsko na víkend", 6, False, 3, "V Lipsku je pivo stále lacnejšie ako v Starom Meste. Toľko k teórii."),
    ("k22", 1, "20:02", "Thinkpad yard", "Ostatné", "X230 v roku 2026", 15, False, 19, "Nová batéria, SSD, coreboot. Je to stále najlepší notebook, ktorý som kedy mal, a vážim si to viac než by som mal."),
    ("mrak", 1, "18:31", "Sprosto-vedecké otázky", "Ostatné", "prečo mačky padajú na nohy, ale chlieb na maslo", 22, False, 37, "Vážne pýtam. Má to niečo spoločné s momentom zotrvačnosti alebo len s mojou smolou?"),
    ("sova", 1, "16:20", "bratislava", "Ostatné", "Re[8]: nové lávky cez Dunaj", 4, False, 2, "Lávka je pekná, ale kto ju navrhol bez strechy, nikdy nešiel cez ňu v novembri."),
    ("kremeň", 1, "11:02", "Slovenčina pre profesionálov", "Filozofia, text & jazyk", "„za účelom“ musí zomrieť", 31, False, 58, "Zbierka najhorších úradných fráz za tento týždeň. Prispievajte, ale bez mien."),
    ("ihla", 1, "09:40", "analógová fotografia", "Photo & Visual", "Portra 400 zdražela znova", 8, False, 15, "Rolka za 19 eur. Prechádzam na čiernobielu a vyvolávam doma, inak to nejde."),
    ("ode", 2, "18:02", "L:teratúra", "L:teratúra", "Čo čítame v októbri", 22, False, 27, "Mesačné vlákno. Jedna kniha, dve vety prečo, žiadne spoilery bez varovania."),
    ("lemur", 3, "12:30", "Compz & Net", "Compz & Net", "Self-hosting v roku 2026: čo nám beží doma", 19, False, 89, "Zdieľajte setup: hardvér, čo na ňom beží, koľko to žerie, a jedna vec, ktorú by ste dnes urobili inak."),
    ("kvasar", 3, "22:47", "Halušky", "Halušky", "najlepší langoš na Slovensku", 12, False, 63, "Hlasujte, ale Zlaté piesky sa nerátajú, tam sme boli všetci a všetci vieme."),
    ("tichá_voda", 4, "10:15", "101 silence justification arXiv", "kyberia", "silence: Re[18] Kyberia session 2026", 23, False, 4, "Dvaja užívatelia, silence v nóde Kyberia session 2026, dôvod: osobné útoky od úrovne 9. Zruším, keď sa ozvú."),
    ("rybár", 4, "15:55", "Foto bazár", "Photo & Visual", "predám: Nikon FM2, čierny", 2, False, 5, "Plne funkčný, nové tesnenia. Osobne v BA, cena dohodou, nie výmena za drony."),
    ("bubon", 5, "21:12", "Slúchadlá a HiFi", "Audio", "otvorené slúchadlá do 200 eur", 7, False, 26, "Hľadám niečo na večerné počúvanie, nie do MHD. Sennheiser alebo niečo nové?"),
    ("hmlovina", 6, "19:30", "Close reading group", "Filozofia, text & jazyk", "november: Wittgenstein, Tractatus", 17, False, 11, "Čítame po kapitolách, stretnutie každý štvrtok online. Kto ide, napíšte pod to."),
    ("lemur", 9, "18:10", "Hobby a voľný čas", "Hobby a voľný čas", "Záhrada na balkóne: zelená stena za 40 eur", 40, False, 64, "Paleta, geotextília, kvapková závlaha z PET fliaš. Zelená stena prežila leto aj dovolenku."),
    ("drienka", 13, "20:05", "::graphics::design::photo", "Photo & Visual", "Prečo je kyberia zelená?", 58, False, 212, "Fosforové monitory, terminály, Matrix, alebo len náhoda? Zbieram teórie."),
    ("papraď", 14, "08:30", "Lyžovanie", "Ostatné", "sezóna 2026/27: kde bude sneh", 6, False, 33, "Predpovede hovoria o slabom začiatku. Kto pôjde do Álp hneď v decembri?"),
]

# what's been put on main (title, user, section, date, K, new)
MAIN = [
    ("Prečo sa mestské stromy oplatia viac ako klimatizácia", "anima", "Veda a technológie", "12.10.", 64, 6,
     "Prehľad troch štúdií z Viedne a Barcelony: koľko stupňov ušetrí jeden vzrastlý javor, koľko stojí jeho údržba, a prečo to radnice aj tak počítajú zle. Plus mapa ulíc, kde by stromy pomohli najviac."),
    ("Kyberia session 2026: zostava, miesto, lístky", "polly", "Hudba", "11.10.", 51, 31, "Sobota 8. novembra, Bratislava, klub pri Dunaji. Štyri live sety, jeden DJ na záver a tentokrát aj šatňa, sľubujem. Vstup pre kyberiánov za dobrovoľný príspevok, výťažok ide na server. Do diskusie píšte, kto ide, kto hrá a kto potrebuje odvoz z Trnavy."),
    ("Prečo je kyberia zelená?", "drienka", "::graphics::design::photo", "29.09.", 58, 0, "Fosforové monitory, terminály, Matrix, alebo len náhoda pri prvom CSS v roku 2001? Pýtal som sa troch ľudí, čo boli pri tom, a dostal som štyri odpovede. Zbieram teórie aj dôkazy, staré screenshoty a zálohy šablón sú vítané."),
    ("Záhrada na balkóne: zelená stena za 40 eur", "lemur", "Hobby a voľný čas", "03.10.", 40, 0, "Paleta z bazáru, geotextília, kvapková závlaha z PET fliaš a jeden časovač. Stena prežila leto aj dvojtýždňovú dovolenku a bazalka rastie lepšie než v obchode. Návod krok za krokom, aj s chybami, ktoré som urobil prvýkrát."),
    ("„za účelom“ musí zomrieť", "kremeň", "Filozofia, text & jazyk", "11.10.", 31, 4, "Zbierka najhorších úradných fráz za tento týždeň. Víťaz: „v rámci zabezpečenia realizácie“, tesne za ním „predmetná vec“. Každý piatok vyberieme jednu a preložíme ju do ľudskej reči. Prispievajte, ale bez mien a bez fotiek úradníkov."),
    ("električka do Petržalky: prvý mesiac", "cín", "Politika", "12.10.", 27, 0, "Ráno plná, večer poloprázdna a nikto nevie, prečo nejazdí po desiatej. Tri dni som počítal cestujúcich na štyroch zastávkach, výsledky sú v tabuľke nižšie. Spoiler: autobusy, ktoré mali zrušiť, jazdia stále a sú prázdne."),
    ("Čo čítame v októbri", "ode", "L:teratúra", "10.10.", 22, 0, "Mesačné vlákno. Jedna kniha, dve vety prečo, žiadne spoilery bez varovania. Minulý mesiac vyhral Hrabal, predminulý Tokarczuk, takže stredná Európa vedie. Kto prečíta niečo z iného kontinentu, dostane čestné K."),
    ("Self-hosting v roku 2026: čo nám beží doma", "lemur", "Compz & Net", "09.10.", 19, 0, "Zdieľajte setup: hardvér, čo na ňom beží, koľko to žerie zo zásuvky, a jedna vec, ktorú by ste dnes urobili inak. Ja začínam: starý Thinkpad, Nextcloud, Jellyfin a záložný disk, ktorý som raz za rok zabudol pripojiť."),
    ("Atkinson Hyperlegible: písmo pre všetkých?", "lastovička", "Photo & Visual", "12.10.", 18, 0, "Font, ktorý vznikol pre slabozrakých, a zrazu ho chce každý redizajn vrátane jedného nemenovaného. Je to dobré písmo, alebo len dobrý príbeh? Porovnal som ho s Verdanou a Tahomou na rovnakom texte, obrázky vo vlákne."),
    ("november: Wittgenstein, Tractatus", "hmlovina", "Filozofia, text & jazyk", "06.10.", 17, 0, "Čítame po kapitolách, stretnutie každý štvrtok o ôsmej online, odkaz pošlem mailom. Netreba nič vedieť vopred, stačí text a trpezlivosť. Čo sa nedá povedať, o tom treba mlčať, ale v diskusii to neplatí."),
    ("X230 v roku 2026", "k22", "Ostatné", "11.10.", 15, 0, "Nová batéria, SSD, coreboot a klávesnica zo staršieho modelu. Stále najlepšia klávesnica, akú som kedy mal, a vážim si ju viac, než by som mal. Displej je zlý, váha je zlá, a aj tak ho nevymením."),
    ("najlepší langoš na Slovensku", "kvasar", "Halušky", "09.10.", 12, 0, "Hlasujte v komentároch, jeden hlas na človeka, cesnak je povinný. Zlaté piesky sa nerátajú, tam sme boli všetci a všetci vieme, ako to skončilo. Víťaza navštívime spoločne, termín dohodneme podľa počasia."),
    ("hmla nad Dunajom", "drienka", "::graphics::design::photo", "12.10.", 28, 0, "Šiesta ráno z Apollo mosta, dvadsať minút čakania na správne svetlo a jedna fotka, kým sa hmla zdvihla. Studené ruky, analóg, Portra 400. Nabudúce idem z druhej strany, ak niekto chce ísť so mnou, ozvite sa."),
]

# replies to slobo's nodes: (user, date, my node, my quote, text, K, new)
REPLIES = [
    ("kvasar", "12.10.2026 19:58", "update šablóny main, ledger a registrácia", "ako chceš riešiť staré linky?", "Dizajn je jedna vec. Kto napíše testy na bookmarky a počítanie nových nód?", 0, True),
    ("k22", "12.10.2026 14:12", "update šablóny main, ledger a registrácia", "navrhujem začať tým, čo používame denne", "Daj vedieť, keď bude niečo na vyskúšanie. Rád to rozbijem.", 4, True),
    ("kremeň", "12.10.2026 11:40", "Long Form Journalism", "The quiet death of the RSS reader", "Čítam cez RSS dodnes a som na to hrdý. Dobrý text.", 2, True),
    ("anima", "11.10.2026 22:05", "Long Form Journalism", "The quiet death of the RSS reader", "Ten odsek o chronologickom čítaní by mal visieť na každej redakcii.", 6, False),
    ("kremeň", "02.10.2026 09:03", "Albumy roka 2026", "čo by ste tam doplnili?", "Zoznam je dobrý, ale chýba tam aspoň jedna slovenská platňa.", 0, False),
    ("sklo", "01.10.2026 18:46", "Albumy roka 2026", "čo by ste tam doplnili?", "Pridávam dve veci z Bandcampu, linky dám večer.", 0, False),
    ("ode", "28.09.2026 21:30", "kyberia v4", "farby ostávajú, písmo je nové", "Konečne to prečítam bez lupy. Len tú zelenú nedajte.", 12, False),
    ("mráz", "27.09.2026 10:12", "kyberia v4", "farby ostávajú, písmo je nové", "Ako bude vyzerať BUGLIST? Pýtam sa pre kamaráta.", 3, False),
]

# mail conversations: (user, last message, mine?, when, unread)
MAIL = [
    ("kvasar", "beriem jedno miesto, platím benzín aj langoš", False, "20:52", 2),
    ("anima", "pošli mi ten článok o javoroch", True, "17:03", 0),
    ("polly", "v Lipsku je pivo stále lacnejšie", False, "včera", 0),
    ("kremeň", "dík, vrátim v piatok", True, "8.10.", 0),
    ("sklo", "máš ešte tú starú Nikon FM2?", False, "2.10.", 0),
    ("drienka", "tá fotka z Apollo mosta ide na main?", False, "1.10.", 0),
    ("lemur", "aký router máš na tom self-hostingu?", True, "29.9.", 0),
    ("tichá_voda", "silence ti zruším, keď sa upokojíte", False, "28.9.", 0),
    ("ode", "Tokarczuk ti donesiem v nedeľu", False, "25.9.", 0),
    ("mráz", "ten bug s bookmarkami som videl, pozriem", False, "22.9.", 0),
    ("hobra", "zoznam pesničiek na session", True, "20.9.", 0),
    ("sova", "lávka cez Dunaj: ideš v sobotu?", False, "14.9.", 0),
]

DAYS = ["dnes, pondelok 12. októbra", "včera, nedeľa 11. októbra", "sobota 10. októbra", "piatok 9. októbra",
        "štvrtok 8. októbra", "streda 7. októbra", "utorok 6. októbra"]
DATE = {0: "12.10.2026", 1: "11.10.2026", 2: "10.10.2026", 3: "09.10.2026", 4: "08.10.2026", 5: "07.10.2026",
        6: "06.10.2026", 9: "03.10.2026", 13: "29.09.2026", 14: "28.09.2026"}

# open mail conversation with kvasar, oldest first: (from, day label, time, where they wrote from, text, new)
THREAD_WITH = "kvasar"
THREAD = [
    ("kvasar", "2.10.", "21:14", "Halušky", "Robíš ešte tú anketu o langošoch? Mám kandidáta z Liptova.", False),
    ("slobo", "2.10.", "21:30", "bookmarks", "Robím. Pošli adresu, overíme v sobotu.", False),
    ("kvasar", "2.10.", "21:32", "mail", "Liptovský Mikuláš, pri stanici. Cesnak je tam povinný, nie voliteľný.", False),
    ("slobo", "5.10.", "10:02", "Compz & Net", "Mimochodom, nevieš, kto u nás rieši BUGLIST? Bookmarks mi po polnoci visia.", False),
    ("kvasar", "5.10.", "10:20", "BUGLIST", "mráz. Napíš mu priamo, do BUGLIST-u sa pozerá raz za týždeň.", False),
    ("kvasar", "včera", "22:14", "Kyberia session 2026", "Ideš v sobotu? Vraj vezieš ľudí z Trnavy.", False),
    ("slobo", "včera", "22:30", "bookmarks", "Ja nie, to je bgdny. Ale idem, uvidíme sa tam.", False),
    ("kvasar", "dnes", "20:50", "mail", "Aha, pomýlil som si vás. Napísal som mu do fóra.", True),
    ("kvasar", "dnes", "20:52", "mail", "Beriem jedno miesto, platím benzín aj langoš. Ty si dáš čo?", True),
]


def icon(user):
    """Path to the user's (invented) GIF icon, generated by _gen_images.py."""
    import unicodedata
    s = unicodedata.normalize("NFKD", user).encode("ascii", "ignore").decode()
    return "img/u/" + "".join(c if c.isalnum() else "_" for c in s.lower()) + ".gif"

# K (top appreciated): mostly photos and longer posts. (user, where, section, title, kind, img, text, K, when)
K_ITEMS = [
    ("drienka", "fotka dňa", "::graphics::design::photo", "hmla nad Dunajom", "photo", "img/k/hmla.gif",
     "Šiesta ráno z Apollo mosta, dvadsať minút čakania na svetlo.", 64, "12.10.2026 07:12"),
    ("anima", "Veda a technológie", "Veda a technológie", "Prečo sa mestské stromy oplatia viac ako klimatizácia", "text", None,
     "Pred rokom som začala zbierať štúdie o tom, čo robia stromy s teplotou v meste. Väčšina hovorí to isté: vzrastlý strom ochladí okolie o dva až štyri stupne a v uliciach, kde sa ľudia pohybujú, to robí väčší rozdiel než akákoľvek klimatizácia. Viedeň, Barcelona a Rotterdam to merali každá inak, ale výsledok je podobný. Prečo to radnice aj tak počítajú zle? Lebo strom je v rozpočte zelene, ale úspora je v zdravotníctve a v účtoch za elektrinu, a nikto neporovnáva tie dve tabuľky naraz.", 58, "12.10.2026 09:14"),
    ("sova", "fotka dňa", "::graphics::design::photo", "mačka na parapete, Štrkovec", "photo", "img/k/macka.gif",
     "Susedova. Sedí tam každý večer o siedmej, presne keď sa rozsvieti lampa.", 51, "11.10.2026 19:20"),
    ("polly", "Kyberia session 2026", "Hudba", "session: fotky zo zvukovej skúšky", "photo", "img/k/session.gif",
     "Generálka v piatok večer. Svetlá sú hotové, šatňa ešte nie.", 47, "11.10.2026 23:05"),
    ("bubon", "Hudobné okienko", "Hudba", "Re[4]: čo počúvate dnes", "video", "youtube.com :: 7:42",
     "Live session z malého klubu v Brne, zvuk je lepší než na albume. Od 3:10 to začne.", 44, "12.10.2026 18:02"),
    ("vlnka", "Slovenská politická scéna", "Politika", "Re[12]: rozpočet na budúci rok", "text", None,
     "Kto čakal, že sa bude škrtať na kultúre a nie na tendroch, ten tu asi nežije dlho.", 41, "12.10.2026 19:15"),
    ("mráz", "BUGLIST", "kyberia.sk", "denne aktívni za tri mesiace", "photo", "img/k/graf.gif",
     "Graf z logov. Tá diera vpravo je víkend, keď padol server. Zvyšok je pekne stabilný.", 38, "12.10.2026 16:40"),
    ("kremeň", "Slovenčina pre profesionálov", "Filozofia, text & jazyk", "„za účelom“ musí zomrieť", "text", None,
     "Zbierka najhorších úradných fráz za tento týždeň. Víťaz: „v rámci zabezpečenia realizácie“, tesne za ním „predmetná vec“ a „z dôvodu toho, že“. Každý piatok vyberieme jednu a preložíme ju do ľudskej reči. Pravidlá: bez mien, bez fotiek úradníkov, a ak frázu nájdete vo vlastnom texte, priznajte sa. Ja začínam: minulý mesiac som napísal „v nadväznosti na uvedené“ a dodnes sa hanbím.", 33, "11.10.2026 11:02"),
    ("drienka", "fotka dňa", "Photo & Visual", "Petržalka v hmle", "photo", "img/k/panelaky.gif",
     "Panelové domy v hmle vyzerajú ako lode. Fotila som len okná, v ktorých sa svieti.", 31, "10.10.2026 18:05"),
    ("rybár", "analógová fotografia", "Photo & Visual", "aleja pri Dunaji, Portra 400", "photo", "img/k/aleja.gif",
     "Platany pri Dunaji v októbri. Jedno políčko, žiadna úprava.", 27, "10.10.2026 08:40"),
    ("hobra", "Hudba", "Hudba", "dokument: ako sa robí vinyl", "video", "vimeo.com :: 24:10",
     "Lisovňa v Lodenici, od laku po obal. Dvadsať minút, ktoré vás naučia mať radšej platne.", 25, "10.10.2026 20:15"),
    ("k22", "Thinkpad yard", "Ostatné", "Re[7]: X230 v roku 2026", "text", None,
     "Displej je zlý, váha je zlá. Tá klávesnica to vyváži.", 24, "11.10.2026 20:31"),
    ("drienka", "fotka dňa", "Photo & Visual", "prečo stále analóg", "text", None,
     "Lebo každé políčko niečo stojí. Lebo nevidím výsledok hneď. Lebo keď sa film vráti z labu, je to ako list od seba samej spred dvoch týždňov. Digitál mi dal tisíc fotiek z výletu a žiadnu som si nepozrela dvakrát. Z filmu mám tridsaťšesť a poznám každú. Neviem, či je to lepšie. Viem, že je to moje.", 22, "09.10.2026 22:30"),
    ("drienka", "fotka dňa", "Photo & Visual", "prvý film z novej Nikon FM2", "photo", "img/k/film.gif",
     "Prvých 36 políčok: tri ostré, päť krivých, zvyšok sú moje topánky. Je to láska.", 18, "05.10.2026 21:40"),
    ("lemur", "Compz & Net", "Compz & Net", "Self-hosting v roku 2026: čo nám beží doma", "text", None,
     "Starý Thinkpad pod posteľou, Nextcloud, Jellyfin, Pi-hole a záložný disk, ktorý som raz za rok zabudol pripojiť. Žerie to 11 W, beží to päť rokov a jediný výpadok bol, keď mačka vytiahla kábel. Čo by som urobil inak: zálohy automaticky od prvého dňa, nie od prvej straty dát.", 15, "09.10.2026 12:30"),
]


# user node numbers (invented): users are referenced by number, shown as "name [number]"
USER_ID = {u: 7004001 + i for i, u in enumerate(USERS)}
USER_ID.update({"slobo": 5001001, "ozvena": 4401337, "lúč": 4401400, "fiktivny_admin": 1000001})
