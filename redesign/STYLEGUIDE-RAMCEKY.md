# kyberia v4 rámčeky: styleguide

The rámčeky version is the same v4 showcase dressed the way kyberia dresses node content: every node
sits in a frame (*rámček*). Members asked for it ("Kybéria je rámčeková, čo noda to rámček").
Pages: [`ramceky/`](ramceky/index.html). Every page has a `čisté | rámčeky` switch in the top strip.

This guide covers only what the rámčeky version changes. Everything else follows
[`STYLEGUIDE.md`](STYLEGUIDE.md).

## 1. What stays from v4

- The node model, the vocabulary and the page skeleton: node column, content, footer.
- The colours: green `#6DAE42` for text, white for names and links, red for K and NEW.
- One post component everywhere, with the same header: name, ☐, date and time, K, NEW, SIROTKA, and `↵ K+ edit` at the right.
- The phone layout.

## 2. What changes

| | clean v4 | rámčeky |
|---|---|---|
| node content | open text, a hairline under the post header | a green frame with a gray band |
| post title | only a title someone wrote | always, centred in the band, also the automatic `Re[n]: …` |
| thread lines | solid elbows from the parent's icon into the reply | dotted, one per level, kyberia style |
| type | Atkinson Hyperlegible, 15 px (16 px on phones), line-height 1.55 | Tahoma 8 pt on desktop, 13 px on phones |

## 3. Type

Kyberia's own sizes, measured on kyberia.sk, on desktop (`min-width: 721px`):

| token | value | kyberia |
|---|---|---|
| `--sans` | `Tahoma, "Lucida Grande CE", lucida, sans-serif` | the same stack |
| `--fs`, `--fs-s`, `--fs-l` | `10.67px` (8 pt) | body text, headers, titles |
| `--fs-xs` | `9px` | small text (signatures) is 8.9 px |
| `--fs-xl` | `13px` | |
| `--fs-xxl` | `16px` | page title |
| body `line-height` | `normal` | `normal` |

On phones the version stays kyberia-small but readable without zooming: body `13px`, meta `12px`, small `11px`,
`--fs-l` `14px`, `--fs-xl` `16px`, page title `20px`, line-height `1.4`. Kyberia itself has no phone layout (it shows the
desktop page zoomed out); 8 pt at 390 px would be smaller than any phone UI.

## 4. The frame

Measured on kyberia.sk:
- **Frame** (`div.node_content`): 1 px solid green, black background, `margin: .1em 0 1.3em`.
- **Band** (`div.node_header`): `#333`, `margin: 2px`, `padding: .2em`. The title line is centred.
- **Text** (`div.node_body`): `margin: 2px`.

In v4 the same markup gets the frame from [`css/ramceky.css`](css/ramceky.css):

```
icon  ┌─ 1px green ───────────────────────────────────────┐
      │▓ name ☐ 12.10.2026 23:04 :: 4 K          ↵  K+   ▓│  band #333, line 1: meta
      │▓              Re[2]: Kyberia session 2026          ▓│  band #333, line 2: title, centred
      │ v parent :: grandparent                             │  only on last, fr, RE, filter, search
      │ text                                                │  green
      └─────────────────────────────────────────────────────┘
```

Colour roles inside the band:
- the name is white, regular weight
- the date and time are green
- K, NEW and SIROTKA are red
- the title is white
- `↵ K+ edit` are gray, white on hover

## 5. Where frames go

Node content only:
- **Posts everywhere:** discussion, filter, last, fr, RE, search, the replies under a submission, blog or file, and friend posts.
- **Blog entries** in `blogs`: the band holds the author and date, then the title centred; the photo and text sit below.
- **A node's own text** (the kyberia rules, a blog's text and photos, a submission) and the **file block** of a data node. These get the frame without a band, because the node's title is the page heading.

Not framed: lists (kyberia's children, bookmarks, stats, people), mail, settings, the node column, the add form.

## 6. Titles

Every post shows its title line. A title someone wrote is shown as written. Without one, the
automatic kyberia title is used:
- **In a thread:** `Re: <node>` at the first level, `Re[n]: <node>` at level n.
- **In flat lists:** `Re: <parent>`. A reply to `Re[2]: X` is `Re[3]: X`.

The titles are in the markup of both versions (`<div class="pt auto">`). The clean version hides
them; the rámčeky skin shows them.

## 7. Threads

- Each post's list item has a dotted line on its left: `1px dotted #323232`.
- Each top-level thread ends with `1px dotted #656565`.
- Posts start `1.6em` apart, as on kyberia.
- The indent and the deep-thread rules are v4's: compact after level 4, and on phones no more indent after level 8.

## 8. Deliberately not brought back

`level: N`, `UP`, and the vector line above each post (`000001010006353500…`). v4 decided these are
noise, and the rámčeky version keeps that decision.

## 9. CSS

- [`css/ramceky.css`](css/ramceky.css) is a **skin**: it is loaded after the template CSS and before `showcase.css`, only in the rámčeky build.
- It is the one CSS layer allowed to override base and template rules. Template files still only add.
- `_src/build.py` builds every page twice: the clean version to `redesign/`, and the rámčeky version to `redesign/ramceky/`, with asset paths pointing one folder up.

## 10. Review checklist

1. Is every post, blog entry and node text in a green frame, and nothing else?
2. Does every post's band have two lines: meta, then the centred title (automatic `Re[n]:` included)?
3. Is the date green and the name white, regular weight?
4. Are the thread lines dotted, with no solid elbows left?
5. Is desktop text 8 pt Tahoma, and phone text 13 px?
6. Is the clean version unchanged, apart from the `čisté | rámčeky` switch?
7. Is every page of both versions readable at 390 px, with no horizontal scroll?
