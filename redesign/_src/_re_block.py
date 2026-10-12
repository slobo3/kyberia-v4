"""RE rendered with the same post component as discussions (imported by _gen_feeds.py)."""
import html

e = html.escape
SEP = '<span class="sep">::</span>'


def re_post(icon, user, when, node, text, k, new):
    kk = f' {SEP} <span class="k">{k} K</span>' if k else ""
    nn = f' {SEP} <span class="new">NEW</span>' if new else ""
    return f"""<li><article class="post">
  <img class="av" src="{icon(user)}" alt="" width="50" height="50">
  <div>
    <div class="ph"><a class="who" href="user.html">{e(user)}</a><input class="pick" type="checkbox" aria-label="vybrať"> <a class="when" href="forum.html">{e(when)}</a>{kk}{nn}</div>
    <div class="pt re">Re: <a href="forum.html">{e(node)}</a></div>
    <div class="pb"><p>{e(text)}</p></div>
    <div class="pa"><button class="btn ghost">odpovedať</button><button class="btn ghost">K+</button></div>
  </div>
</article></li>"""
