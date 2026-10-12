"""Write example pages for more templates: submission, blog, data. Same node anatomy everywhere:
node details -> content -> add form -> children. Run from anywhere."""
import html
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import icon  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
SEP = '<span class="sep">::</span>'
PICK = '<input class="pick" type="checkbox" aria-label="vybrať">'
COST = '<span class="cost" title="pridanie stojí 1 K">−1 K</span> '


def post(user, when, text, title=None, k=None, new=False, level=None, children=""):
    kk = f' {SEP} <span class="k">{k} K</span>' if k else ""
    nn = f' {SEP} <span class="new">NEW</span>' if new else ""
    lv = f' {SEP} <span class="lvl">level {level}</span>' if level else ""
    t = f'<div class="pt re">{e(title)}</div>' if title else ""
    kids = f"\n<ol>\n{children}\n</ol>" if children else ""
    return f"""<li><article class="post">
  <img class="av" src="{icon(user)}" alt="" width="50" height="50">
  <div>
    <div class="ph"><a class="who" href="user.html">{e(user)}</a>{PICK} <a class="when" href="submission.html">{e(when)}</a>{lv}{kk}{nn}</div>
    {t}
    <div class="pb"><p>{e(text)}</p></div>
    <div class="pa"><button class="btn ghost">odpovedať</button><button class="btn ghost">K+</button></div>
  </div>
</article>{kids}</li>"""


def composer(label, placeholder, title_ph="názov (nepovinný, inak Re: …)"):
    return f"""      <form class="composer" aria-label="{label}">
        <div class="title-row">
          <input class="field" placeholder="{title_ph}" aria-label="názov">
          <label class="check"><input type="checkbox"> bez HTML</label>
        </div>
        <textarea class="field" placeholder="{placeholder}" aria-label="text"></textarea>
        <div class="send"><span></span><span><button type="button" class="btn">náhľad</button> {COST}<button type="submit" class="btn primary">pridať</button></span></div>
      </form>"""


def write(name, text):
    io.open(name, "w", encoding="utf-8").write(text)
    print("wrote", name)


# ── submission: one post as a node, with its replies ──────────────────────
replies = (
    post("cín", "12.10.2026 10:02", "Viedeň to počíta v nákladoch na zdravotníctvo, nie v rozpočte zelene. Preto im to vychádza. U nás to platí iný úrad.", "Re: Prečo sa mestské stromy oplatia…", k=6, level=1,
         children=post("anima", "12.10.2026 10:20", "Presne. Kto platí stromy a kto ušetrí na horúčavách, sú dve rôzne kapitoly. Nikto to nespojí.", "Re[2]: Prečo sa mestské stromy oplatia…", k=3, level=2))
    + "\n" + post("mrak", "12.10.2026 11:45", "A koľko z tých stromov prežije prvé tri roky bez polievania? To je tá časť, ktorá sa v štúdiách nespomína.", "Re: Prečo sa mestské stromy oplatia…", level=1, new=True)
    + "\n" + post("lemur", "12.10.2026 13:30", "Na našom sídlisku vysadili javory pred piatimi rokmi. Teraz je tam v lete o dva stupne menej, meral som to cez Arduino.", "Re: Prečo sa mestské stromy oplatia…", k=11, level=1, new=True)
)
body = f"""  <div class="head">
    <h1>Prečo sa mestské stromy oplatia viac ako klimatizácia</h1>
    <div class="actions">
      <span class="k ksum">64 K</span>
      <button class="btn">K+</button>
      <button class="btn">book</button>
      <button class="btn">fook</button>
      <button class="btn ghost">put do…</button>
    </div>
  </div>
  <section class="topic prose">
    <p>Pred rokom som začala zbierať štúdie o tom, čo robia stromy s teplotou v meste. Väčšina hovorí to isté: vzrastlý strom ochladí okolie o dva až štyri stupne a v uliciach, kde sa ľudia pohybujú, to robí väčší rozdiel než akákoľvek klimatizácia.</p>
    <h2>Tri štúdie, ktoré stoja za prečítanie</h2>
    <ol>
      <li><b>Viedeň, 2022:</b> mapa ulíc s teplotou povrchu v júli. Ulice so stromami o 6 °C chladnejšie na úrovni chodníka.</li>
      <li><b>Barcelona, 2023:</b> superbloky a nové výsadby. Menej hospitalizácií počas vĺn horúčav.</li>
      <li><b>Rotterdam, 2024:</b> náklady na údržbu na strom a rok, porovnané s cenou chladenia budov.</li>
    </ol>
    <p>Prečo to radnice aj tak počítajú zle? Lebo strom je v rozpočte zelene, ale úspora je v zdravotníctve a v účtoch za elektrinu. Nikto neporovnáva tie dve tabuľky naraz.</p>
    <blockquote>Najlacnejšia klimatizácia v meste je tá, ktorá rastie sama.</blockquote>
    <p>Pridávam mapu ulíc v Bratislave, kde by stromy pomohli najviac. Návrhy na doplnenie vítané.</p>
  </section>
{composer("odpovedať na príspevok", "tvoja reakcia…")}
  <div class="thread-bar"><h2>48 reakcií</h2></div>
  <ol class="thread">
{replies}
  </ol>
  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>"""
write("submission.html",
      "<!-- title: Prečo sa mestské stromy oplatia viac ako klimatizácia -->\n<!-- nav: kyberia -->\n"
      "<!-- node: id=9185501; name=Prečo sa mestské stromy oplatia…; template=submission; parent=63611|Veda a technológie|kyberia.html; "
      "owner=anima; viewers=slobo,cín,mrak,lemur; img=img/n/main0.gif; created=12.10.2026 09:14; updated=12.10.2026 09:31; perms=r, w :: public; view=threaded -->\n"
      f'<main class="wrap" id="obsah">\n{body}\n</main>\n')

# ── blog: a user's diary (denník); entries newest first ───────────────────
ENTRIES = [
    ("hmla nad Dunajom", "12.10.2026 07:12", 242, 3, 28, "Šiesta ráno z Apollo mosta. Dvadsať minút čakania na správne svetlo a jedna fotka, kým sa hmla zdvihla. Studené ruky, analóg, Portra 400, a pocit, že mesto ešte spí len pre mňa."),
    ("prvý film z novej Nikon FM2", "05.10.2026 21:40", 180, 6, 12, "Kúpila som ju v Foto bazári od človeka, ktorý ju mal v skrini dvadsať rokov. Prvých 36 políčok: tri ostré, päť krivých, zvyšok sú moje topánky. Je to láska."),
    ("Petržalka v novembri", "28.09.2026 18:05", 95, 2, 7, "Panelové domy v hmle vyzerajú ako lode. Prešla som od Draždiaka až k Chorvátskemu ramenu a fotila len okná, v ktorých sa svieti."),
    ("prečo stále analóg", "14.09.2026 22:30", 412, 19, 41, "Lebo každé políčko niečo stojí. Lebo nevidím výsledok hneď. Lebo keď sa film vráti z labu, je to ako list od seba samej spred dvoch týždňov."),
    ("Dunaj pri Devíne", "01.09.2026 06:50", 133, 4, 9, "Zase hmla, zase skoro ráno. Tentoraz s statívom a s kamarátkou, ktorá zaspala v aute. Fotky budú vo fotke dňa."),
]
entries = "\n".join(f"""    <article class="entry">
      <h2><a href="submission.html">{e(t)}</a></h2>
      <div class="m"><a href="user.html">drienka</a> {SEP} <a class="when" href="submission.html">{when}</a> {SEP} videné {views}× {SEP} {subs} reakcií {SEP} <span class="k">{k} K</span></div>
      <p>{e(x)}</p>
    </article>""" for t, when, views, subs, k, x in ENTRIES)
body = f"""  <div class="head">
    <h1>denník: drienka</h1>
    <div class="actions">
      <span class="k ksum">97 K</span>
      <button class="btn">K+</button>
      <button class="btn">book</button>
      <button class="btn">fook</button>
    </div>
  </div>
  <section class="topic prose"><p>Fotky z rána, film, mesto v hmle. Píšem, keď sa vrátim z labu.</p></section>
{composer("pridať zápis do denníka", "o čom dnes…", "názov zápisu")}
  <div class="entries">
{entries}
  </div>
  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie zápisy</a></nav>"""
write("blog.html",
      "<!-- title: denník: drienka -->\n<!-- nav: people -->\n"
      "<!-- node: id=7004120; name=denník: drienka; template=blog; parent=7004001|drienka|user.html; owner=drienka; "
      "viewers=slobo,ihla,ode; img=img/u/drienka.gif; created=14.03.2019 20:10; updated=12.10.2026 07:12; perms=r :: public -->\n"
      f'<main class="wrap" id="obsah">\n{body}\n</main>\n')

# ── data: a file node (uploaded file with its own access rights) ──────────
comments = (
    post("ihla", "12.10.2026 08:01", "Plné rozlíšenie je krásne. Tá zrnitosť je presne to, prečo fotím na film.", "Re: hmla_nad_dunajom.tif", k=4, level=1)
    + "\n" + post("ode", "12.10.2026 09:40", "Môžem si to vytlačiť na stenu? Opýtam sa radšej, než to spravím.", "Re: hmla_nad_dunajom.tif", level=1, new=True,
                  children=post("drienka", "12.10.2026 09:52", "Môžeš, len mi pošli fotku tej steny.", "Re[2]: hmla_nad_dunajom.tif", k=2, level=2, new=True))
)
body = f"""  <div class="head">
    <h1>hmla_nad_dunajom.tif</h1>
    <div class="actions">
      <span class="k ksum">19 K</span>
      <a class="btn primary" href="#">stiahnuť</a>
      <button class="btn">K+</button>
      <button class="btn">book</button>
      <button class="btn">fook</button>
    </div>
  </div>
  <section class="datafile">
    <img class="preview" src="img/n/main12.gif" alt="náhľad: hmla nad Dunajom" width="240" height="300">
    <dl class="kv">
      <dt>súbor</dt><dd>hmla_nad_dunajom.tif</dd>
      <dt>veľkosť</dt><dd>48,2 MB</dd>
      <dt>typ</dt><dd>image/tiff, 6000 × 4000</dd>
      <dt>stiahnuté</dt><dd>37×</dd>
      <dt>kto môže</dt><dd>priatelia drienky</dd>
    </dl>
  </section>
{composer("napísať k súboru", "tvoja reakcia…")}
  <div class="thread-bar"><h2>3 reakcie</h2></div>
  <ol class="thread">
{comments}
  </ol>"""
write("data.html",
      "<!-- title: hmla_nad_dunajom.tif -->\n<!-- nav: people -->\n"
      "<!-- node: id=9184101; name=hmla_nad_dunajom.tif; template=data; parent=7004120|denník: drienka|blog.html; owner=drienka; "
      "viewers=slobo,ihla,ode; img=img/n/main12.gif; created=12.10.2026 07:15; updated=12.10.2026 07:15; perms=r :: friends -->\n"
      f'<main class="wrap" id="obsah">\n{body}\n</main>\n')
