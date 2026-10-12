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
│ viewers   a, b, c   │ │ 120 K [K+] [book] [fook]          ← node pages only     │
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
  `stats :: source :: commanders :: dendrites :: axones` (white links). Page-specific sections go underneath. Permissions, visitor
  counts, tiamat, K-filters, neurons and polls are not shown.
- The node column is sticky on desktop and moves below the content under 1000px.
- The coordinate trail is the signature element: ids in mono above the names. The current node is bold.

---

## 4. Components

| component | notes |
|---|---|
| top bar | Bracketed groups in green, white links; the active link is a green block with black text. Red badge for new mail and RE. Search field, wallet, user. |
| child listing (`.rows`) | Grouped under `nodeshell::`, `forum::`, `submission::`, `link::`. Columns: name (white) · children (gray) · `N new`/`descdnt` (red) · K (red) · owner (green). |
| bookmarks (`.bm`) | Category heading (green) + total `N new`. Rows: name · `N new` · `descdnt` · `changed` · owner. |
| post | 40px avatar · white name · gray time · `level N` · `UP` · red `NEW`/K · title (green; `Re[n]:` in gray) · green body · quiet actions (`odpovedať`, `K+`, `put`). |
| thread | Nested lists with a dark-green guide line. Full indent for 4 levels, then compact, so a 20-deep flamewar still fits. |
| user page | Avatar, coordinate trail, name, `K` + actions (`mail`, `book`, `K+`, `ignore`, `ignore_mail`), tabs, userinfo frame, then **friends**: flat, chronological, newest first. Posting there makes you a friend. |
| feed item | Used by last, RE, fr, sub, K and search: where (green, parent white bold) · title · who/when · text · score column. |
| composer | Panel with title field, `bez HTML`, a formatting row, textarea, `náhľad` and `pridať`. |
| mail | Conversations list plus a stream; each message shows where the sender was. |
| segmented control | For view and sort switches (threads/chronological, 24 h/3 days…). |

---

## 5. Voice

Lowercase, kyberia jargon kept as is: `::`, `nodeshell::`, `descdnt`, `changed`, `K+`, `book`,
`fook`, `put`, `UP`, `SIROTKA`, `level`, `viewers`, `commanders`. Slovak UI copy. Button labels say
what they do (`pridať`, `poslať`, `náhľad`). Footer:
`provider(s) of this digital community guarant Thee nothing`.

---

## 6. Review checklist

1. Is any text a green other than `#6DAE42`? Is gray used outside meta?
2. Are any titles white, or any node links green or gray?
3. Is there a subtitle, an explainer or a counter line under a title?
4. Does the page use the shared skeleton (node column, trail, title)?
5. Is K written as `N K`, in red, with no icon?
6. Is it readable on a 390px phone: no horizontal scroll, node column below the content?
