"""K page items: mostly photos, videos and longer posts. 'name of node, in X, by Y', no children counts."""
import html

e = html.escape
SEP = '<span class="sep">::</span>'


def k_item(rank, user, where, section, title, kind, media, text, k, when):
    if kind == "photo":
        body = f'<img class="kimg" src="{media}" alt="{e(title)}" width="640" height="420">\n    <p class="txt">{e(text)}</p>'
    elif kind == "video":
        body = (f'<div class="video" role="img" aria-label="video: {e(title)}"><span class="play" aria-hidden="true"></span>'
                f'<span class="src">{e(media)}</span></div>\n    <p class="txt">{e(text)}</p>')
    else:
        body = f'<p class="txt long">{e(text)}</p>'
    return f"""<li>
  <span class="rank">{rank}</span>
  <div>
    <h3 class="art"><a href="submission.html">{e(title)}</a></h3>
    <div class="by">v <a class="parent" href="forum.html">{e(where)}</a> {SEP} od <a href="user.html">{e(user)}</a> {SEP} <a class="when" href="submission.html">{e(when)}</a></div>
    {body}
  </div>
  <div class="score"><span class="k">{k} K</span><button class="btn">K+</button><button class="btn ghost">fook</button></div>
</li>"""
