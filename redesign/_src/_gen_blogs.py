"""Write blogs.html: the newest diary (denník) entries from everyone. A system node, like v2's /id/21."""
import html
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import icon  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
SEP = '<span class="sep">::</span>'

# (user, title, when, views, replies, K, excerpt)
ENTRIES = [
    ("drienka", "hmla nad Dunajom", "12.10.2026 07:12", 242, 3, 28, "Šiesta ráno z Apollo mosta. Dvadsať minút čakania na správne svetlo a jedna fotka, kým sa hmla zdvihla."),
    ("kremeň", "slová, ktoré sa nedajú preložiť", "11.10.2026 11:28", 180, 4, 9, "Zbieram ich do zošita: „ľúbozvučný“, „prieberčivý“, „otupený“. Kamarátka z Lipska mi za každé pošle nemecké, ktoré sa tiež nedá preložiť."),
    ("ode", "október v knihách", "10.10.2026 22:40", 96, 2, 6, "Tri knihy, dve dočítané. Tokarczuk je pomalá ako rieka a presne preto ju nechcem dočítať."),
    ("lemur", "keď mačka vytiahne kábel", "09.10.2026 23:12", 310, 11, 17, "Päť rokov uptime a jediný výpadok spôsobila mačka. Zálohy som dovtedy riešil teoreticky."),
    ("sova", "lávka, november, vietor", "08.10.2026 19:05", 74, 1, 3, "Nová lávka cez Dunaj je krásna, ale kto ju navrhol bez strechy, nikdy nešiel cez ňu v novembri."),
    ("paprika", "kvások, deň štrnásty", "07.10.2026 08:30", 201, 9, 14, "Volá sa Gertrúda, žerie ražnú múku a v sobotu konečne upiekla chlieb, ktorý sa dá jesť."),
    ("kvasar", "langoš tour, prvá zastávka", "05.10.2026 21:15", 158, 7, 12, "Liptovský Mikuláš, pri stanici. Cesnak povinný, syr hojný, čakanie dvadsať minút. Hodnotenie: dobrý, ale nie najlepší."),
]

items = "\n".join(f"""    <article class="entry">
      <div class="who-line"><img class="av s" src="{icon(u)}" alt="" width="25" height="25"><a href="blog.html">denník: {e(u)}</a></div>
      <h2><a href="submission.html">{e(t)}</a></h2>
      <div class="m"><a href="user.html">{e(u)}</a> {SEP} <a class="when" href="submission.html">{when}</a> {SEP} videné {v}× {SEP} {r} reakcií {SEP} <span class="k">{k} K</span></div>
      <p>{e(x)}</p>
    </article>""" for u, t, when, v, r, k, x in ENTRIES)

body = f"""  <div class="head"><h1>blogs</h1></div>
  <p class="blogs-own"><a class="btn" href="blog.html">tvoj denník</a></p>
  <div class="entries">
{items}
  </div>
  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie zápisy</a></nav>"""
io.open("blogs.html", "w", encoding="utf-8").write(
    "<!-- title: blogs -->\n<!-- nav: blogs -->\n"
    "<!-- node: id=21; name=blogs; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo -->\n"
    f'<main class="wrap" id="obsah">\n{body}\n</main>\n')
print("wrote blogs.html")
