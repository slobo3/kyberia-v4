"""RE: replies to my nodes, the shared post component with the node they answer as context."""
import html

from _post import post

e = html.escape


def re_post(icon, user, when, node, text, k, new):
    return post(user, when, e(text), k=k, new=new, where=[(node, "submission.html")])
