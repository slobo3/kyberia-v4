"""Generates _src/user.html (ozvena' profile + a 20-deep flamewar). Run from redesign/."""
import html
import io
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import icon  # noqa: E402

e = html.escape
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # run from anywhere; paths are relative to redesign/

USERINFO = """<div style="background-color:#161616;padding:2em 6em 6em 6em;"><center>
<font color="#ffffff"><b>~</b></font><br><br>
<svg width="120" height="120" viewBox="0 0 120 120" aria-label="kresba: kruh a vlna"><circle cx="60" cy="60" r="48" fill="none" stroke="#5a5a5a" stroke-width="1"/><path d="M14 66 Q37 40 60 66 T106 66" fill="none" stroke="#9a9a9a" stroke-width="1.5"/><circle cx="60" cy="38" r="5" fill="#cfcfcf"/></svg><br><br>
<div style="color:#f2f2f2;font-size:0.9em;padding-left:45%;">ozvena<br><font color="#999999">// to, čo sa vráti, keď zakričíš do hôr</font></div><br><br><br>
<div style="color:#666;font-size:0.9em;">"kto počúva, ten počuje aj ticho"<br><font color="#777777">// napísané kriedou na múre pri rieke</font></div><br><br><br>
<div style="color:#e6e6e6;width:15em;font-size:0.9em;">
pošlem ti<br>hlas<br><br><font color="#999999">ako kameň<br>do studne</font><br><br>
čo padá<br>dlho-<font color="#999999">dlho<br><br>narazí<br><br>zazvoní</font><br><br>
a vráti sa<br><br><font color="#777777">// iný</font></div><br><br><br><br>
<div style="padding-left:16em;"><div style="color:#777;width:15em;font-size:0.9em;">nemám vlastné slová<br><font color="#555555">// mám tie tvoje, len neskôr</font></div></div><br><br><br>
<font color="#555555">{{ zbieram zvuky z miest, kde nikto nie je</font><br><br><br>
<div style="color:#e6e6e6;padding-left:45%;font-size:0.9em;">ticho<br><font color="#999999">je tiež odpoveď</font></div><br><br>
<font color="#ffffff"><b>~</b></font>
</center></div>"""

HUE = {"kvasar": 20, "ozvena": 15, "sklo": 230, "drienka": 80, "tichá_voda": 260}

# (user, time, K, is_new, text) — one entry per level, each replying to the previous
FLAME = [
    ("kvasar", "23:01", None, False, "Ten plagát na session je krásny. Len prečo šedý? Na kyberii sa píše zelenou."),
    ("ozvena", "23:04", "4 K", False, "lebo šedá je ticho. zelená je hluk."),
    ("kvasar", "23:06", None, False, "Zelená je identita. #6DAE42 je posvätná, to vie každý, kto sa tu kedy prihlásil."),
    ("sklo", "23:09", "2 K", False, "Posvätná je akurát tvoja nostalgia. Tahoma 8pt bola zločin proti očiam."),
    ("kvasar", "23:11", None, False, "Tahoma 8pt nás naučila čítať pozorne. Dnes nikto nedočíta ani odsek."),
    ("sklo", "23:14", None, False, "Áno, a kedysi sme aj prali na valche. Pokrok, kvasar."),
    ("kvasar", "23:16", "3 K", False, "Pokrok je, keď sa stránka vygeneruje za 0.0078 sec. Nie keď ťahá štyri megabajty fontov."),
    ("sklo", "23:19", None, False, "Ten font má 60 kB. Ale hlavne, že máš názor."),
    ("kvasar", "23:21", None, False, "Mám názor aj na tvoje K. Dve za celý rok. Gratulujem."),
    ("sklo", "23:24", "6 K", False, "Ad hominem na úrovni 10. Osobný rekord, ešte máš kam rásť."),
    ("drienka", "23:30", "11 K", False, "Chlapci, pozerám people. V tejto nóde je sedemnásť ľudí, len kvôli vám."),
    ("kvasar", "23:33", None, False, "drienka, toto je principiálna debata o identite komunity."),
    ("sklo", "23:35", None, False, "Je to debata o farbe písma."),
    ("kvasar", "23:41", None, True, "Farba písma JE identita komunity. Spýtaj sa hocikoho, kto tu bol pred tebou."),
    ("sklo", "23:58", None, True, "Pred tebou tu boli ľudia, čo to celé napísali v PHP4 a nikdy neplakali nad farbou."),
    ("kvasar", "00:12", None, True, "Lebo vedeli, čo robia. Na rozdiel od niekoho, kto by z kyberie najradšej spravil Discord."),
    ("sklo", "00:26", None, True, "Nikto nechce Discord. Chcem len prečítať, čo píšem, bez lupy."),
    ("kvasar", "00:41", None, True, "Kúp si okuliare. Alebo sa spýtaj ozveny, tá ti to zopakuje."),
    ("tichá_voda", "01:02", "23 K", True,
     'Chlapci, je jedna v noci. Choďte spať, ráno to bude vyzerať inak.'),
    ("ozvena", "01:47", "31 K", True, 'ticho<br>je tiež odpoveď<br><span class="whisper">// dobrú noc</span>'),
]


def post(level, user, time, k, new, text, topic="Kyberia session 2026"):
    day = "13.10.2026" if time[:2] in ("00", "01") else "12.10.2026"
    title = ""
    if level > 1:
        n = "" if level == 2 else f"[{level - 1}]"
        title = f'<div class="pt re">Re{n}: {topic}</div>'
    up = ""  # no UP links (decided)
    kk = f' <span class="sep">::</span> <span class="k">{k}</span>' if k else ""
    nn = ' <span class="sep">::</span> <span class="new">NEW</span>' if new else ""
    return f"""<article class="post">
  <img class="av" src="{icon(user)}" alt="" width="50" height="50">
  <div>
    <div class="ph"><a class="who" href="user.html">{e(user)}</a><input class="pick" type="checkbox" aria-label="vybrať"> <a class="when" href="submission.html">{day} {time}</a> <span class="sep">::</span> <span class="lvl">level {level}</span>{up}{kk}{nn}</div>
    {title}
    <div class="pb"><p>{text}</p></div>
    <div class="pa"><button class="btn ghost">odpovedať</button><button class="btn ghost">K+</button></div>
  </div>
</article>"""


inner = ""
for i in range(len(FLAME) - 1, -1, -1):
    child = f"\n<ol>\n<li>\n{inner}\n</li>\n</ol>" if inner else ""
    inner = post(i + 1, *FLAME[i]) + child

# flamewar lives in the forum discussion (threads exist there), between markers
fp = "_src/forum.html"
f = io.open(fp, encoding="utf-8").read()
block = f"<!-- flame:start -->\n<li>\n{inner}\n</li>\n<!-- flame:end -->"
if "<!-- flame:start -->" in f:
    f = re.sub(r"<!-- flame:start -->.*?<!-- flame:end -->", lambda m: block, f, flags=re.S)
else:
    f = f.replace('<ol class="thread">', '<ol class="thread deep">\n' + block, 1)
io.open(fp, "w", encoding="utf-8").write(f)

# user node discussion: ALWAYS flat + chronological, newest first. Every post is a friend node.
FRIENDS = [
    ("drienka", "12.10.2026 18:20", "5 K", True, "Tá kresba s vlnou v userinfe ma dostala. Je to tvoje?"),
    ("lúč", "02.09.2026 22:41", None, False, "~"),
    ("tichá_voda", "14.06.2026 09:12", "2 K", False, "Ďakujem za tie knihy. Vrátim ich osobne, nie poštou."),
    ("kvasar", "30.12.2025 23:59", None, False, "Šťastný nový rok, ozvena."),
    ("sklo", "03.05.2024 16:05", "1 K", False, "Pamätáš na tú session v Subclube? Tie kresby na servítkach mám dodnes."),
    ("lúč", "11.11.2019 11:11", "8 K", False, "keď kričím do hôr, odpovedáš ty"),
]
HUE.setdefault("lúč", 170)

def friend_post(user, when, k, new, text):
    kk = f' <span class="sep">::</span> <span class="k">{k}</span>' if k else ""
    nn = ' <span class="sep">::</span> <span class="new">NEW</span>' if new else ""
    return f"""<li><article class="post">
  <img class="av" src="{icon(user)}" alt="" width="50" height="50">
  <div>
    <div class="ph"><a class="who" href="user.html">{e(user)}</a><input class="pick" type="checkbox" aria-label="vybrať"> <a class="when" href="user.html">{when}</a>{kk}{nn}</div>
    <div class="pb"><p>{text}</p></div>
    <div class="pa"><button class="btn ghost">K+</button></div>
  </div>
</article></li>"""

thread = '<ol class="thread friends">\n' + "\n".join(friend_post(*x) for x in FRIENDS) + "\n</ol>"

PAGE = f"""<!-- title: ozvena -->
<!-- nav: node -->
<!-- node: id=4401337; name=ozvena; template=user; parent=||; owner=ozvena; viewers=slobo,kvasar,sklo,drienka; img=img/u/ozvena.gif; created=03.02.2003 18:12; updated=07.07.2025 20:24; perms=r, w :: public -->
<main class="wrap" id="obsah">
  <div class="cols">
    <div>
      <div class="head prof">
        <div>
          <ol class="coords" aria-label="cwbe coordinatez"><li><span class="id">4401337</span><span class="n">ozvena</span></li></ol>
          <h1>ozvena</h1>
          <div class="actions">
            <span class="k ksum">38 K</span>
            <a class="btn primary" href="mail.html">mail</a>
            <button class="btn">book</button>
            <button class="btn">K+</button>
            <button class="btn ghost">ignore</button>
            <button class="btn ghost">ignore_mail</button>
          </div>
        </div>
      </div>

      <nav class="tabs" aria-label="nódy používateľa">
        <a href="#" aria-current="page">userinfo</a><a href="#">submissions</a><a href="#">forums</a><a href="#">nodeshells</a><a href="#">articles</a><a href="blogs.html">blogs</a><a href="data.html">datas</a><a href="#">K</a><a href="#">friends</a><a href="#">movement</a><a href="#">bookmarks</a>
      </nav>

      <section class="userinfo" aria-label="userinfo">
{USERINFO}
      </section>

      <form class="composer" aria-label="napísať ozvena">
        <div class="title-row">
          <input class="field" placeholder="názov" aria-label="názov">
          <label class="check"><input type="checkbox"> bez HTML</label>
        </div>
        <textarea class="field" placeholder="napíš ozvena…" aria-label="text"></textarea>
        <div class="send"><span></span><span><button type="button" class="btn">náhľad</button> <button type="submit" class="btn primary">pridať</button></span></div>
      </form>

      <div class="thread-bar">
        <h2>friends</h2>
      </div>

{thread}
      <nav class="pager" aria-label="stránkovanie"><a class="btn" href="#">staršie</a></nav>
    </div>

    <aside class="side" aria-label="o používateľovi">
      <section>
        <h2>node</h2>
        <dl class="kv">
          <dt>owns</dt><dd>47 046 K</dd>
          <dt>K</dt><dd>38 K</dd>
          <dt>children</dt><dd>179</dd>
          <dt>updated</dt><dd>07.07.2025 20:24</dd>
        </dl>
      </section>
      <section>
        <h2>permissions</h2>
        <dl class="kv"><dt>you</dt><dd>read, write</dd><dt>system</dt><dd>public</dd><dt>net</dt><dd>no</dd></dl>
      </section>
      <section>
        <h2>friends</h2>
        <ul class="who-list">
          <li><img class="av s" src="{icon('lúč')}" alt=""><span class="u">lúč</span><span class="idle"></span></li>
        </ul>
      </section>
      <section>
        <h2>visitors</h2>
        <ul class="who-list">
          <li><img class="av s" src="{icon('slobo')}" alt=""><span class="u">slobo</span><span class="idle">teraz</span></li>
          <li><img class="av s" src="{icon('kvasar')}" alt=""><span class="u">kvasar</span><span class="idle">dnes</span></li>
          <li><img class="av s" src="{icon('sklo')}" alt=""><span class="u">sklo</span><span class="idle">dnes</span></li>
        </ul>
      </section>
    </aside>
  </div>
</main>
"""

io.open("_src/user.html", "w", encoding="utf-8").write(PAGE)
print("wrote _src/user.html")
