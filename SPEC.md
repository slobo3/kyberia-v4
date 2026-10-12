# kyberia clone: product & technical spec (MVP)

Source: hands-on review of kyberia.sk on 2026-10-12 (logged in as `slobo`), plus the in-site
"kyberia manual / user guide" (`/id/625175`, `/id/628600`) and "23 dôvodov…" (`/id/3391807`).
Things marked **[inferred]** were deduced from the UI rather than documented; confirm before building.

Design and look & feel live in [`design/DESIGN.md`](design/DESIGN.md).

---

## 1. What kyberia is (the part worth preserving)

A Slovak/Czech members-only community running since 2001. It is not a forum *app*; it is
**one tree of nodes**. A category, a forum, a post, a reply, a user profile, a "friend"
comment and a bookmark category are all the same thing: a *node* with a template, a parent,
an owner, content, and permissions. Everything the site does is an *operation* (a green
button) performed on a node.

The things users actually care about, in rough order:

1. **Reading what's new.** Bookmarks with per-node "N NEW" counters, `last` (global
   firehose), `re:` (replies to me), and `K` (most-appreciated nodes recently).
2. **Threaded discussions** under any node, with NEW markers since my last visit.
3. **Mail** (private messages between users).
4. **People.** Who is online and *where on kyberia they are right now*, plus friends.
5. **K.** Giving K (appreciation) to nodes; a K leaderboard.
6. **Self-governance.** Node owners/masters run their own corner (access, silence).
7. **Ownership & structure.** Anyone can create forums/nodeshells where allowed, and
   `put` (hard-link) a node into several places without copying it.

Things that are cruft or out of scope (see §9): the 2026 "k26" homepage portal, KOL/Solana
wallet, 🦆/🐘 currencies, giver.eu, chat, user-programmable Smarty templates, K-neurons weights,
skins, polls, stats.

---

## 2. Core concept: the node

### 2.1 Node fields

| field | notes |
|---|---|
| `id` | integer, global, monotonically increasing. URL is `/id/{id}`. Node `1` is the root ("vrchol hierarchie"), the only node without a parent. |
| `name` | title. For replies, auto-defaults to `Re: <parent name>`, then `Re[2]:`, `Re[3]:`… by depth. |
| `content` | HTML body (sanitised) or plain text (`NO HTML` checkbox). `nl2br` flag per node. |
| `template_id` | the node's **template** (§2.2), itself a node. Decides how the node and its children render and which operations are offered. **Not a fixed type:** it can be changed via configure. |
| `parent_id` | the primary parent. |
| `vector` | materialized path of ancestor ids from root to self. Observed format: 8-digit zero-padded ids concatenated, e.g. `00000101 03391807 08479011`. Shown as "cwbe coordinatez" (one ancestor id per line) and as a tiny id-path above each post. Depth = number of segments. |
| `owner_id` | user (node) who created it. Can be changed (`set_creator`). |
| `created_at`, `updated_at` | shown as `dd.mm.yyyy - hh:mm:ss`. Posts show `(modif: …)` if edited. |
| `system_access` | `public` / `moderated` / `private` / `closed`. See §4. |
| `external_access` | bool: visible to anonymous/web visitors ("net: yes"). |
| `image` | optional node icon (avatar for users), stored as `/images/nodes/{a}/{b}/{id}.gif`. |
| `external_link` | optional, e.g. `db://user` on user nodes **[inferred: internal marker]**. |
| counters | `k` (K received), `children_count`, `descendants_count`, `views`, `last_child_at`, `last_descendant_at`. Denormalised; needed for listings. |

### 2.2 Everything is a node; templates are just defaults (decided, core principle)

There are no hard-coded "kinds" of thing. A category, forum, post, user, friend comment,
bookmark category, even system pages (bookmarks, mail, K…) are **nodes**. What makes them look and
behave differently is the node's **template**:

- A template is **itself a node** (as on kyberia: `template: 4` links to `/id/4`), with a name and
  a renderer behind it.
- The template decides three things only: (1) how the node's own content renders, (2) how its
  **children** render, (3) which operations are offered. Permissions still decide who may do what.
- **Every node has the same anatomy**: node details (image, node, template, parent, owner, viewers,
  created, updated, permissions), own content, **add form** (if you may write), children.
- **Any node can switch template** in configure (e.g. an article becomes a forum). Nothing is lost:
  the same node, the same children, rendered differently.
- New templates can be added later **without changing the data model**.

**Default templates (MVP):**

| template | children render as | add form creates |
|---|---|---|
| `nodeshell` | a listing grouped by the children's templates (`nodeshell::`, `forum::`, `submission::`, `link::`) | a child node of any template (default: forum) |
| `forum` | a discussion, threaded or flat (view switch) | a reply (`submission`) |
| `submission` | its replies as a thread | a reply |
| `user` | friend posts: flat, chronological, newest first | a friend post; posting makes you a friend |
| `friend` | (a friend post itself; renders like a post) | — |
| `system:*` | bookmarks, mail, last, RE, fr, people, K, search: their special views; no node details | per page (mail: a message) |
| `article` | **MVP: a submission with a "promotable to main" flag** | — |
| `data` | uploaded file with access control. **Post-MVP.** | — |

`link` is not a template: a `put` hard-link is a synapse row (§2.3) that appears in listings as
`link:: <name>`.

Listings print the child's template as a lowercase prefix: `nodeshell:: Hudba :: (305 children) 12 new 12 K (evad)`.

### 2.3 Synapses (links between nodes)

- **`put`**: insert an existing node (yours or anyone's) into the context of another node
  you can write to. The node is not copied. It shows up as a child (`link::`) in the target.
  "Like a UNIX symlink." The target is chosen from your bookmarks dropdown, or by typing an id.
- **`delete_hardlink`**: remove such a link.
- A node view lists **dendrites** (nodes that link *into* this one) and **axones** (nodes this one
  links *out to*). In the UI they are one link in the node column (`… commanders :: dendrites & axones`)
  that opens one page with both lists; no sidebar sections (decided).
- Store as `synapse(src_id, dst_id, created_by, created_at)`.

---

## 3. Users, identity, presence

- A user **is a node** with the `user` template. Login name = node name.
- Fields beyond the node: `login`, `password_hash`, `email`, `mood` (short status text plus a
  mood list), `mail_notify` setting, `listing_amount` (default 200), `listing_order`
  (`najnovšie hore` = newest first), `last_action_at`, `current_node_id` (where they are now).
- **Registration is gated** ("registračnou procedúrou neprejde len tak každý"). There is a
  `registrations` forum where existing members review applicants. **Decided:** sign-up form →
  pending account → **members vote** on the application in `registrations`; accepted or rejected
  by the community's rules. **TODO: find the written registration/voting rules on the site**
  (vote threshold, voting window, who may vote) and encode them here.
- **Presence:** every page view updates `last_action_at` and `current_node_id`. "Online" means
  active within the last ~15 min **[inferred]**. Shown as `[node name]` + idle time `140m44s`.
- **Friends:** add by posting a `friend` node on their profile. **Posting anything in someone's
  user node makes you their friend** — there is no separate "add friend" button.
- **User node discussion is always flat and chronological** (newest first): no threading, no
  levels, no reply-to-reply, no view switch. Every post there is a `friend` node. Friends get a separate
  "friends" section in `people` and in the bookmarks sidebar, and their avatar gets a border.
- **Ignore:** `ignore` (hide their posts) and `ignore_mail` (block their mail). Buttons on the profile.
- **Profile sidebar links:** bookmarks, movement (recent locations), their nodeshells, forums,
  submissions, articles, blogs, data, K given/received, friends, and "you have N mutual friends".

---

## 4. Permissions & moderation

Each node view shows a permissions box:
```
you:    r, w        ← your effective rights here
system: moderated   ← node.system_access
net:    yes         ← node.external_access
```

**[inferred] semantics** (confirm with long-time users):

| system_access | read | write (add children) |
|---|---|---|
| `public` | all members | all members |
| `moderated` | all members | members, but masters/operators can hide/move/silence |
| `private` | only users on the node's access list | access list |
| `closed` | all members | owner/masters only |

Per-node, per-user access rows: `node_access(node_id, user_id, read, write, master, operator, silence, ban)`.

- **owner**: full control of the node and its configuration.
- **master**: can grant access, silence and moderate inside the subtree.
- **operator**: like master, with less power **[inferred]**.
- **silence**: user can't write in this node/subtree. The site rules say silence must be
  justified in a public log (`101 silence justification arXiv`). **MVP: write an audit row
  for every silence and show the log on the node.**
- **ban**: site-wide, admin only.
- Rights inherit down the tree unless a node overrides them **[inferred]**.
- "Sirotka" (orphan) is shown in red in the post header when a post's parent is gone or
  inaccessible **[inferred]**.

Configure page (`/id/{id}/conf`, original `/id/{id}/1961033`) for owners: name, image,
system_access, external_access, template/type, nl2br ("apply on all own nodes" option),
parent (move), external_link, creator, content body (big textarea), access list
management, and for user nodes: password, email, mail notify, mood, listing amount and order.

---

## 5. K (appreciation)

- **K+** button on every node and in the discussion toolbar (bulk, using the checkboxes).
- One K per user per node. Received K shows next to the node everywhere (`205 K`, red).
- **K wallet, old style (decided):** every user has a wallet. It is refilled by a **daily
  allowance** and grows by every **K received** on your nodes. Giving K spends one from the
  wallet. Shown on bookmarks as a **daily ledger**: K včera, + denný príspevok, + dostal si dnes,
  − rozdal si dnes, = K teraz (and the current balance in the top bar). No transfers,
  treasury, 🦆/🐘 or crypto. Allowance size and whether unspent allowance accumulates: **[decide;
  match the old rules]**.
- **K page** (`/k`): nodes ordered by K received, created in the last N days (`newly
  CREATED K valued nodes`, interval input in days). Shown as full posts with a red K count +
  `K` badge on the left.
- Variants in the nav: `kNEW` (only nodes I haven't seen), `kNSFW` (NSFW-tagged nodes), `noImg`
  (same list with images hidden). **MVP: `k` and `kNEW` only.**

---

## 6. Reading what's new (the heart of the site)

### 6.1 Visit tracking
`node_visit(user_id, node_id, last_visit_at, visits)` updated on every view. Then:
- a post is **NEW** for me if `created_at > my last_visit_at` on the forum where I'm reading it.
- a listing line shows `N NEW Child` (direct children created since my visit) and
  `NEW DESCENDANT` / `descdnt` (something new deeper in the subtree) and `changed`
  (node content updated since my visit).
- Visiting a node resets its counters for me.
- The left sidebar of every node lists **recent visitors** with a small number. **[inferred:
  days since their last visit; 0 = today.]**

### 6.2 Bookmarks (`/bookmarks`)
- `book` button bookmarks a node; `unbook` removes it.
- Bookmarks are grouped into user-defined **categories** (`kategoria::#2 Politika :: 741 NEW`).
  Header shows the total NEW in the category. Uncategorised bookmarks go into a default group.
- Each line: `☐ name :: 4 NEW Child :: descdnt :: changed :: [owner]`, with the NEW count in red
  and `descdnt`/`changed` in green. Nodes with new stuff are rendered bold.
- Left sidebar: **Friends** online (avatar, `[where]`, idle time, login).
- Customize bookmarks: create/rename/delete categories and move bookmarks between them.

### 6.3 `last` (`/last`)
Global feed of the newest submissions across the site (respecting my read rights and ignores).
Each item: avatar · `Re[2]: title in <parent name>` · `author: login [lokacia :: where-they-are-now]` ·
time-date · `NEW` · body. Paged.

### 6.4 `re:` (`/re`)
Replies to *my* nodes (children of anything I own), newest first, rendered as a **flat discussion**: the same
post component as a forum in flat view, each titled `Re: <my node>`.

### 6.5 Search (`/search`)
- Full-text over name + content. Options: order by (default / K / views / created), show
  (full / short / titles), corpus (new / old **[inferred: recent index vs archive]**). Paged.
- The top bar and right column also have a **quick node-name search**: client-side regex
  over a cached JSON of `{node_id, node_name, k}` sorted by K. **MVP: server-side prefix
  search with debounced dropdown.**

---

## 7. Discussions

### 7.0 Every page is a node: one skeleton (decided)
Every page — including system pages (bookmarks /id/19, mail /id/24, last, people, K, search…) —
uses the same layout: **left node column** (starting with the node image) + content (title, then
the page). No coordinate trail. **Exception: main** has its own front-page layout.
The node column shows only: node image, `node`, `template`, `parent`, `owner`, `viewers` (plain names, not
avatars), `created`, `updated`, `permissions` (your rights :: access), `view` (threaded :: flat, discussion nodes), and links `stats :: source :: commanders :: dendrites & axones`. Below that, page-specific
sections (friends online, K wallet, fook list…). Dropped as cruft: permissions box,
visitor counts, tiamat, K-filter/synapse weights, neurons, polls.
**Exceptions:** main has its own layout; **system nodes** (mail, bookmarks, RE, fr, last, people, K, search…) show no node details at all.

### 7.1 Node view layout (forum / submission)
1. Node header content (`#topic` box).
2. **Add form**: `title or keywords::` input + `NO HTML` checkbox, a big monospace textarea,
   then a toolbar row:
   `[add] [preview] [<template#>] [helpful ▾] [<] [<<] [200] [>>] [>] [filter_by] [title/content ▾]`
   and a second row: `[K+] [delete_hardlink] [put] into [____] [bookmarks ▾] [go_to]`.
   - `helpful ▾` inserts markup snippets: tag user, link, image, bold, italic.
   - `< << 200 >> >`: paging; the number is the page size (default = `listing_amount`).
   - `filter_by` + `title/content/user` select: filter the thread.
   - Toolbar actions apply to **checked posts** (each post header has a checkbox).
3. The discussion.

### 7.2 Thread rendering
- Default is **threaded**; `show[ 2 | 3 ] flat` switches the view mode (flat = chronological).
- Each post: tiny vector path line, then avatar (50px) on the left, then a box:
  - header bar: `login ☐ dd.mm.yyyy - hh:mm:ss level: N UP NEW`
    - `level` = depth below the viewed node; `UP` links to the parent post; `NEW` in red.
  - centered title line (`Re: …`).
  - body.
- Indentation grows with depth (`level1`, `level2`… classes), and the vertical guide line is
  drawn on the left.
- Paging: newest-first top-level ordering by default (`listing_order`).

### 7.3 Writing
- Reply to a post: open the post (`/id/{post}`) and use the same add form. The new node's
  parent is that post.
- HTML is allowed (sanitised allowlist: a, b, i, u, br, p, img, blockquote, pre, code, font
  class, h1–h3, ul/ol/li, iframe for YouTube **[decide]**). `NO HTML` escapes everything.
- Edit own node via configure; `updated_at` shows `(modif: …)`.
- `fook` (decided): hides a node from **my** K list (top daily K). It doesn't affect other
  listings or other users. `unfook` reverses it.

---

## 8. Mail (`/mail`)

- Compose box at top: recipient field (login, autocomplete), textarea, `send`.
- Below it, one **chronological stream** of all my sent and received messages (not
  per-conversation threads), newest first. Each item: avatar, `from → to`, `[location: where
  sender was]`, timestamp, body, checkbox.
- Toolbar: paging, `delete_mail` (checked), `filter_by` user (= view one conversation),
  `check_all`, `NO HTML`.
- New-mail indicator in the top bar (`mail 📬`), polled.
- Left sidebar: friends avatars + all online users (click = prefill recipient).
- `ignore_mail` users can't mail you.

---

## 9. MVP scope

### In
1. Auth: login/logout, gated registration (admin approval), password change.
2. Node tree where every node has a `template_id`; default templates `nodeshell`, `forum`, `submission`, `user`,
   `friend` and the `system:*` pages. Templates are nodes; any node can switch template.
3. Node view with sidebar meta (owner, parent, template/type, coordinates, permissions,
   created/updated, K, children/descendants), child listing, threaded/flat discussion, add form.
4. Create child nodes, reply, preview, edit own, configure (subset in §4).
5. Permissions: system_access + access list + masters + silence (with log) + ban.
6. Visit tracking and NEW/descendant/changed markers.
7. Bookmarks with categories; bookmarks page with friends sidebar.
8. `last`, `re:`/`RE` (replies to me), `sub` (my submissions by month/year/parent creator, with new-reply counts),
   `fr` (friends' submissions), `k`, `kNEW`, `people`, search, quick node search.
9. Mail.
10. Friends, ignore, ignore_mail, mood, avatar upload.
11. `put` / `delete_hardlink`, dendrites/axones.
12. Top-bar nav exactly as in the design manual.

### Out (later, or never)
- k26 portal homepage (user explicitly rejected it). `/` should redirect to `main` (node 1 view)
  or to bookmarks for logged-in users **[decide]**.
- KOL / Solana wallet / 🦆🐘 / K-treasury / giver.eu / Kyberia Feudum Licence tooling.
- Chat (`/chat/chat.htm`).
- User-authored Smarty templates, per-node templates, header templates, "kyberia API".
- K-neurons / synapse weights / K-filter sliders, stats, tiamat, commanders, polls.
- `data` file nodes, galleries, unzip.
- Skins.

---

## 10. URL map (keep `/id/{n}` stable, which matters for decades of internal links)

| original | clone | notes |
|---|---|---|
| `/id/{n}` | `/id/{n}` | node view. **Must keep the ids when importing.** |
| `/id/{n}/{template}` | `/id/{n}/{view}` | view variants: `conf`, `flat`, `k`, `history` |
| `/id/1` (main) | `/id/1` | |
| `/id/101` (kyberia) | `/id/101` | the community nodeshell root |
| `/id/19` | `/bookmarks` | also alias `/id/19` |
| `/id/24` | `/mail` | |
| `/id/35`, `/id/23` | `/last` | |
| `/id/1522695` | `/re` | |
| `/id/27` | `/people` | |
| `/id/15` | `/k` | |
| `/id/25` | `/search` | |
| `/id/{me}/1961033` | `/id/{me}/conf` | |

Keep the system aliases (`/id/19`, `/id/24`, …) as redirects so old links work.

---

## 11. Data model (Postgres sketch)

```sql
nodes(id bigint pk, name text, content text, template_id bigint /* -> nodes.id */, parent_id bigint,
      path bigint[] /* vector */, depth int, owner_id bigint,
      system_access text, external_access bool, nl2br bool, no_html bool,
      image text, external_link text,
      k int, children_count int, descendants_count int, views int,
      last_child_at timestamptz, last_descendant_at timestamptz,
      created_at timestamptz, updated_at timestamptz, deleted_at timestamptz,
      search tsvector)
  -- indexes: parent_id+created_at, GIN(path), GIN(search), owner_id+created_at

users(node_id pk -> nodes, login citext unique, password_hash, email, mood,
      listing_amount int default 200, listing_order text, mail_notify text,
      status text /* pending|active|banned */, last_action_at, current_node_id,
      k_allowance int, k_allowance_reset_at)

node_access(node_id, user_id, can_read, can_write, is_master, is_operator,
            silenced_until, pk(node_id,user_id))
moderation_log(id, node_id, actor_id, target_user_id, action, reason, created_at)
synapses(src_id, dst_id, created_by, created_at, pk(src_id,dst_id))
k_votes(user_id, node_id, created_at, pk(user_id,node_id))
node_visits(user_id, node_id, last_visit_at, visits, pk(user_id,node_id))
bookmark_categories(id, user_id, name, position)
bookmarks(user_id, node_id, category_id null, created_at, pk(user_id,node_id))
fooked_nodes(user_id, node_id)          -- fook: excluded from my K list
ignores(user_id, target_id, kind /* posts|mail */)
messages(id, from_id, to_id, body, no_html, sender_location_node_id,
         created_at, read_at, deleted_by_sender, deleted_by_recipient)
```

Counting NEW children per bookmark is the hot query: `count(children where created_at >
visit.last_visit_at)` for ~100 bookmarks per page load. Use `last_child_at` /
`last_descendant_at` to skip unchanged nodes cheaply, then count only the changed ones.

---

## 12. Tech recommendation

- **Server-rendered HTML, near-zero JS.** The site is a dense text UI, and old-timers expect
  everything to work with plain forms. JS is only for quick search, the mail poll and the
  `helpful` inserts.
- Suggested stack: TypeScript + Next.js App Router (Server Components and Server Actions as
  plain form posts) + Postgres. Any server-rendered stack works (Rails, Django, Laravel).
- HTML sanitising on write *and* render (DOMPurify/sanitize-html allowlist).
- Data import: a one-time migration from the MySQL dump, preserving node ids, vectors and
  timestamps.
- Performance budget: the original prints `page generation took 0.0078 sec`. Keep the footer
  and keep the number honest.

---

## 13. Open questions for the community/admins
1. Exact semantics of `moderated` vs `closed`, and of the `operator` vs `master` roles.
2. ~~Registration approval~~: member voting (decided). Still need the written rules.
3. ~~K~~: wallet = daily allowance + K received (decided). Allowance size TBD.
4. What the number next to each name in the sidebar visitor list means.
5. ~~`fook`~~: hides a node from my K list (decided).
6. Allowed HTML tags in posts (iframes/embeds?).
7. Should non-members see anything (`net: yes` nodes) in the MVP?
