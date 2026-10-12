# kyberia v4

A redesign concept for [kyberia.sk](https://kyberia.sk): the same kyberia, made readable.

**Live showcase:** https://slobo3.github.io/kyberia-v4/

v4 keeps kyberia's holy green (`#6DAE42`), its vocabulary (`::`, `nodeshell::`, `descdnt`, `K+`,
`book`, `fook`, `put`) and its node model. It rebuilds the typography, spacing, page skeleton and
mobile layout. The pages are pure HTML and CSS, with no JavaScript. All people and posts in them are invented.

## What's here

| path | what |
|---|---|
| [`redesign/`](redesign/) | the v4 showcase pages: main, kyberia, discussion, sub, fr, RE, bookmarks, mail, last, people, user, search, K |
| [`redesign/STYLEGUIDE.md`](redesign/STYLEGUIDE.md) | v4 styleguide: colour rules, type, page skeleton, components |
| [`redesign/k.css`](redesign/k.css) | the stylesheet |
| [`SPEC.md`](SPEC.md) | product and technical spec for an MVP rewrite (node model, permissions, K, bookmarks, mail…) |
| [`design/`](design/) | notes on the classic v2 look as it is today, plus a classic specimen |

## Editing the showcase

Pages are written in `redesign/_src/` and assembled by a tiny build script. It adds the shared
top bar, the node column and the footer:

```sh
python redesign/_src/_gen_user.py   # regenerates the user page + the flamewar
python redesign/_src/build.py       # writes redesign/*.html
```
