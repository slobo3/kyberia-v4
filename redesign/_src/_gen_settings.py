"""Write conf.html (configure a node), setup.html (my settings), mail-new.html (write to someone new)."""
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import FRIENDS, MAIL, icon  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape


def write(name, text):
    io.open(name, "w", encoding="utf-8").write(text)
    print("wrote", name)


def row(label, control, action="", hint=""):
    h = f'<p class="hint">{hint}</p>' if hint else ""
    a = f'<button class="btn" type="button">{action}</button>' if action else ""
    return f"""      <div class="setrow">
        <div class="setlabel">{label}</div>
        <div class="setctl">{control}{h}</div>
        <div class="setact">{a}</div>
      </div>"""


def section(title, rows):
    return f'    <section class="setsec">\n      <h2>{title}</h2>\n' + "\n".join(rows) + "\n    </section>"


# ── conf: configure a node you own ────────────────────────────────────────
# Rights on kyberia are named lists on the node (as seen on /commanders): masters, ops, access, execute,
# bans, silence. Each holds users by number; membership lasts until removed (no time limits).
from _content import USER_ID  # noqa: E402
LISTS = [
    ("masters", "spravujú nódu: nastavenia aj tieto zoznamy", ["kvasar"]),
    ("ops", "moderujú: silence, bans, presúvanie príspevkov", ["lemur", "tichá_voda"]),
    ("access", "smú dnu, keď je nóda private", []),
    ("execute", "smú spúšťať template tejto nódy", []),
    ("bans", "nemajú do nódy prístup", ["vlnka"]),
    ("silence", "čítajú, ale nepíšu", ["mrak"]),
]


def person_row(u, rights):
    who = f'<span class="person"><img class="av xs" src="{icon(u)}" alt="">{e(u)} <span class="uid">[{USER_ID[u]}]</span></span>'
    chips = "".join(f'<span class="tag">{r}<button class="btn ghost" type="button" aria-label="odobrať {r} pre {e(u)}">×</button></span>' for r in rights)
    return row(who, f'<div class="tags">{chips}</div>')


# práva as a list of people, each with the lists they're on; adding says which right you give
PEOPLE = {}
for name, _hint, users in LISTS:
    for u in users:
        PEOPLE.setdefault(u, []).append(name)
rights_rows = [person_row(u, rs) for u, rs in PEOPLE.items()]
opts = "".join(f"<option>{n}: {h}</option>" for n, h, _ in LISTS)
rights_rows.append(row("pridať",
    '<span class="adder"><input class="field num id" value="7004016" inputmode="numeric" aria-label="číslo používateľa">'
    f'<select class="field" aria-label="aké právo">{opts}</select>'
    '<button class="btn" type="button">pridať</button></span><p class="nodetitle"><a href="user.html">papraď</a></p>'))


conf_body = f"""  <div class="head">
    <h1>configure</h1>
  </div>
  <div class="settings">
{section("obsah", [
    row("text", '<textarea class="field" rows="8">Tu sa rieši redizajn kyberie: farby ostávajú, písmo a rozostupy sú nové. Návrhy, bugy a nápady píšte sem.</textarea><span class="radios"><label class="check"><input type="checkbox"> bez HTML</label><label class="check"><input type="checkbox" checked> nl2br</label></span>'),
])}
{section("názov", [
    row("názov", '<input class="field" value="&lt;b&gt;kyberia v4&lt;/b&gt;: redizajn">', hint='<span class="preview"><b>kyberia v4</b>: redizajn</span>'),
])}
{section("obrázok nódy", [
    row("obrázok", '<span class="imgpick"><img src="img/kyberia.gif" alt="" width="62" height="77"><input type="file" aria-label="nový obrázok"></span>'),
])}
{section("template", [
    # templates are nodes too: picked by number like parent (4 = forum, as on kyberia)
    row("template", '<input class="field num id" value="4" inputmode="numeric" aria-label="číslo template nódy">'
                    '<p class="nodetitle"><a href="forum.html">forum</a></p>'),
])}
{section("umiestnenie", [
    row("parent", '<input class="field num id" value="63540" inputmode="numeric" aria-label="číslo nódy, kam presunúť">'
                  '<p class="nodetitle"><a href="kyberia.html">Compz &amp; Net</a></p>'),
])}
{section("prístup", [
    row("system", '<span class="radios"><label><input type="radio" name="acc" checked> public</label><label><input type="radio" name="acc"> moderated</label><label><input type="radio" name="acc"> private</label></span>'),
    row("external access", '<label class="check"><input type="checkbox"> viditeľná aj pre neprihlásených</label>'),
])}
{section("práva", rights_rows)}
  </div>
  <div class="savebar"><a class="btn ghost" href="forum.html">zrušiť</a><button class="btn primary" type="submit">uložiť zmeny</button></div>"""
write("conf.html",
      "<!-- title: configure :: kyberia v4 -->\n<!-- nav: node -->\n"
      "<!-- node: id=9190001; name=kyberia v4: redizajn; template=forum; parent=63540|Compz & Net|kyberia.html; owner=slobo; "
      "viewers=slobo,kvasar,lemur; img=img/kyberia.gif; created=01.10.2026 20:00; updated=12.10.2026 20:02; perms=r, w, owner :: public -->\n"
      f'<main class="wrap" id="obsah">\n{conf_body}\n</main>\n')

# ── setup: my own settings ────────────────────────────────────────────────
ignored = "".join(f'<span class="tag">{u} <button class="btn ghost" type="button" aria-label="zrušiť ignore {u}">×</button></span>' for u in ("vlnka", "bager"))
setup_body = f"""  <div class="head"><h1>setup</h1></div>
  <div class="settings">
{section("ty", [
    row("ikona", f'<span class="imgpick"><img class="av" src="{icon("slobo")}" alt="" width="50" height="50"><input type="file" aria-label="nová ikona"></span>'),
    row("mood", '<input class="field" value="redizajnujem kyberiu">'),
])}
{section("mail", [
    row("e-mail", '<input class="field" type="email" value="slobo@example.org">'),
])}
{section("čítanie", [
    row("na stranu", '<input class="field num" value="200" inputmode="numeric">'),
    row("poradie", '<select class="field"><option>najnovšie hore</option><option>najstaršie hore</option></select>'),
])}
{section("súkromie", [
    row("bookmarks", '<label class="check"><input type="checkbox" checked> ostatní vidia moje bookmarks</label>'),
    row("movement", '<label class="check"><input type="checkbox" checked> ostatní vidia, kde chodím</label>'),
])}
{section("ignore", [
    row("ignoruješ", f'<span class="tags">{ignored}</span><input class="field num id" value="7004021" inputmode="numeric" aria-label="číslo používateľa"><p class="nodetitle"><a href="user.html">mrak</a></p>', "pridať"),
])}
{section("heslo", [
    row("staré heslo", '<input class="field" type="password" autocomplete="current-password">', ""),
    row("nové heslo", '<input class="field" type="password" autocomplete="new-password">', ""),
    row("ešte raz", '<input class="field" type="password" autocomplete="new-password">', "zmeniť heslo"),
])}
  </div>
  <div class="savebar"><a class="btn ghost" href="main.html">zrušiť</a><button class="btn primary" type="submit">uložiť zmeny</button></div>"""
write("setup.html",
      "<!-- title: setup -->\n<!-- nav: node -->\n"
      "<!-- node: id=5001001; name=slobo; template=user; parent=||; owner=slobo; viewers=slobo; "
      "img=img/u/slobo.gif; created=06.10.2014 23:38; updated=12.10.2026 20:02; perms=r, w, owner :: private -->\n"
      f'<main class="wrap" id="obsah">\n{setup_body}\n</main>\n')

# ── mail-new: write to someone you haven't mailed yet ─────────────────────
convs = "\n".join(
    f'        <li><a href="mail.html"><span class="u">{u}</span><span class="t">{when}{f" <span class=new>{unread}</span>" if unread else ""}</span>'
    f'<span class="last">{"ty: " if mine else ""}{e(last)}</span></a></li>'
    for u, last, mine, when, unread in MAIL)
sugg = "\n".join(f'          <li><a href="#"><img class="av s" src="{icon(u)}" alt="" width="25" height="25"><span>{u}</span></a></li>'
                 for u in ("paprika", "papraď", "plachta"))
new_body = f"""  <h1 class="sr">mail</h1>
  <div class="mail">
    <nav class="convos" aria-label="konverzácie">
      <a class="btn primary newmail" href="mail-new.html" aria-current="true">+ nová správa</a>
      <ul>
{convs}
      </ul>
    </nav>
    <section class="stream" aria-label="nová správa">
      <header><span class="u">nová správa</span></header>
      <form class="newmsg" aria-label="nová správa">
        <label class="lab" for="komu">komu</label>
        <input id="komu" class="field" value="pa" autocomplete="off">
        <ul class="suggest" aria-label="návrhy">
{sugg}
        </ul>
        <label class="lab" for="msg">správa</label>
        <textarea id="msg" class="field" rows="6" placeholder="napíš…"></textarea>
        <div class="send"><span class="g2">prvá správa novému človeku</span><button class="btn primary" type="submit">poslať</button></div>
      </form>
    </section>
  </div>"""
write("mail-new.html",
      "<!-- title: nová správa -->\n<!-- nav: mail -->\n"
      "<!-- node: id=24; name=mail; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo -->\n"
      f'<main class="wrap" id="obsah">\n{new_body}\n</main>\n')
