"""Write stats.html, source.html, commanders.html for the kyberia node (101). Run from anywhere."""
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import icon  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
SEP = '<span class="sep">::</span>'
NODE = ("<!-- node: id=101; name=kyberia; template=nodeshell; parent=1|main|main.html; owner=fiktivny_admin; "
        "viewers=slobo,anima,bgdny,polly,ode; img=img/kyberia.gif; created=21.09.2005 01:41; updated=18.04.2025 14:40; perms=r :: moderated -->\n")


def write(name, title, body):
    io.open(name, "w", encoding="utf-8").write(f"<!-- title: {title} -->\n<!-- nav: node -->\n{NODE}<main class=\"wrap\" id=\"obsah\">\n{body}\n</main>\n")
    print("wrote", name)


def head(title):
    return f'  <div class="head">\n    <h1>{title}</h1>\n    <p class="crumbs">nóda <a href="kyberia.html">kyberia</a></p>\n  </div>\n'


def who(u, right):
    return f'<li><img class="av s" src="{icon(u)}" alt="" width="25" height="25"><a href="user.html">{e(u)}</a><span>{right}</span></li>'


# ── stats ────────────────────────────────────────────────────────────────
# As on kyberia (/id/{n}/1961037, by_visit, by_K): the node's visitor list. One row per person:
# last visit, (N) NEW = items new for them here, booked = has it in bookmarks, K = gave the node K, visit count.
# Three orderings of the same list: by last visit (default), by visits, by K (only those who gave K).
VISITS = [  # (user, last visit, new for them, booked, gave K, visits)
    ("slobo", "12.10.2026 22:44", 0, True, False, 666), ("anima", "12.10.2026 22:22", 0, True, True, 241),
    ("bgdny", "12.10.2026 21:56", 0, False, False, 188), ("kvasar", "12.10.2026 21:27", 0, True, True, 1169),
    ("polly", "12.10.2026 21:23", 0, True, False, 892), ("ode", "12.10.2026 21:23", 2, False, False, 159),
    ("sova", "12.10.2026 20:09", 4, True, False, 83), ("lemur", "12.10.2026 18:40", 0, False, True, 412),
    ("drienka", "12.10.2026 07:12", 11, True, True, 1890), ("kremeň", "11.10.2026 23:02", 17, False, True, 774),
    ("hmlovina", "11.10.2026 14:03", 23, True, True, 979), ("paprika", "10.10.2026 09:30", 41, False, False, 120),
    ("mrazik", "08.10.2026 19:45", 66, False, False, 64), ("ihla", "03.10.2026 10:43", 120, True, True, 551),
    ("tichá_voda", "17.09.2026 13:42", 318, False, True, 240), ("k22", "22.04.2026 19:55", 2904, False, False, 3191),
    ("rezbár", "22.04.2025 14:12", 9120, False, False, 2678),
]


def visit_row(u, last, new, booked, k, visits, rank=None):
    flags = "".join(f'<span class="flag">{f}</span>' for f, on in (("booked", booked), ("K", k)) if on)
    nn = f'<span class="new">{new} new</span>' if new else '<span class="none">0 new</span>'
    r = f'<span class="rank">{rank}</span>' if rank else ""
    return (f'      <li>{r}<img class="av s" src="{icon(u)}" alt="" width="25" height="25"><a href="user.html">{e(u)}</a>'
            f'<span class="when">{last}</span>{nn}<span class="flags">{flags}</span><span class="cnt">{visits} visitz</span></li>')


rows = "\n".join(visit_row(*v) for v in VISITS)
stats = head("stats") + f"""  <div class="filters">
    <span class="seg" role="group" aria-label="zoradiť"><a href="#" aria-current="true">posledná návšteva</a><a href="#">návštevy</a><a href="#">K</a></span>
  </div>
  <ol class="visits">
{rows}
  </ol>
  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">ďalší</a></nav>"""
write("stats.html", "stats :: kyberia", stats)

# ── source: the node's raw HTML ──────────────────────────────────────────
kyb = io.open("kyberia.html", encoding="utf-8").read()
topic = re.search(r'<section class="topic prose">(.*?)</section>', kyb, re.S).group(1)
topic = "\n".join(line[8:] if line.startswith("        ") else line.strip() for line in topic.strip("\n").splitlines())
source = head("source") + f"""  <dl class="kv srcmeta">
    <dt>template</dt><dd>nodeshell</dd>
    <dt>formát</dt><dd>HTML :: nl2br vypnuté</dd>
    <dt>dĺžka</dt><dd>{len(topic)} znakov</dd>
  </dl>
  <pre class="source"><code>{e(topic)}</code></pre>"""
write("source.html", "source :: kyberia", source)

# ── commanders: the node's rights lists, as on kyberia (masters, ops, execute, access, bans, silence) ──
from _content import USER_ID  # noqa: E402
CMD = [
    ("masters", ["tichá_voda", "kompas", "hmlovina"]),
    ("ops", ["mráz", "plachta", "ode", "sova"]),
    ("execute", []),
    ("access", []),
    ("bans", ["vlnka"]),
    ("silence", ["kvasar", "sklo"]),
]


def member(u):
    return (f'<li><img class="av s" src="{icon(u)}" alt="" width="25" height="25"><a href="user.html">{e(u)}</a>'
            f'<span class="uid">[{USER_ID[u]}]</span></li>')


owner = ('<li><span class="av s ph" aria-hidden="true">f</span><a href="user.html">fiktivny_admin</a>'
         f'<span class="uid">[{USER_ID["fiktivny_admin"]}]</span></li>')
NL = "\n"
blocks = [f'  <section class="statsec"><h2>owner::</h2><ol class="whos">{NL}{owner}{NL}  </ol></section>']
for name, users in CMD:
    items = NL.join(member(u) for u in users) if users else '<li class="none">nikto</li>'
    blocks.append(f'  <section class="statsec"><h2>{name}::</h2><ol class="whos">{NL}{items}{NL}  </ol></section>')
commanders = head("commanders") + NL.join(blocks)
write("commanders.html", "commanders :: kyberia", commanders)
