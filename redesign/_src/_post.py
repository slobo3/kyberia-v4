"""The one post component. Every list of posts (threaded and flat discussion, filter, last, fr, RE,
a post's or blog's replies, friend posts on a user node) is built from post(); nothing else writes posts.

Anatomy, always the same:
  icon | name ☐ date time :: K :: NEW            (header; SIROTKA for orphans)
       | v parent :: grandparent                 (only where the post isn't shown under its parent)
       | title                                   (only a title someone wrote; automatic Re[n]: … is hidden)
       | text
       | (odpovedať · K+ sit at the right end of the header as small text actions, not buttons)
Threaded = these nested in <ol>; flat = the same, not nested.
"""
import html
import re

from _content import icon

e = html.escape
SEP = '<span class="sep">::</span>'
ACTS = '<span class="pa"><button class="act" type="button">odpovedať</button><button class="act" type="button">K+</button></span>'
AUTO_TITLE = re.compile(r"^\s*Re(\[\d+\])?:", re.I)


def k_label(k):
    if not k:
        return ""
    k = str(k)
    return k if k.endswith("K") else f"{k} K"


def article(user, when, text, title=None, k=None, new=False, where=None, orphan=False, mark=False):
    """user: name; when: 'dd.mm.yyyy hh:mm'; text: HTML (escape it before); where: [(label, href), …]."""
    name = f"<mark>{e(user)}</mark>" if mark else e(user)
    meta = ""
    if k:
        meta += f' {SEP} <span class="k">{k_label(k)}</span>'
    if new:
        meta += f' {SEP} <span class="new">NEW</span>'
    if orphan:
        meta += f' {SEP} <span class="orphan">SIROTKA</span>'
    ctx = ""
    if where:
        ctx = '\n    <div class="pw">v ' + f" {SEP} ".join(f'<a href="{h}">{e(lbl)}</a>' for lbl, h in where) + "</div>"
    ttl = f'\n    <div class="pt">{e(title)}</div>' if title and not AUTO_TITLE.match(title) else ""
    return f"""<article class="post{' is-new' if new else ''}">
  <img class="av" src="{icon(user)}" alt="" width="50" height="50">
  <div>
    <div class="ph"><a class="who" href="user.html">{name}</a><input class="pick" type="checkbox" aria-label="vybrať"> <a class="when" href="submission.html">{e(when)}</a>{meta}{ACTS}</div>{ctx}{ttl}
    <div class="pb">{text if text.lstrip().startswith("<") else f"<p>{text}</p>"}</div>
  </div>
</article>"""


def post(*args, kids="", **kw):
    """A post as a list item; kids = already rendered child <li>s (threaded)."""
    sub = f"\n<ol>\n{kids}\n</ol>" if kids else ""
    return f"<li>{article(*args, **kw)}{sub}</li>"
