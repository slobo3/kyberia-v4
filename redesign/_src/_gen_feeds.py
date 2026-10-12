"""Write main, last, fr, RE, K, people and the mail list from _content.py. Run from anywhere."""
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import DATE, DAYS, FRIENDS, IDLE, LOCATION, MAIL, MAIN, POSTS, REPLIES, THREAD, THREAD_WITH, USERS  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape


def av(user, cls="av"):
    return f'<span class="{cls}" style="--h:{USERS[user]}" aria-hidden="true">{user[0]}</span>'


def ulink(user):
    return f'<a href="user.html">{e(user)}</a>'


def sep():
    return '<span class="sep">::</span>'


def feed_item(p, score=True, show_day=False, rank=None):
    user, day, time, where, section, title, k, new, children, text = p
    when = f"{DATE[day]} {time}" if show_day else time
    t = f'<div class="ttl">{e(title)}</div>' if title else ""
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
    <div class="by">{ulink(user)} {sep()} {when}{ch}{nn}</div>
    <p class="txt">{e(text)}</p>
  </div>
  {sc}
</li>"""


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
    body += f'  <h2 class="day">{label}</h2>\n  <ol class="feed">\n' + "\n".join(feed_item(p) for p in posts if p[1] == day) + "\n  </ol>\n"
body += '  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>'
write("last.html", page("last", "last", "id=35; name=last; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,sklo,paprika,mrazik", body))

# ── fr: friends only ───────────────────────────────────────────────────────
fr = [p for p in posts if p[0] in FRIENDS]
body = head("fr") + '  <ol class="feed">\n' + "\n".join(feed_item(p, show_day=True) for p in fr) + '\n  </ol>\n  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>'
side = '      <section>\n        <h2>priatelia</h2>\n        <ul class="who-list">\n' + "\n".join(
    f'          <li>{av(u, "av s on" if i < 5 else "av s")}<span class="u">{u}</span><span class="idle">{"online" if i < 5 else IDLE[i * 3]}</span></li>'
    for i, u in enumerate(FRIENDS)) + "\n        </ul>\n      </section>"
write("fr.html", page("fr", "fr", "id=3576777; name=fr; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,anima", body, side))

# ── RE: replies to my nodes ────────────────────────────────────────────────
items = []
for user, when, node, quote, text, k, new in REPLIES:
    kk = f'<span class="k">{k} K</span>' if k else ""
    nn = ' <span class="new">NEW</span>' if new else ""
    items.append(f"""<li>
  {av(user)}
  <div>
    <blockquote class="mine"><a href="forum.html">{e(node)}</a> {sep()} „…{e(quote)}…“</blockquote>
    <div class="by">{ulink(user)} {sep()} {when}{nn}</div>
    <p class="txt">{e(text)}</p>
  </div>
  <div class="score">{kk}<button class="btn">odpovedať</button></div>
</li>""")
body = head("RE") + '  <ol class="feed replies">\n' + "\n".join(items) + '\n  </ol>\n  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>'
write("re.html", page("RE", "RE", "id=3579407; name=RE; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo", body))

# ── K: ranked ──────────────────────────────────────────────────────────────
ranked = sorted([p for p in POSTS if p[6]], key=lambda p: -p[6])[:15]
body = head("K")
body += ('  <div class="filters">\n    <span class="seg" role="group" aria-label="obdobie"><a href="#" aria-current="true">24 h</a><a href="#">3 dni</a><a href="#">týždeň</a><a href="#">mesiac</a></span>\n'
         '    <span class="seg" role="group" aria-label="výber"><a href="#" aria-current="true">všetko</a><a href="#">kNEW</a></span>\n  </div>\n')
body += '  <ol class="feed klist">\n' + "\n".join(feed_item(p, show_day=True, rank=i + 1) for i, p in enumerate(ranked)) + "\n  </ol>"
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
write("k.html", page("K", "K", "id=15; name=K; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,lemur,anima", body, side))

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
    msgs.append(f'        <li class="msg{me}"><div class="mh"><a class="who" href="user.html">{frm}</a> {day} {time} {sep()} z {e(where)}{nn}</div>'
                f'<p class="mb">{e(text)}</p></li>')
body = head("mail") + f"""  <div class="mail">
    <nav class="convos" aria-label="konverzácie">
      <input class="field" type="search" placeholder="komu napísať" aria-label="komu napísať">
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
write("mail.html", page("mail", "mail", "id=24; name=mail; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo,kvasar,kremeň", body))

# ── main: the front page (doesn't rhyme on purpose) ────────────────────────
lead = MAIN[0]
rest = sorted(MAIN[1:], key=lambda r: (int(r[3].split('.')[1]), int(r[3].split('.')[0])), reverse=True)
k_today = sorted([p for p in POSTS if p[1] <= 1 and p[6]], key=lambda p: -p[6])[:10]
busy = sorted([p for p in POSTS if p[1] <= 1], key=lambda p: -p[8])[:8]


def main_row(t, u, sec, d, k, new):
    nn = f' <span class="new">{new} new</span>' if new else ""
    return f'      <li><a class="t" href="forum.html">{e(t)}</a><span class="m">{ulink(u)} {sep()} {e(sec)} {sep()} {d}{nn}</span><span class="k">{k} K</span></li>'


body = f"""  <header class="front">
    <img class="logo" src="img/kyberia.gif" alt="kyberia.sk">
    <h1>Something smarter than us is going to emerge</h1>
  </header>

  <article class="leadstory">
    <div class="m">{ulink(lead[1])} {sep()} {e(lead[2])} {sep()} {lead[3]} <span class="new">{lead[5]} new</span></div>
    <h2><a href="forum.html">{e(lead[0])}</a></h2>
    <p>{e(lead[6])}</p>
    <span class="k">{lead[4]} K</span>
  </article>

  <div class="frontcols">
    <section>
      <h2 class="day">na main</h2>
      <ol class="mainlist">
{chr(10).join(main_row(*r[:6]) for r in rest)}
      </ol>
      <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>
    </section>
    <aside>
      <h2 class="day"><a href="k.html">K dnes</a></h2>
      <ol class="ranked compact">
{chr(10).join(f'        <li><a href="forum.html">{e(p[5] or p[3])}</a><span class="k">{p[6]} K</span></li>' for p in k_today)}
      </ol>
      <h2 class="day"><a href="last.html">kde sa píše</a></h2>
      <ol class="compact">
{chr(10).join(f'        <li><a href="forum.html">{e(re.sub(r'^Re(\[\d+\])?: ', '', p[5] or p[3]))}</a><span class="g2">{p[8]}</span></li>' for p in busy)}
      </ol>
    </aside>
  </div>"""
write("main.html", "<!-- title: main -->\n<!-- nav: main -->\n<!-- layout: free -->\n" + f'<main class="wrap front-page" id="obsah">\n{body}\n</main>\n')
