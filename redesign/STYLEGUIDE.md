# kyberia v4: styleguide

The same kyberia, made readable. v4 keeps kyberia's colours, vocabulary and node model, and
rebuilds type, spacing, layout and mobile. The reference implementation is [`k.css`](k.css); the
pages in this folder are the specimens.

(For the classic v2 look as it is today, see [`../design/DESIGN.md`](../design/DESIGN.md).)

---

## 1. Rules that don't bend

1. **The green is holy.** `#6DAE42` is the text colour, the label colour and the border colour.
   It never gets lighter, darker or replaced.
2. **K is just K.** Always written `205 K`. No hearts, stars or icons.
3. **No subtitles.** No explainer text under titles, and no summary counters ("9 friends :: 14 new").
   Assume people will figure it out.
4. **Every page is a node.** Every page uses the same skeleton (§3), including bookmarks, mail and K.
   The one exception is **main**: the front page has its own layout (logo, tagline, lead story, lists).
6. **The kyberia logo is holy.** Use the original node-101 GIF, unmodified. Never redraw or reinterpret it.
5. **User HTML is sacred.** A userinfo or post renders the author's own HTML as written, in a frame.

---

## 2. Tokens

### Colour

| token | value | use |
|---|---|---|
| `--void` | `#000` | page background (true black, not tinted) |
| `--green` | `#6DAE42` | body text, headings, titles, labels, control borders, main dividers |
| `--white` | `#fff` | **links to nodes** (listings, sidebars), people's names, nav |
| `--red` | `#ff3b30` | `NEW`, `N new`, K counts, silence, `SIROTKA` |
| `--mute` | `#8b8f87` | low-importance meta only: times, ids, counts, `::`, levels |
| `--rule` | `#1d2e13` | faint row separators |
| `--rule-3` | `#2f4a1f` | thread guide lines, coordinate separators |
| `--panel` | `#0a1206` | the one surface: composer, mail panes, own messages |

Grays and extra greens are allowed only in those exact roles. No text is ever a second green.

**Who gets which colour:**
- Headings and titles (h1, category names, post titles, article titles): **green**, set apart by size and weight.
- Links to nodes (child listings, bookmarks, sidebar lists): **white**. Bold when something is new, regular when not. Never gray.
- People: **white bold**.
- Owners in listings: **green**.

### Type

- **Atkinson Hyperlegible Next** for everything. It's a legibility-first humanist sans with full Slovak diacritics, and Tahoma's spiritual successor.
- **Atkinson Hyperlegible Mono** only for things that are really codes: node ids, vectors, coordinate ids.
- Scale (15px base): 12 · 13 · 15 · 18 · 26 · 30–44 (h1), up to 56 on main.
- Weights: 400 body, 500 nav/controls, 700 titles and names, 800 h1.
- Numbers use tabular figures.

### Shape

- Radius 2px on controls only. No shadows, no gradients (except the photo placeholder), no glow, no scanlines.
- Borders are 1px.

---

## 3. Page skeleton

```
┌ top bar ─────────────────────────────────────────────────────────────────────────┐
│ kyberia.sk  [ main kyberia sub fr RE bookmarks ] [ mail last people ] [ K ]       │
│                                                     [search]  5 849 K  slobo     │
└───────────────────────────────────────────────────────────────────────────────────┘
┌ node column (220px) ┐ ┌ content (≤ 940px) ──────────────────────────────────────┐
│ node      kyberia   │ │ 1    │ 101                     ← cwbe coordinatez trail  │
│ template  nodeshell │ │ main │ kyberia                                         │
│ parent    main      │ │                                                        │
│ owner     admin     │ │ kyberia                          ← h1, green, 800      │
│ viewers   a, b, c   │
│ created / updated   │
│ permissions         │
│ view  threaded::flat│ │ 120 K [K+] [book] [fook]          ← node pages only     │
│ stats::source::     │ │                                                        │
│ commanders::dendr.. │ │ …page content…                                         │
│ ─────────────────── │ │                                                        │
│ page sections       │ │                                                        │
│ (friends online,    │ │                                                        │
│  online, wallet…)   │ │                                                        │
└─────────────────────┘ └────────────────────────────────────────────────────────┘
  © kyberia.sk v4 :: solon's revenge revisited · provider(s)… guarant Thee nothing · page generation took …
```

- The node column shows only node, template, parent, owner, viewers (names, not avatars), and
  `stats :: source :: commanders :: dendrites & axones` (the last opens one page with both lists) (white links). Page-specific sections go underneath. Permissions, visitor
  counts, tiamat, K-filters, neurons and polls are not shown.
- The node column sits at the top of the page and scrolls away with it (not sticky). Under 1000px it splits: the **basics** (node image on the left, node/template/
  parent/owner/viewers on the right) go **above** the content; the links and page extras go below it.
- ****system nodes** (mail, bookmarks, RE, fr, last, people, K, search…) show no node details** (no node/template/parent/owner/viewers, no stats links).
  If they have page sections (bookmarks: friends online + wallet; fr: friends) those keep the left column;
  otherwise the content takes the full width (mail, RE, last, people, search).
- Every post has a checkbox (vybrať) in its header line right after the name, no label (for bulk K+, put, delete_hardlink).
- No coordinate trail above titles (dropped). The title starts the page.
- The node column starts with the **node image** (v2's node image; user avatar on user pages).

---

## 3b. One node, many templates

Every page shows a **node**. Forum, nodeshell and user aren't different kinds of thing, just
different **templates** (default renderers) for the same anatomy:

```
node details  →  own content  →  add form (if you may write)  →  children
```

| template | children render as | the add form creates |
|---|---|---|
| nodeshell | listing grouped by template (`forum::`, `nodeshell::`…) | a child node; template chosen in the form |
| forum / submission | discussion: threaded or flat | a reply |
| user | friend posts: flat, newest first | a friend post (and a friendship) |
| system (bookmarks, mail, K…) | the page's own view, no node details | per page |

Design consequences: the same components (node details, composer, post, listing row) appear
under every template. A template never invents its own chrome. `template` in the node details is a
link, because a template is a node too.

## 4. Components

| component | notes |
|---|---|
| top bar | Bracketed groups in green, white links; the active link is a green block with black text. Red badge for new mail and RE. Search field, wallet, user. |
| child listing (`.rows`) | Grouped under `nodeshell::`, `forum::`, `submission::`, `link::`. Columns: name (white) · children (gray) · `N new`/`descdnt` (red) · K (red) · owner (green). |
| bookmarks (`.bm`) | Category heading (green) + total `N new`. Rows: name · `N new` · `descdnt` · `changed` · owner. |
| post | 40px avatar · white name · gray time · `level N` · red `NEW`/K · title (green; `Re[n]:` in gray) · green body · quiet actions (`odpovedať`, `K+`); unlabeled select checkbox after the name; the time is a link to the post node (gray, white + underline on hover). |
| thread | Nested lists with a dark-green guide line. Full indent for 4 levels, then compact, so a 20-deep flamewar still fits. |
| user page | Avatar, coordinate trail, name, `K` + actions (`mail`, `book`, `K+`, `ignore`, `ignore_mail`), tabs, userinfo frame, then **friends**: flat, chronological, newest first. Posting there makes you a friend. |
| feed item | Used by last, RE, fr, sub, K and search: where (green, parent white bold) · title · who/when · text · score column. |
| composer | Panel with title field, `bez HTML`, a formatting row, textarea, `náhľad` and `pridať`. |
| mail | Conversations list plus a stream; each message shows where the sender was. |
| segmented control | For view and sort switches (threads/chronological, 24 h/3 days…). |

---

## 4b. Icons & images (kyberia's soul)

- **User icons** are the users' own GIFs (pixel art, often animated), shown at **native size**:
  50×50 in posts, feeds, people and main; 25×25 in small lists. Always `image-rendering: pixelated`,
  no rounding, no frames. The showcase icons are invented (`_src/_gen_images.py`).
- **Node images** illustrate content: the lead story and every entry on main, and the top of the
  node column. **System nodes (bookmarks, mail, last, people, K, fr, RE, search) have no image.**
- **main** opens with the animated **banner**, a rework of the historical kyberia banner
  (`_src/_gen_banner.py`): the original logo, a circuit-board frame, faint UI text, horizontal tears. No tagline, no flashing blocks.
- **Friends online** are shown on main as a row of their icons with names and locations.

## 5. Voice

Lowercase, kyberia jargon kept as is: `::`, `nodeshell::`, `descdnt`, `changed`, `K+`, `book`,
`fook`, `put`, `SIROTKA`, `level`, `viewers`, `commanders`. Slovak UI copy. Button labels say
what they do (`pridať`, `poslať`, `náhľad`). Footer:
`provider(s) of this digital community guarant Thee nothing`.

---

## 6. Review checklist

1. Is any text a green other than `#6DAE42`? Is gray used outside meta?
2. Are any titles white, or any node links green or gray?
3. Is there a subtitle, an explainer or a counter line under a title?
4. Does the page use the shared skeleton (node image + node column, title), unless it's main?
5. Is K written as `N K`, in red, with no icon?
6. Is it readable on a 390px phone: no horizontal scroll, node column below the content? Check **every** page in `mobile.html` after **every** change.
7. Are all `@media` rules still at the end of `k.css`? Add new base rules above the responsive section, never after it.
