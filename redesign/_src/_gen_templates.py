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
COST = ''


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
      "<!-- title: Prečo sa mestské stromy oplatia viac ako klimatizácia -->\n<!-- nav: node -->\n"
      "<!-- node: id=9185501; name=Prečo sa mestské stromy oplatia…; template=submission; parent=63611|Veda a technológie|kyberia.html; "
      "owner=anima; viewers=slobo,cín,mrak,lemur; img=img/n/main0.gif; created=12.10.2026 09:14; updated=12.10.2026 09:31; perms=r, w :: public -->\n"
      f'<main class="wrap" id="obsah">\n{body}\n</main>\n')

# ── blog: a user's diary (denník) is a forum; each entry is a forum post (child node), shown in full ──
from _blogdata import DRIENKA, IMG, POSTPAGE, REPLIES as BLOG_REPLIES  # noqa: E402


def block(b):
    if b[0] == IMG:
        return f'<figure class="bimg"><img src="{b[1]}" alt="{e(b[2])}" width="640" height="420"><figcaption>{e(b[2])}</figcaption></figure>'
    return f"<p>{e(b[1])}</p>"


entries = "\n".join(f"""    <article class="entry full">
      <h2><a href="{POSTPAGE[t]}">{e(t)}</a></h2>
      <div class="m"><a href="user.html">drienka</a> {SEP} <a class="when" href="{POSTPAGE[t]}">{when}</a> {SEP} videné {views}× {SEP} <a href="{POSTPAGE[t]}">{subs} reakcií</a></div>
      {"".join(block(b) for b in blocks)}
      <div class="pa"><a class="btn ghost" href="{POSTPAGE[t]}">odpovedať</a></div>
    </article>""" for t, when, views, subs, blocks in DRIENKA)
body = f"""  <div class="head">
    <h1>denník: drienka</h1>
    <div class="actions">
      <span class="k ksum">97 K</span>
      <button class="btn">K+</button>
      <button class="btn">book</button>
      <button class="btn">fook</button>
    </div>
  </div>
{composer("pridať zápis do denníka", "o čom dnes…", "názov zápisu")}
  <div class="entries">
{entries}
  </div>
  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie zápisy</a></nav>"""
write("blog.html",
      "<!-- title: denník: drienka -->\n<!-- nav: node -->\n"
      "<!-- node: id=7004120; name=denník: drienka; template=forum; parent=7004001|drienka|user.html; owner=drienka; "
      "viewers=slobo,ihla,ode; img=img/u/drienka.gif; created=14.03.2019 20:10; updated=12.10.2026 07:12; perms=r :: public -->\n"
      f'<main class="wrap" id="obsah">\n{body}\n</main>\n')

# each diary entry on its own: a forum post node (template submission). The title is the node name and the
# node column carries owner and dates, so the page is just the text, then the replies at the bottom.
for i, (t, when, views, subs, blocks) in enumerate(DRIENKA):
    reps = BLOG_REPLIES.get(t, [])
    items = []  # level-2 replies nest under the reply before them
    for u, w, x, k, n, lv in reps:
        if lv == 2 and items:
            items[-1][1].append(post(u, w, x, "Re[2]: " + t, k=k, new=n, level=2))
        else:
            items.append(((u, w, x, k, n), []))
    thread = "\n".join(post(u, w, x, "Re: " + t, k=k, new=n, level=1, children="\n".join(kids)) for (u, w, x, k, n), kids in items)
    more = '\n  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>' if subs > len(reps) else ""
    body = f"""  <div class="head">
    <h1>{e(t)}</h1>
    <div class="actions">
      <button class="btn">K+</button>
      <button class="btn">book</button>
      <button class="btn">fook</button>
    </div>
  </div>
  <section class="topic prose blogpost">
    {"".join(block(b) for b in blocks)}
  </section>
  <div class="thread-bar"><h2>{subs} reakcií</h2></div>
  <ol class="thread">
{thread}
  </ol>{more}
{composer("odpovedať na zápis", "tvoja reakcia…")}"""
    write(POSTPAGE[t],
          f"<!-- title: {t} -->\n<!-- nav: node -->\n"
          f"<!-- node: id={9184100 - i * 1731}; name={t}; template=submission; parent=7004120|denník: drienka|blog.html; owner=drienka; "
          f"viewers=slobo,ihla,ode; img=img/u/drienka.gif; created={when}; updated={when}; perms=r :: public -->\n"
          f'<main class="wrap" id="obsah">\n{body}\n</main>\n')

# ── data: a file node (uploaded file with its own access rights) ──────────
comments = (
    post("ihla", "12.10.2026 10:15", "Plné rozlíšenie je krásne, v tom tife je vidieť každé zrnko.", "Re: hmla_nad_dunajom.tif", k=4, level=1)
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
      <dt>veľkosť</dt><dd>48,2 MB</dd>
      <dt>typ</dt><dd>image/tiff, 6000 × 4000</dd>
      <dt>stiahnuté</dt><dd>37×</dd>
    </dl>
  </section>
{composer("napísať k súboru", "tvoja reakcia…")}
  <div class="thread-bar"><h2>1 reakcia</h2></div>
  <ol class="thread">
{comments}
  </ol>"""
write("data.html",
      "<!-- title: hmla_nad_dunajom.tif -->\n<!-- nav: node -->\n"
      "<!-- node: id=9184101; name=hmla_nad_dunajom.tif; template=data; parent=9184100|hmla nad Dunajom|zapis-hmla.html; owner=drienka; "
      "viewers=slobo,ihla,ode; img=img/n/main12.gif; created=12.10.2026 07:15; updated=12.10.2026 07:15; perms=r :: friends -->\n"
      f'<main class="wrap" id="obsah">\n{body}\n</main>\n')
