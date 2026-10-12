# kyberia clone: design manual

**Goal:** a kyberia user should not notice that the engine changed. Keep the classic
v2 look ("solon's revenge"): black page, poison-green text, white links, tiny Tahoma, dense
tables, brackets and double-colons. **Do not use the 2026 "k26" homepage portal theme**
(neon cards, Share Tech Mono, scanlines). It was explicitly rejected.

Files:
- `kyberia.css` is the reference stylesheet (tokens + all components below).
- `specimen.html` renders every component and is the visual source of truth for review.
- `reference/*.jpg|png` are screenshots of the live site taken 2026-10-12 (kept locally, not published: members-only content).

Allowed modernisation: semantic HTML instead of nested `<table>`s, CSS grid, responsive
collapse on phones, accessible focus states. **Not allowed:** new colours, rounded corners,
shadows, gradients, larger type, icons beyond the emoji the site already uses, animations.

---

## 1. Tokens

### Colour
| token | value | use |
|---|---|---|
| `--bg` | `#000000` | page background, post bodies |
| `--green` | `#6DAE42` | **default text colour**, borders, labels, meta |
| `--link` | `#FFFFFF` | all links and "names" (users, nodes), button text |
| `--bar` | `#333333` | post header bar background |
| `--field` | `#060606` | inputs, textareas, selects, buttons |
| `--red` | `#FF0000` | `NEW`, `N NEW Child`, K counts, `most_important`, `SIROTKA` |
| `--yellow` | `#FFFF00` (rare) | user-styled emphasis inside content only |

There is no hover colour on links (they stay white). Underline is not used by default.
Visited links are not differentiated.

### Type
| token | value |
|---|---|
| `--font` | `Tahoma, "Lucida Grande CE", lucida, Verdana, "DejaVu Sans", sans-serif` |
| `--fs` | `8pt` (≈10.67px), used for **everything**: nav, posts, listings, sidebars |
| `--fs-tiny` | `6.4pt` (≈8.5px), the vector/id-path line above posts |
| `--fs-textarea` | `10pt monospace`, textareas only |
| headings in content | user HTML (`<h1>` renders large green bold; leave browser defaults inside `#topic`) |

Bold is used for: node names in listings, category names, `NEW` markers, K counts,
`.important`. Line-height is the browser default (dense).

### Spacing & borders
- Borders are always `1px solid var(--green)`. Some separators are `1px dotted #444`.
- No border-radius anywhere. No shadows.
- Padding is tiny: 1–3px in cells, 2px in post header/body.
- Space between posts is roughly 14px.

---

## 2. Page skeleton

```
┌──────────────────────────── fixed top bar (20px, centered, z 666) ───────────────────────────┐
│ [ main - kyberia - sub /fr /RE - bookmarks /2]:[ mail - chat - last - people - blogz - …    │
│   …]:[ k / kNEW / … - forumz]:[ userinfo [setup] - /conf /2 - search [Quick...]  - help [logout] │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
┌ left 19% ───────┐┌ center (content, max ≈ 666px) ─────────────────┐┌ right ────────────────┐
│ node image      ││ #topic (bordered box: node content)            ││ [Search some node…]   │
│ node:  name     ││                                                ││                       │
│ template: 2     ││ add form                                       ││ dendrite <node>       │
│ parent: x       ││ toolbar                                        ││ dendrite <node>       │
│ owner: x        ││                                                ││ axone <node>          │
│ viewed by: [av] ││ child listing  OR  threaded discussion         ││                       │
│ created/updated ││                                                ││                       │
│ ┌cwbe coords┐   ││                                                ││                       │
│ ┌permissions┐   ││                                                ││                       │
│ K+ book fook  ││                                                ││                       │
│ show[2|3] flat  ││                                                ││                       │
│ ┌visitors───┐   ││                                                ││                       │
└─────────────────┘└────────────────────────────────────────────────┘└───────────────────────┘
                    © kyberia.sk v2.3 - solon's revenge
                    provider(s) of this digital community guarant Thee nothing
                    page generation took 0.00788 sec
```

- Full-width, no max-width container. The center column is left-aligned after the 19% sidebar.
- System pages (bookmarks, mail, last, re:, people, k) use a **narrower left sidebar** (or none)
  and a **wide content** area. See screenshots.
- A short green underline (≈62px) sits at the very top-left under the fixed bar (legacy artefact).
  Optional.
- Mobile (<760px, new): stack left sidebar *below* content, wrap the top bar onto 2–3 lines,
  and keep everything else unchanged.

---

## 3. Components

### 3.1 Top bar (`.t1`)
- `position: fixed; top: 0; height: 20px; width: 100%; background: #000; text-align: center;`
- One line of plain text links grouped with brackets and separators, exactly:
  `[ main - kyberia - sub /fr /RE - bookmarks /2]:[ mail - chat - last - people - blogz - pappa - KOL / ]:[ k / kNEW / kNSFW / noImg - CONS - forumz]:[ userinfo [setup] - /conf /2 - search` + quick-search input (placeholder `Quick...`) + ` - help` + `logout` button.
- Brackets and separators are green; links are white.
- MVP nav (drop links to out-of-scope features):
  `[ main - kyberia - bookmarks ]:[ mail - last - re: - people ]:[ k / kNEW - forumz ]:[ userinfo [setup] - search [Quick...] ]  [logout]`
- New mail: append ` 📬 N` in red after `mail`.

### 3.2 Buttons, inputs
- All controls: `background: #060606; color: #fff; border: 1px solid #6DAE42; font: 8pt Tahoma; border-radius: 0;`
- Buttons padding `1px 6px`, inputs `1px 2px`, height ≈ 18px.
- Button labels are lowercase identifiers with underscores: `add`, `preview`, `set_parent`,
  `configure_node_name`, `delete_hardlink`, `go_to`, `filter_by`. **Keep this voice.** Exceptions:
  `K+`, `book`, `fook`.
- Textarea: same border/background, `font: 10pt monospace`, full content width (≈666px), ~10 rows,
  resizable.
- Checkboxes: native, small. They exist on every listing line and post header (for bulk ops).
- Focus (new, a11y): `outline: 1px solid #fff; outline-offset: 1px`.

### 3.3 Bordered box (`.bordered`)
`border: 1px solid #6DAE42;` with no fill. Used for `#topic`, cwbe coordinates,
permissions, the visitor list and the config password group.

### 3.4 Left sidebar meta (`#sidebar_info`)
Two-column table, labels green, values white links:
```
      [node image, max 123px wide]
node:      23 dôvodov prečo…
template:  4
parent:    kyberia
owner:     zakladateľ
viewed by: [23px avatars inline]
created:   25.09.2007 - 18:42:42
updated:   25.09.2007 - 18:43:51
```
Then centered stacked boxes:
- **cwbe coordinatez:** (bold label) then one ancestor id per line (white links), blank line,
  `ABSOLUT` / `KYBERIA` (green; the K links to the node's K view).
- **permissions** (bold label): `you: r, w,` / `system: public` / `net: yes`.
- `total descendants::N` / `total children::N` (green) / `205 K` (red bold).
- Buttons row: `[K+] [book] [fook]`.
- `show[ 2 | 3 ] flat` view switcher.
- Visitors table (bordered): login (white) + number (green, right-aligned).

### 3.5 Child listing line (nodeshell view)
```
☐ nodeshell:: Compz & Net :: (236 children ) NEW DESCENDANT 11 K (mráz)
```
| part | style |
|---|---|
| `nodeshell::` | green, normal |
| node name | **white bold link** |
| `:: (236 children )` | green |
| `NEW DESCENDANT` | **red bold** (only if something new below) |
| `11 K` | **red bold** number + ` K` (omit when 0) |
| `(mráz)` | owner, white, in parens |

Sorted by type (nodeshell, forum, submission, node, link), then alphabetically **[observed]**.

### 3.6 Post (submission in a thread)
```
- 000001010339180708479011                      ← .vector: tiny white id-path, prefixed "- "
┌────┐┌──────────────────────────────────────────────────┐
│ av ││ jazmín ☐ 29.03.2018 - 18:41:15 level: 1 UP NEW   │ ← .node_header: bg #333, padding 2px
│50px││            NY Times dnes vymyslel kybcu           │ ← .node_header_title: centered
└────┘│ body text in green, links white …                │ ← .node_body: bg #000
      └──────────────────────────────────────────────────┘ ← .node_content: 1px green border
```
- Login: white. Date + `level: N`: green. `UP`: white link to parent. `NEW` / `SIROTKA`: red bold.
- Edited: `14.12.2010 - 12:16:50 (modif: 17.01.2011 - 21:40:50)`.
- Avatar: 50px wide, top-aligned, left of the box, no border.
- Depth indent: `padding-left` grows ~20–40px per level (`.level1`, `.level2`…). Keep a 1px dotted
  vertical guide at the left of each nested reply.
- Gap between posts ≈ 14px. The vector line sits just above the box.

### 3.7 Feed item (last / re: / k / mail)
Full-width variant of the post:
```
[av] ┌ Re[2]: update sablon main… in Re: update sablon main…                  (bar #333, white) ┐
     │ author: mrak [lokacia :: KyMoNo News, Bugs & Features] 20:05:24 - 12.10.2026 NEW     │
     └ body…                                                                                     ┘
```
- `in <parent>` link white; `author:` and `[lokacia :: …]` green; time green; `NEW` red.
- K page: the left gutter shows the K count in red (`12 K`) plus a small `K` button under the avatar.
- Mail: header is `from --> to [location: bookmarks] ☐`, then the date on its own line.

### 3.8 Bookmarks page
```
kategoria::#2 Politika :: 741 NEW
☐ Regionálna politická scéna :: 4 NEW Child :: descdnt :: [mirex]
☐ Slovenská politická scéna … :: 658 NEW Child :: descdnt :: changed :: [vlnka]
```
- `kategoria::` green; `#2 Politika` white bold; `741 NEW` red bold.
- Line: name white (bold when something is new); `N NEW Child` red bold; `descdnt` and `changed`
  green bold; owner `[login]` white in brackets.
- Left sidebar: `customize bookmarks`, K wallet (green), a **Friends** header bar (bg #333, green
  bold), and per friend: 23px avatar, `[where]` (white), `140m44s | login` (green).

### 3.9 People
- Centered small headings `most populated nodes`, `friends`, `users` (green).
- 5-column grid of entries: login (green, centered above), avatar (~32px), `[where]` white,
  idle time green.

### 3.10 Configure page
A centered single column of `input + [configure_xxx]` pairs, one per row: field on the left,
the button that commits *only that field* on the right. Preserve this one-field-one-button pattern.
Then the password group in a bordered box, then mail settings, mood, and the big content textarea
(≈490px wide, ~300px tall, bordered).

### 3.11 Footer
Centered, green, three lines:
```
© kyberia.sk v2.3 - solon's revenge          ("digital community" in white bold on some pages)
provider(s) of this digital community guarant Thee nothing
page generation took 0.00788 sec
```
Use the clone's own version string, e.g. `v4 - <codename>`.

### 3.12 Avatars & node images
- Square-ish GIF/JPG/PNG, displayed at 50px (posts), 23px (viewed-by, friends), and up to 123px
  (sidebar node image). No border radius, no frame.
- No avatar: show nothing (keep the space for 50px) **[decide: a green initial letter?]**.

---

## 4. Voice & micro-copy
- Mixed Slovak/English hacker jargon, lowercase, double-colons: `title or keywords::`,
  `total children::57`, `kategoria::`, `cwbe coordinatez`, `NEW DESCENDANT`, `descdnt`.
- Operation names are code-like identifiers (`set_synapse_weight`, `configure_mail_notify`).
- Dates are always `dd.mm.yyyy - hh:mm:ss`, local time (Europe/Bratislava).
- Do not "fix" or translate these. They are the identity of the site.

---

## 5. Review checklist (for every screen)
1. Background pure black, default text #6DAE42, every link white?
2. Font is Tahoma 8pt everywhere except the textarea (10pt mono)?
3. Borders 1px #6DAE42, square corners, no shadows/gradients?
4. NEW markers and K counts red bold, written as `N K` (never a heart or other icon)?
5. Post = 50px avatar + #333 header bar + centered title + body inside a green border?
6. Fixed one-line bracketed top bar?
7. Button labels are lowercase identifiers?
8. Density: compare side-by-side with `reference/` at 100% zoom; nothing should be roomier.
