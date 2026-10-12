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
import hashlib
CSS_VER = hashlib.sha1((OUT / "k.css").read_bytes()).hexdigest()[:8]  # cache-bust the stylesheet on every change

NAV = [
    [("main", "main.html"), ("kyberia", "kyberia.html"), ("fr", "fr.html"),
     ("RE", "re.html"), ("bookmarks", "bookmarks.html")],
    [("mail", "mail.html"), ("last", "last.html"), ("people", "people.html")],
    [("K", "k.html")],
]
BADGES = {"mail": '<span class="new">2</span>', "RE": '<span class="new">3</span>'}
# sidebar sections that are cruft now (their data lives in the node column or nowhere)
CRUFT = ("permissions", "node", "visitors")


LOUPE = ('<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" '
         'stroke="currentColor" stroke-width="2"/><line x1="12.5" y1="12.5" x2="18" y2="18" stroke="currentColor" stroke-width="2"/></svg>')


def header(active, title=""):
    groups, linksets = [], []
    for grp in NAV:
        links = []
        for label, href in grp:
            cur = ' aria-current="page"' if label == active else ""
            links.append(f'<a href="{href}"{cur}>{label}{BADGES.get(label, "")}</a>')
        groups.append('<span class="grp">' + "".join(links) + "</span>")
        linksets.append(links)
    # phone menu: K joins the mail/last/people group (a group of one wastes two dividers)
    mobile_sets = linksets[:1] + [sum(linksets[1:], [])]
    mgroups = ['<div class="grp">' + "".join(ls) + "</div>" for ls in mobile_sets]
    here = e(title or active)
    return f"""<a class="skip" href="#obsah">preskočiť na obsah</a>
<header class="top"><div class="top-in">
  <nav class="nav" aria-label="hlavná navigácia">
    {"".join(groups)}
  </nav>
  <form class="search-top" action="search.html" role="search"><label for="q-top" class="loupe" title="search">{LOUPE}</label><input id="q-top" class="jump" name="q" type="search" placeholder="search" aria-label="search"></form>
  <div class="me"><a href="user.html">slobo</a><a href="#" class="g">setup</a><a href="#" class="btn ghost logout">logout</a></div>
  <span class="here" aria-hidden="true">{here}</span>
  <span class="mquick"><a href="mail.html">mail<span class="new">2</span></a><a href="re.html">RE<span class="new">3</span></a></span>
  <details class="mmenu"><summary aria-label="menu"><svg viewBox="0 0 20 16" width="20" height="16" aria-hidden="true"><rect y="0" width="20" height="2"/><rect y="7" width="20" height="2"/><rect y="14" width="20" height="2"/></svg></summary>
    <nav class="mnav" aria-label="menu">
      {"".join(mgroups)}
      <div class="grp"><a href="user.html">userinfo <span class="who-me">[slobo]</span></a><a href="search.html">search</a></div>
      <div class="mme"><a href="#">setup</a><a href="#" class="btn ghost logout">logout</a></div>
    </nav>
  </details>
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
    if node.get("details") == "no" or node.get("template") == "system":  # system nodes: no node details, only page sections
        return f'<aside class="side nodecol" aria-label="nóda">\n{extra}\n    </aside>' if extra.strip() else ""
    pid, pname, phref = (node.get("parent") or "||").split("|")
    parent = f'<a href="{phref}">{e(pname)}</a>' if pname else "—"
    dates = "".join(f"<dt>{k}</dt><dd>{e(node[k])}</dd>" for k in ("created", "updated") if node.get(k))
    if node.get("perms"):
        dates += f'<dt>permissions</dt><dd>{e(node["perms"])}</dd>'
    if node.get("view"):  # discussion nodes: threaded / flat
        cur = node["view"]
        links = "".join(f'<a href="#"{" aria-current=\"true\"" if v == cur else ""}>{v}</a>' for v in ("threaded", "flat"))
        dates += f'<dt>view</dt><dd class="views">{links}</dd>'
    viewers = ", ".join(user_link(v) for v in node.get("viewers", "").split(",") if v)
    if node.get("template") == "system":
        image = ""  # system nodes don't need images
    elif node.get("img"):
        image = f'<img class="nodeimg" src="{node["img"]}" alt="">'
    else:
        hue = int(node["id"]) * 47 % 360
        image = f'<span class="nodeimg tile" style="--h:{hue}" aria-hidden="true">{e(node["name"][0])}</span>'
    # nodehead = the basics (image + node/template/parent/owner/viewers): top of the column on desktop,
    # top of the page on phones. Everything after it goes below the content on phones.
    return f"""<aside class="side nodecol" aria-label="nóda">
      <section class="nodeinfo nodehead{' noimg' if not image else ''}">
        {image}
        <dl class="kv">
          <dt>node</dt><dd>{e(node["name"])}</dd>
          <dt>template</dt><dd><a href="#" title="template je tiež nóda">{e(node["template"])}</a></dd>
          <dt>parent</dt><dd>{parent}</dd>
          <dt>owner</dt><dd>{user_link(node["owner"])}</dd>
          <dt>viewers</dt><dd class="viewers">{viewers}</dd>
          {dates}
        </dl>
      </section>
      <p class="nodelinks"><a href="#">stats</a><a href="#">source</a><a href="#">commanders</a><a href="synapses.html">dendrites &amp; axones</a></p>
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
    elif "<!-- layout: free -->" in text:  # main: its own layout, no node column
        body = body.replace("<!-- layout: free -->\n", "")
        body = re.sub(r'\s*<ol class="coords".*?</ol>', "", body, flags=re.S)
        page = f"{header(nav, title)}{body.strip()}\n{FOOTER}"
    else:
        node = parse_node(text)
        side_m = re.search(r"<!-- side -->(.*?)<!-- /side -->\n?", body, flags=re.S)
        if side_m:
            side, content = side_m.group(1), body.replace(side_m.group(0), "")
        else:
            content, side = split_old_format(body)
        side = strip_cruft_sections(side)
        content = re.sub(r"\s*<div class=\"meta sub\">.*?</div>", "", content, flags=re.S)  # node data lives in the column now
        content = re.sub(r'\s*<ol class="coords".*?</ol>', "", content, flags=re.S)  # no coordinate trail (decided)
        if node.get("template") == "system":  # the active top-bar item already names the page: title only for screen readers
            content = re.sub(r'<div class="head">\s*<h1>(.*?)</h1>\s*</div>', r'<h1 class="sr">\g<1></h1>', content, count=1, flags=re.S)
        column = node_column(node, side.rstrip())
        wide = " wide" if 'class="mail' in content else ""
        if not column:
            wide += " solo"  # no left column at all
        if node.get("template") == "system":
            wide += " sys"
        page = f"""{header(nav, title)}<main class="wrap" id="obsah">
  <div class="shell{wide}">
    {column}
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
<link rel="stylesheet" href="k.css?v={CSS_VER}">
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
