"""Write blogs.html: the newest diary (denník) entries from everyone. A system node, like v2's /id/21.
Excerpts ~250 chars at full width (as on real kyberia); no K numbers (same rule as main)."""
import html
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import icon  # noqa: E402
from _blogdata import OVERVIEW  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
SEP = '<span class="sep">::</span>'

items = "\n".join(f"""    <article class="entry">
      <img class="av" src="{icon(u)}" alt="" width="50" height="50">
      <div>
        <h2><a href="submission.html">{e(t)}</a></h2>
        <div class="m"><a href="blog.html">denník: {e(u)}</a> {SEP} <a class="when" href="submission.html">{when}</a> {SEP} videné {v}× {SEP} <a href="submission.html">{r} reakcií</a></div>
        <p>{e(x)}</p>
      </div>
    </article>""" for u, t, when, v, r, x in OVERVIEW)

body = f"""  <div class="head"><h1>blogs</h1></div>
  <div class="entries list">
{items}
  </div>
  <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie zápisy</a></nav>"""
io.open("blogs.html", "w", encoding="utf-8").write(
    "<!-- title: blogs -->\n<!-- nav: blogs -->\n"
    "<!-- node: id=21; name=blogs; template=system; parent=1|main|main.html; owner=fiktivny_admin; viewers=slobo -->\n"
    f'<main class="wrap" id="obsah">\n{body}\n</main>\n')
print("wrote blogs.html")
