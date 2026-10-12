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


# ── submission: one discussion reply opened as its own node (click a post's title in diskusia) ──
# kvasar's reply in Kyberia session 2026: the title is the node name, the text is its content, its replies below.
replies = post("bgdny", "12.10.2026 21:03", "Dohodnuté. Langoš je povinný.", "Re[2]: Kyberia session 2026", k=2, level=1)
body = f"""  <div class="head">
    <h1>Re: Kyberia session 2026</h1>
    <div class="actions">
      <button class="btn">K+</button>
      <button class="btn">book</button>
      <button class="btn">fook</button>
    </div>
  </div>
  <section class="topic prose">
    <p>Beriem jedno miesto, ďakujem. Platím benzín aj langoš.</p>
  </section>
  <div class="thread-bar"><h2>1 reakcia</h2></div>
  <ol class="thread">
{replies}
  </ol>
{composer("odpovedať na príspevok", "tvoja reakcia…")}"""
write("submission.html",
      "<!-- title: Re: Kyberia session 2026 -->\n<!-- nav: node -->\n"
      "<!-- node: id=9184840; name=Re: Kyberia session 2026; template=submission; parent=9184811|Kyberia session 2026|forum.html; "
      "owner=kvasar; viewers=slobo,bgdny,kvasar; img=img/u/kvasar.gif; created=12.10.2026 20:52; updated=12.10.2026 20:52; perms=r, w :: public -->\n"
      f'<main class="wrap" id="obsah">\n{body}\n</main>\n')

# ── blog: each blog is its own node (template blog) under its author; blogs lists the newest ──
from _blogdata import DRIENKA, IMG, POSTPAGE, REPLIES as BLOG_REPLIES  # noqa: E402


def block(b):
    if b[0] == IMG:
        return f'<figure class="bimg"><img src="{b[1]}" alt="{e(b[2])}" width="640" height="420"><figcaption>{e(b[2])}</figcaption></figure>'
    return f"<p>{e(b[1])}</p>"


# The title is the node name and the node column carries owner and dates, so the page is just the text and
# photos, then the replies, then the reply form.
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
{composer("odpovedať na blog", "tvoja reakcia…")}"""
    write(POSTPAGE[t],
          f"<!-- title: {t} -->\n<!-- nav: node -->\n"
          f"<!-- node: id={9184100 - i * 1731}; name={t}; template=blog; parent=7004001|drienka|user.html; owner=drienka; "
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
