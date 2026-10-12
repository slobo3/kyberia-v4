"""Assemble kyberia v4 showcase pages: shared header, node column, content, footer.

Every page is a node, so every page has the same skeleton:

    [ top bar ]
    [ node column | coords + title + content ]
    [ footer ]

Source files (_src/*.html, files starting with "_" are skipped) start with comments:
    <!-- title: kyberia -->
    <!-- nav: kyberia -->
    <!-- node: id=101; name=kyberia; template=nodeshell; parent=1|main|main.html; owner=fiktivny_admin; viewers=anima,bgdny -->
then optionally
    <!-- side --> ...extra <section>s for the node column... <!-- /side -->
and then the page content. Pages with `nav: none` get no shell at all.

Older-format sources (<div class="cols"> … <aside class="side">) are converted on the fly.
Run:  python _src/build.py
"""
import html
import pathlib
import re

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent
e = html.escape

NAV = [
    [("main", "main.html"), ("kyberia", "kyberia.html"), ("sub", "sub.html"), ("fr", "fr.html"),
     ("RE", "re.html"), ("bookmarks", "bookmarks.html")],
    [("mail", "mail.html"), ("last", "last.html"), ("people", "people.html")],
    [("K", "k.html")],
]
BADGES = {"mail": '<span class="new">2</span>', "RE": '<span class="new">3</span>'}
# sidebar sections that are cruft now (their data lives in the node column or nowhere)
CRUFT = ("permissions", "node", "visitors")


def header(active):
    groups = []
    for grp in NAV:
        links = []
        for label, href in grp:
            cur = ' aria-current="page"' if label == active else ""
            links.append(f'<a href="{href}"{cur}>{label}{BADGES.get(label, "")}</a>')
        groups.append('<span class="grp">' + "".join(links) + "</span>")
    return f"""<a class="skip" href="#obsah">preskočiť na obsah</a>
<header class="top"><div class="top-in">
  <a class="brand" href="main.html">kyberia<b>.</b>sk</a>
  <nav class="nav" aria-label="hlavná navigácia">
    {"".join(groups)}
  </nav>
  <form class="search-top" action="search.html" role="search"><input class="jump" name="q" type="search" placeholder="search" aria-label="search"></form>
  <div class="me"><a href="k.html" class="g" title="K wallet">5 849 K</a><a href="user.html">slobo</a><span class="av s" style="--h:95" aria-hidden="true">s</span></div>
</div></header>
"""


FOOTER = """<footer class="foot">
  <span>© kyberia.sk v4 <span class="sep">::</span> solon's revenge revisited</span>
  <span>provider(s) of this <b>digital community</b> guarant Thee nothing</span>
  <span>page generation took 0.0041 sec</span>
</footer>
"""


def parse_node(text):
    m = re.search(r"<!-- node: (.*?) -->", text)
    node = {}
    for part in m.group(1).split(";"):
        k, v = part.strip().split("=", 1)
        node[k] = v
    return node


def user_link(name):
    return f'<a href="user.html">{e(name)}</a>'


def node_column(node, extra):
    pid, pname, phref = (node.get("parent") or "||").split("|")
    parent = f'<a href="{phref}">{e(pname)}</a>' if pname else "—"
    viewers = ", ".join(user_link(v) for v in node.get("viewers", "").split(",") if v)
    return f"""<aside class="side nodecol" aria-label="nóda">
      <section class="nodeinfo">
        <dl class="kv">
          <dt>node</dt><dd>{e(node["name"])}</dd>
          <dt>template</dt><dd>{e(node["template"])}</dd>
          <dt>parent</dt><dd>{parent}</dd>
          <dt>owner</dt><dd>{user_link(node["owner"])}</dd>
          <dt>viewers</dt><dd class="viewers">{viewers}</dd>
        </dl>
        <p class="nodelinks"><a href="#">stats</a><a href="#">source</a><a href="#">commanders</a><a href="#">dendrites</a><a href="#">axones</a></p>
      </section>
{extra}
    </aside>"""


def coords(node):
    pid, pname, phref = (node.get("parent") or "||").split("|")
    items = []
    if pid:
        items.append(f'<li><span class="id">{pid}</span><a href="{phref}">{e(pname)}</a></li>')
    items.append(f'<li><span class="id">{node["id"]}</span><span class="n">{e(node["name"])}</span></li>')
    return f'<ol class="coords" aria-label="cwbe coordinatez">{"".join(items)}</ol>\n'


def strip_cruft_sections(side):
    def keep(m):
        h = re.search(r"<h2>(.*?)</h2>", m.group(0))
        return "" if h and h.group(1) in CRUFT else m.group(0)
    return re.sub(r"\s*<section>.*?</section>", keep, side, flags=re.S)


def split_old_format(body):
    """<main><div class="cols…"><div>CONTENT</div><aside>SIDE</aside></div></main>  ->  (content, side)"""
    m = re.search(r'<div class="cols[^"]*">\s*<div>(.*)</div>\s*<aside class="side"[^>]*>(.*?)</aside>\s*</div>\s*</main>',
                  body, flags=re.S)
    if m:
        return m.group(1), m.group(2)
    m = re.search(r"<main[^>]*>(.*)</main>", body, flags=re.S)
    return m.group(1), ""


def build(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"<!-- title: (.*?) -->", text).group(1)
    nav = re.search(r"<!-- nav: (.*?) -->", text).group(1)
    body = re.sub(r"<!-- (title|nav|node): .*? -->\n?", "", text)

    if nav == "none":
        page = body
    else:
        node = parse_node(text)
        side_m = re.search(r"<!-- side -->(.*?)<!-- /side -->\n?", body, flags=re.S)
        if side_m:
            side, content = side_m.group(1), body.replace(side_m.group(0), "")
        else:
            content, side = split_old_format(body)
        side = strip_cruft_sections(side)
        content = re.sub(r"\s*<div class=\"meta sub\">.*?</div>", "", content, flags=re.S)  # node data lives in the column now
        if 'class="coords"' not in content:
            content = re.sub(r'(<div class="head[^"]*">\s*)', lambda m: m.group(1) + coords(node), content, count=1)
        wide = " wide" if 'class="mail' in content else ""
        page = f"""{header(nav)}<main class="wrap" id="obsah">
  <div class="shell{wide}">
    {node_column(node, side.rstrip())}
    <div class="content">
{content.strip()}
    </div>
  </div>
</main>
{FOOTER}"""

    html_doc = f"""<!doctype html>
<html lang="sk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} :: kyberia.sk</title>
<link rel="stylesheet" href="k.css">
</head>
<body>
{page}
</body>
</html>
"""
    (OUT / path.name).write_text(html_doc, encoding="utf-8")
    print("built", path.name)


if __name__ == "__main__":
    for p in sorted(q for q in SRC.glob("*.html") if not q.name.startswith("_")):
        build(p)
