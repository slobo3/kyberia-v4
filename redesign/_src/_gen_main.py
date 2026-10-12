"""Write _src/main.html: the front page (the one page that doesn't rhyme). Run from anywhere."""
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import FRIENDS, LOCATION, MAIN, POSTS, icon  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
SEP = '<span class="sep">::</span>'


def ulink(u):
    return f'<a href="user.html">{e(u)}</a>'


def strip_re(title):
    return re.sub(r"^Re(\[\d+\])?: ", "", title)


lead = MAIN[0]
rest = sorted(enumerate(MAIN[1:], start=1),
              key=lambda ir: (int(ir[1][3].split(".")[1]), int(ir[1][3].split(".")[0])), reverse=True)
k_today = sorted([p for p in POSTS if p[1] <= 1 and p[6]], key=lambda p: -p[6])[:10]
busy = sorted([p for p in POSTS if p[1] <= 1], key=lambda p: -p[8])[:8]
online = FRIENDS[:7]


def main_row(idx, t, u, sec, d, k, new, _excerpt):
    nn = f' <span class="new">{new} new</span>' if new else ""
    return (f'      <li><img class="thumb" src="img/n/main{idx}.gif" alt="" width="60" height="75">'
            f'<a class="t" href="forum.html">{e(t)}</a>'
            f'<span class="m">{ulink(u)} {SEP} {e(sec)} {SEP} {d}{nn}</span></li>')


friends = "\n".join(
    f'      <li><a href="user.html"><img class="av" src="{icon(u)}" alt="" width="50" height="50">'
    f'<span class="u">{e(u)}</span><span class="loc">{e(LOCATION[u])}</span></a></li>'
    for u in online)
rows = "\n".join(main_row(i, *r) for i, r in rest)
ktop = "\n".join(f'        <li><a href="forum.html">{e(p[5] or p[3])}</a><span class="k">{p[6]} K</span></li>' for p in k_today)
active = "\n".join(f'        <li><a href="forum.html">{e(strip_re(p[5] or p[3]))}</a><span class="g2">{p[8]}</span></li>' for p in busy)

body = f"""  <header class="front">
    <img class="banner" src="img/banner.gif" alt="kyberia.sk" width="1208" height="240">
    <h1 class="sr">kyberia.sk</h1>
  </header>

  <section class="online" aria-label="priatelia online">
    <h2 class="day"><a href="people.html">priatelia online</a></h2>
    <ul>
{friends}
    </ul>
  </section>

  <article class="leadstory">
    <img class="leadimg" src="img/n/main0.gif" alt="" width="120" height="150">
    <div>
      <div class="m">{ulink(lead[1])} {SEP} {e(lead[2])} {SEP} {lead[3]} <span class="new">{lead[5]} new</span></div>
      <h2><a href="forum.html">{e(lead[0])}</a></h2>
      <p>{e(lead[6])}</p>
    </div>
  </article>

  <div class="frontcols">
    <section>
      <h2 class="day">na main</h2>
      <ol class="mainlist">
{rows}
      </ol>
      <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>
    </section>
    <aside>
      <h2 class="day"><a href="k.html">K dnes</a></h2>
      <ol class="ranked compact">
{ktop}
      </ol>
      <h2 class="day"><a href="last.html">kde sa píše</a></h2>
      <ol class="compact">
{active}
      </ol>
    </aside>
  </div>"""

io.open("main.html", "w", encoding="utf-8").write(
    "<!-- title: main -->\n<!-- nav: main -->\n<!-- layout: free -->\n"
    f'<main class="wrap front-page" id="obsah">\n{body}\n</main>\n')
print("wrote main.html")
