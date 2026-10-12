"""Write forum-filter.html: the discussion filtered by user (kvasar). Results are all sub-nodes of the
node at any depth, flat, newest first, each with its place in the thread. Run from anywhere."""
import ast
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _post import post  # noqa: E402

os.chdir(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
SEP = '<span class="sep">::</span>'
WHO = "kvasar"

# reuse the flamewar data from _gen_user.py without running it
src = io.open("_gen_user.py", encoding="utf-8").read()
FLAME = ast.literal_eval(re.search(r"FLAME = (\[.*?\n\])", src, re.S).group(1))

hits = []
for i, (user, time, k, new, text) in enumerate(FLAME):
    if user != WHO:
        continue
    level = i + 1
    day = "13.10.2026" if time[:2] in ("00", "01") else "12.10.2026"
    parent = "Kyberia session 2026" if level == 1 else ("Re: Kyberia session 2026" if level == 2 else f"Re[{level - 2}]: Kyberia session 2026")
    hits.append((day, time, level, k, new, parent, re.sub(r"<[^>]+>", "", text)))
hits.sort(key=lambda h: (h[0][6:], h[0][3:5], h[0][:2], h[1]), reverse=True)

posts = [post(WHO, f"{day} {time}", e(text), k=k, new=new, mark=True, where=[(parent, "submission.html")])
         for day, time, level, k, new, parent, text in hits]

body = f"""  <div class="head">
    <h1>Kyberia session 2026: zostava, miesto, lístky</h1>
    <div class="actions"><span class="k ksum">51 K</span><button class="btn">K+</button><button class="btn on" aria-pressed="true" title="je v bookmarks">unbook</button><button class="btn">fook</button></div>
  </div>
  <form class="filterbar on" action="forum-filter.html" role="search" aria-label="filter v tejto nóde">
    <input class="field" name="filter" value="{WHO}" aria-label="filter">
    <select class="field by" name="by" aria-label="filtrovať podľa"><option value="text">text</option><option value="title">názov</option><option value="user" selected>user</option></select>
    <button class="btn" type="submit">filtrovať</button>
  </form>
  <p class="filterinfo"><span><b>{len(posts)}</b> od <b>{WHO}</b></span> <a class="btn" href="forum.html">zrušiť filter</a></p>
  <ol class="thread flat">
{chr(10).join(posts)}
  </ol>"""
io.open("forum-filter.html", "w", encoding="utf-8").write(
    "<!-- title: filter: kvasar :: Kyberia session 2026 -->\n<!-- nav: node -->\n"
    "<!-- node: id=9184022; name=Kyberia session 2026; template=forum; parent=63528|Hudba|kyberia.html; owner=polly; "
    "viewers=slobo,bgdny,kvasar,tichá_voda,sklo; img=img/session.svg; created=11.10.2026 21:40; updated=12.10.2026 21:03; perms=r, w :: public -->\n"
    f'<main class="wrap" id="obsah">\n{body}\n</main>\n')
print("wrote forum-filter.html with", len(posts), "results")
