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
days = [("29.9.", 812), ("30.9.", 790), ("1.10.", 845), ("2.10.", 901), ("3.10.", 760), ("4.10.", 512), ("5.10.", 498),
        ("6.10.", 870), ("7.10.", 905), ("8.10.", 880), ("9.10.", 932), ("10.10.", 799), ("11.10.", 560), ("12.10.", 1104)]
top = max(v for _, v in days)
bars = "\n".join(f'      <li><span class="bar" style="--v:{v / top:.3f}" title="{v} návštev"></span><span class="d">{d}</span></li>' for d, v in days)
visitors = "\n".join(who(u, f"{n}×") for u, n in (("anima", 412), ("bgdny", 388), ("polly", 301), ("kvasar", 287), ("ode", 240), ("sova", 199)))
kgivers = "\n".join(who(u, f'<span class="k">{n} K</span>') for u, n in (("drienka", 14), ("kremeň", 11), ("lemur", 9), ("anima", 7), ("paprika", 5)))
stats = head("stats") + f"""  <dl class="bignums">
    <div><dt>children</dt><dd>700</dd></div>
    <div><dt>descendants</dt><dd>4 310 058</dd></div>
    <div><dt>K</dt><dd class="k">120 K</dd></div>
    <div><dt>návštevy dnes</dt><dd>1 104</dd></div>
  </dl>
  <section class="statsec">
    <h2>návštevy, posledných 14 dní</h2>
    <ol class="bars">
{bars}
    </ol>
  </section>
  <div class="statcols">
    <section class="statsec"><h2>najčastejšie tu</h2><ol class="whos">
{visitors}
    </ol></section>
    <section class="statsec"><h2>najviac K dali</h2><ol class="whos">
{kgivers}
    </ol></section>
  </div>"""
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

# ── commanders: who runs this node ───────────────────────────────────────
masters = "\n".join(who(u, "master") for u in ("tichá_voda", "kompas"))
operators = "\n".join(who(u, "operator") for u in ("mráz", "plachta", "hmlovina"))
silenced = "\n".join(f'<li><img class="av s" src="{icon(u)}" alt="" width="25" height="25"><a href="user.html">{u}</a>'
                     f'<span>do {until} {SEP} <a href="forum.html">odôvodnenie</a></span></li>'
                     for u, until in (("kvasar", "13.10. 01:02"), ("sklo", "13.10. 01:02")))
commanders = head("commanders") + f"""  <section class="statsec"><h2>owner</h2><ol class="whos">
{who("fiktivny_admin", "owner") if False else '<li><span class="av s ph" aria-hidden="true">f</span><a href="user.html">fiktivny_admin</a><span>owner</span></li>'}
  </ol></section>
  <section class="statsec"><h2>masters</h2><ol class="whos">
{masters}
  </ol></section>
  <section class="statsec"><h2>operators</h2><ol class="whos">
{operators}
  </ol></section>
  <section class="statsec"><h2>silence</h2><ol class="whos">
{silenced}
  </ol></section>"""
write("commanders.html", "commanders :: kyberia", commanders)
