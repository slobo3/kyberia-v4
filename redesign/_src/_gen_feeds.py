"""Write main, last, fr, RE, K, people and the mail list from _content.py. Run from anywhere."""
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import DATE, DAYS, FRIENDS, IDLE, LOCATION, MAIL, MAIN, POSTS, REPLIES, THREAD, THREAD_WITH, USERS, icon  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape


def av(user, cls="av"):
    return f'<img class="{cls}" src="{icon(user)}" alt="" width="50" height="50">'


def ulink(user):
    return f'<a href="user.html">{e(user)}</a>'


def sep():
    return '<span class="sep">::</span>'


def feed_item(p, score=True, show_day=False, rank=None):
    user, day, time, where, section, title, k, new, children, text = p
    when = f"{DATE[day]} {time}" if show_day else time
    t = f'<div class="ttl"><a href="submission.html">{e(title)}</a></div>' if title else ""
    nn = f' <span class="new">NEW</span>' if new else ""
    ch = f" {sep()} {children} children" if children else ""
    kk = f'<span class="k">{k} K</span>' if k else ""
    lead = f'<span class="rank">{rank}</span>' if rank else av(user)
    fook = '<button class="btn ghost">fook</button>' if rank else ""
    sc = f'<div class="score">{kk}<button class="btn">K+</button>{fook}</div>' if score else '<div class="score"></div>'
    return f"""<li>
  {lead}
  <div>
    <div class="where">v <a class="parent" href="forum.html">{e(where)}</a> {sep()} <a href="kyberia.html">{e(section)}</a></div>
    {t}
    <div class="by">{ulink(user)} {sep()} <a class="when" href="submission.html">{when}</a>{nn}</div>
    <p class="txt">{e(text)}</p>
  </div>
  {sc}
</li>"""


def feed_post(p, show_day=False):
    """last / fr: the same post component as a flat discussion, plus where it was written."""
    user, day, time, where, section, title, k, new, children, text = p
    when = f"{DATE[day]} {time}" if show_day else time
    kk = f' {sep()} <span class="k">{k} K</span>' if k else ""
    nn = f' {sep()} <span class="new">NEW</span>' if new else ""
    t = f'<div class="pt">{e(title)}</div>' if title else ""
    return f"""<li><article class="post">
  {av(user)}
  <div>
    <div class="ph"><a class="who" href="user.html">{e(user)}</a><input class="pick" type="checkbox" aria-label="vybrať"> <a class="when" href="submission.html">{when}</a>{kk}{nn}</div>
    <div class="pw">v <a href="forum.html">{e(where)}</a> {sep()} <a href="kyberia.html">{e(section)}</a></div>
    {t}
    <div class="pb"><p>{e(text)}</p></div>
    <div class="pa"><button class="btn">odpovedať</button><button class="btn">K+</button></div>
  </div>
</article></li>"""


def page(title, nav, node, body, side=""):
    s = f"<!-- title: {title} -->\n<!-- nav: {nav} -->\n<!-- node: {node} -->\n"
    if side:
        s += f"<!-- side -->\n{side}\n<!-- /side -->\n"
    return s + f'<main class="wrap" id="obsah">\n{body}\n</main>\n'


def write(name, text):
    io.open(name, "w", encoding="utf-8").write(text)
    print("wrote", name)


def head(h1):
    return f'  <div class="head">\n    <h1>{e(h1)}</h1>\n  </div>\n'


# ── last: everything, grouped by day ───────────────────────────────────────
posts = sorted(POSTS, key=lambda p: (p[1], [-int(x) for x in p[2].split(":")]))
body = head("last")
body += '  <div class="filters"><span class="seg" role="group" aria-label="filter"><a href="#" aria-current="true">všetko</a><a href="#">len nové</a><a href="#">bez ignorovaných</a></span></div>\n'
for day in sorted({p[1] for p in posts}):
    label = DAYS[day] if day < len(DAYS) else DATE[day]
    body += f'  <h2 class="day">{label}</h2>\n  <ol class="thread">\n' + "\n".join(feed_post(p) for p in posts if p[1] == day) + "\n  </ol>\n"
body += '  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>'
write("last.html", page("last", "last", "id=35; name=last; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,sklo,paprika,mrazik; details=no", body))

# ── fr: friends only ───────────────────────────────────────────────────────
fr = [p for p in posts if p[0] in FRIENDS]
body = head("fr") + '  <ol class="thread">\n' + "\n".join(feed_post(p, show_day=True) for p in fr) + '\n  </ol>\n  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>'
side = '      <section>\n        <h2>priatelia</h2>\n        <ul class="who-list">\n' + "\n".join(
    f'          <li>{av(u, "av s on" if i < 5 else "av s")}<span class="u">{u}</span><span class="idle">{"online" if i < 5 else IDLE[i * 3]}</span></li>'
    for i, u in enumerate(FRIENDS)) + "\n        </ul>\n      </section>"
write("fr.html", page("fr", "fr", "id=3576777; name=fr; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,anima; details=no", body, side))

# ── RE: replies to my nodes, rendered exactly like posts in a discussion ──
from _re_block import re_post  # noqa: E402
items = [re_post(icon, user, when, node, text, k, new) for user, when, node, quote, text, k, new in REPLIES]
body = head("RE") + '  <ol class="thread">\n' + "\n".join(items) + '\n  </ol>\n  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>'
write("re.html", page("RE", "RE", "id=3579407; name=RE; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo; details=no", body))

# ── K: ranked ──────────────────────────────────────────────────────────────
from _content import K_ITEMS  # noqa: E402
from _k_block import k_item  # noqa: E402
ranked = sorted(K_ITEMS, key=lambda it: -it[7])
body = head("K")
body += ('  <div class="filters">\n    <span class="seg" role="group" aria-label="obdobie"><a href="#" aria-current="true">24 h</a><a href="#">3 dni</a><a href="#">týždeň</a><a href="#">mesiac</a></span>\n'
         '    <span class="seg" role="group" aria-label="výber"><a href="#" aria-current="true">najviac K</a><a href="#">najnovšie K</a></span>\n  </div>\n')
body += '  <ol class="feed klist">\n' + "\n".join(k_item(i + 1, *it) for i, it in enumerate(ranked)) + "\n  </ol>"
side = """      <section>
        <h2>fook</h2>
        <ul class="links">
          <li><a href="forum.html">Slovenská politická scéna: denný súhrn</a> <button class="btn ghost">unfook</button></li>
          <li><a href="forum.html">Foto bazár: predám bicykel</a> <button class="btn ghost">unfook</button></li>
        </ul>
      </section>
      <section>
        <h2>komu dávaš K</h2>
        <ul class="who-list">
""" + "\n".join(f'          <li>{av(u, "av s")}<span class="u">{u}</span><span class="idle">{k} K</span></li>'
                for u, k in (("anima", 31), ("polly", 18), ("drienka", 14), ("kremeň", 11), ("paprika", 9), ("lemur", 7))) + """
        </ul>
      </section>"""
write("k.html", page("K", "K", "id=15; name=K; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,lemur,anima", body))

# ── people ─────────────────────────────────────────────────────────────────
others = [u for u in USERS if u not in FRIENDS]


def person(u, i, online_mark):
    cls = "av on" if online_mark else "av"
    return f'      <li>{av(u, cls)}<span><span class="u">{u}</span><span class="loc">v <a href="forum.html">{e(LOCATION[u])}</a></span><span class="idle">{IDLE[i % len(IDLE)]}</span></span></li>'


hot = [("bookmarks", 96), ("last", 41), ("mail", 38), ("Kyberia session 2026", 17), ("Slovenská politická scéna", 14),
       ("K", 12), ("bratislava", 11), ("BUGLIST", 9), ("Mestá a doprava", 8), ("fotka dňa", 7)]
body = head("people")
body += '  <section class="block">\n    <h2 class="day">kde je najviac ľudí</h2>\n    <ul class="hot">\n' + "\n".join(
    f'      <li><a href="forum.html">{e(n)} <b>{c}</b></a></li>' for n, c in hot) + "\n    </ul>\n  </section>\n"
body += '  <section class="block">\n    <h2 class="day">priatelia</h2>\n    <ul class="people">\n' + "\n".join(person(u, i * 2, True) for i, u in enumerate(FRIENDS)) + "\n    </ul>\n  </section>\n"
body += '  <section class="block">\n    <h2 class="day">ostatní</h2>\n    <ul class="people">\n' + "\n".join(person(u, i, False) for i, u in enumerate(others)) + '\n    </ul>\n    <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">ďalších 391</a></nav>\n  </section>'
write("people.html", page("people", "people", "id=27; name=people; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,mrazik,lemur", body))

# ── mail: conversations on the left, the open one on the right (newest first) ──
convs = []
for i, (u, last, mine, when, unread) in enumerate(MAIL):
    cur = ' aria-current="true"' if u == THREAD_WITH else ""
    badge = f' <span class="new">{unread}</span>' if unread else ""
    convs.append(f'        <li><a href="#"{cur}><span class="u">{u}</span><span class="t">{when}{badge}</span>'
                 f'<span class="last">{"ty: " if mine else ""}{e(last)}</span></a></li>')
msgs = []
for frm, day, time, where, text, new in reversed(THREAD):
    nn = ' <span class="new">NEW</span>' if new else ""
    me = " me" if frm == "slobo" else ""
    who = f'<a class="who" href="user.html">{frm}</a>'
    meta = f'{nn} {day} {time} {sep()} z {e(where)} {who}' if me else f'{who} {day} {time} {sep()} z {e(where)}{nn}'
    msgs.append(f'        <li class="msg{me}"><div class="mh">{meta}</div>'
                f'<p class="mb">{e(text)}</p></li>')
body = head("mail") + f"""  <div class="mail">
    <nav class="convos" aria-label="konverzácie">
      <a class="btn primary newmail" href="mail-new.html">+ nová správa</a>
      <ul>
{chr(10).join(convs)}
      </ul>
    </nav>
    <section class="stream" aria-label="konverzácia s {THREAD_WITH}">
      <header><a class="u" href="user.html">{THREAD_WITH}</a> <span class="loc">online {sep()} teraz v mail</span></header>
      <form class="reply" aria-label="napísať {THREAD_WITH}">
        <textarea class="field" placeholder="napíš {THREAD_WITH}…" aria-label="správa"></textarea>
        <button class="btn primary" type="submit">poslať</button>
      </form>
      <ol class="msgs">
{chr(10).join(msgs)}
      </ol>
    </section>
  </div>"""
write("mail.html", page("mail", "mail", "id=24; name=mail; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,kvasar,kremeň; details=no", body))

# main is generated by _gen_main.py
