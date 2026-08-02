# AGENT.md — ajdelgados.com project guide

Personal static site (portfolio + blog) for Arturo J. Delgado S., meant to be
deployed on **GitHub Pages with a custom domain** (`ajdelgados.com`). It's a
replica of the old WordPress site, rebuilt as plain
HTML with no framework and no build step.

## Project structure

```
ajdelgados/
├── index.html                 # Home page (hero, "Sobre mí", 4 latest posts)
├── blog/
│   └── <slug>.html            # One file per article
└── assets/
    ├── logo_60x60.png         # Shared (used by every page)
    ├── favicon-32x32.png
    ├── favicon-192x192.png
    ├── apple-touch-icon.png
    └── <slug>/                # Per-article images (if the post has any)
        └── *.png
```

**Path rules:**
- `index.html` (root) references assets as `assets/…` and posts as `blog/<slug>.html`.
- Posts (inside `blog/`) reference with `../`:
  - Shared assets → `../assets/logo_60x60.png`, `../assets/favicon-*`
  - Post images → `../assets/<slug>/<image>.png`
  - Back to home → `../index.html`, `../index.html#inicio`, `../index.html#blog`
- **The `slug`** is the title in lowercase, without accents, hyphen-separated (same as the
  original WordPress URL). E.g. `react-con-aws-cognito-para-autenticacion-de-usuario`.
- If the post has no images, **do not** create a folder in `assets/` (Git doesn't track
  empty directories).

## Style (design system)

All values live in each page's inline `<style>`
(there is no external CSS). CSS variables in `:root`:

| Variable | Value | Use |
|---|---|---|
| `--accent` | `#80abc8` | Steel-blue — used on dark surfaces (footer/hero) and non-text UI (divider, icon fills, hover backgrounds), where it passes contrast |
| `--link` | `#3f7597` | Link/interactive text on light surfaces — darker sibling that passes WCAG AA (5.0:1 on white) |
| `--link-hover` | `#2b5e80` | Link, nav, and title hover on light surfaces (6.96:1 on white) |
| `--dark` | `#2d3033` | Dark header/footer, heading text |
| `--text` | `#616161` | Body text |
| `--heading` | `#333` | Headings |
| `--bg` | `#ffffff` | Background |
| `--light` | `#f7f7f7` | Blog section background |
| `--border` | `#ededed` | Borders |

Other conventions:
- Font: `"Helvetica Neue", Helvetica, Arial, sans-serif`, `font-size: 15px`, `line-height: 1.7`.
- `<blockquote>` inside `article.post-content` gets a 3px `--accent` left border and
  `--heading` text — use it to pull out a key takeaway, not for long quoted passages.
- Language: **Spanish** (`<html lang="es">`), all content in Spanish.
- **Font Awesome 4.7.0** via cdnjs for icons (features and social media).
  Icons used in features: `fa-bolt` (Ágil), `fa-microchip` (Innovador), `fa-cubes` (Lógico).
- Header: logo + `#header-text` (`#site-title` with a link + `#site-description`) + nav.
- Dark footer with social icons (LinkedIn, Facebook, Twitter) centered above the copyright.
- Social media (real URLs):
  - `https://www.linkedin.com/in/ajdelgados`
  - `https://www.facebook.com/ajdelgados`
  - `https://www.twitter.com/ajdelgados`

## Google Analytics

Every page carries the GA4 tag **`G-KFW5JJ3DJT`** (same ID as the live site), placed
right after `<meta charset="UTF-8">`, as high as possible in `<head>`:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-KFW5JJ3DJT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-KFW5JJ3DJT');
</script>
```

## SEO

### On-page budget — the two limits that get missed

These are the two findings that keep coming back in SEO audits of this site. Check them
**while writing** the post, not after:

| Check | Limit | Why |
|---|---|---|
| **`<meta name="description">` length** | **≤ 158 characters** (aim 145–155) | Google cuts the snippet around 155–160 chars. Past that the sentence is truncated mid-word and the value proposition is lost. |
| **Keyword coverage in `<h2>`** | **≥ 50% of the `<h2>`s** name the target keyword | Headings are the strongest on-page structural signal after the `<h1>`. A post with 2 of 17 `<h2>`s mentioning the keyword reads as off-topic to a crawler. |

**Never fake the coverage.** A heading only gets the keyword if that section genuinely talks
about it — `Paso 7: descartes físicos RTSP` is a lie when the section is about cables and
voltage, and Google reads it as keyword stuffing. Truthful headings on ~70% of sections beat
100% with false labels. Sections that legitimately cover something else stay as they are;
that's a correct result, not a miss.

Rewriting a heading for coverage is also a chance to make it **long-tail searchable** — phrase
it the way someone types the query (`Resolver el 401 Unauthorized de RTSP` over `Resolver el
401`), so it stands on its own in a featured snippet or a shared table of contents.

Other on-page rules: the keyword belongs in the `<title>`, the `<h1>`, the first paragraph, and
at least one `<h2>` in the first third of the article. The description must be **identical**
across all four places it appears (`meta description`, `og:description`, `twitter:description`,
and the JSON-LD `description`) — see step 13 for how to verify that.

`llms.txt` is **exempt** from the 158-char limit: it's a map for LLMs, not a search snippet, so
a longer and more detailed summary there is correct. The `index.html` card is also exempt — it's
home-page copy meant to pull in a reader already on the site, with a different job than a SERP
snippet. Both should stay *coherent* with the description, not identical to it.

### Site-wide files and per-page tags

Every page carries a full SEO layer. Site-wide files at the root: **`sitemap.xml`**
(lists every URL), **`robots.txt`** (allows all crawlers, points to the sitemap), and
**`llms.txt`** (a Markdown map of the site for LLMs — the proposed llmstxt.org format:
an `# H1` title, a `>` blockquote summary, and a `## Blog` list of every post as
`[title](absolute-url): description`).

Each page's `<head>` includes, right after `<meta name="description">`:

- `<link rel="canonical">` — the page's absolute URL (`https://ajdelgados.com/…`).
- `<meta name="author">`, `<meta name="keywords">`, `<meta name="robots" content="index, follow">`.
- **Open Graph** — `og:type` (`website` for home, `article` for posts), `og:site_name`
  (`AJDELGADOS`), `og:locale` (`es_ES`), `og:title`, `og:description`, `og:url`,
  `og:image` (+ `og:image:width` 1200 / `og:image:height` 630). Posts also add
  `article:published_time` and `article:author`.
- **Twitter Card** — `twitter:card` = `summary_large_image`, `twitter:site` = `@ajdelgados`,
  `twitter:title`, `twitter:description`, `twitter:image`.
- Descriptions with a literal `&` must be escaped as `&amp;` in meta content.

Just before `</head>`, a **JSON-LD** structured-data block:
- Home → `WebSite` schema (Person author with `sameAs` social links).
- Posts → `BlogPosting` schema (`headline`, `description`, `image`, `datePublished`,
  `dateModified`, `author`, `publisher`).

**One `<h1>` per page.** The header `#site-title` is a `<div id="site-title">` (NOT an
`<h1>`) so the only real `<h1>` is the page/article heading. (Code examples inside
`<pre><code>` may contain escaped `<h1>` text — that's fine, it's not a rendered heading.)

### Share images (og:image)

Each page uses a branded **1200×630 PNG** (the 1.91:1 ratio social platforms expect):
- Home → `assets/og-home.png`
- Post → `assets/<slug>/og.png`

They're generated by **`scripts/make-og-image.py`** (Python **Pillow** — light `#f7f7f7`
background, left accent bar `#80abc8`, logo + `AJDELGADOS` brand top-left, the title
wrapped in dark `#333` text, and a `Blog · ajdelgados.com` line at the bottom). Requires
`pip3 install pillow`. Usage:

```bash
# New blog post -> assets/<slug>/og.png
python3 scripts/make-og-image.py --slug <slug> --title "<Post title>"

# Home page -> assets/og-home.png
python3 scripts/make-og-image.py --home --title "Software Developer & Software Architect"
```

## How to create a new blog article

The existing posts were migrated from WordPress. The process to migrate/create one:

1. **Pick the slug** from the title (lowercase, no accents, hyphen-separated).

2. **Get the content.** If it comes from the original WordPress URL, extract only the
   `<div class="entry-content">` and **cut off when you reach** `<div class="extra-hatom-entry-title">`
   (that's where the real content ends; after it come comments, tags, and the theme's
   navigation, which are NOT copied).

3. **Download the images** to `assets/<slug>/` keeping the original filename. Rewrite each
   `src` to `../assets/<slug>/<image>` (strip the ShortPixel wrapper; always use the
   original `wp-content/uploads/...` URL).

4. **Clean the WordPress HTML:**
   - `<p class="wp-block-paragraph">` → `<p>`
   - `<hN class="wp-block-heading">` → `<hN>`
   - `<pre class="wp-block-preformatted">` → `<pre><code>…</code></pre>`
   - `<figure class="…">` → `<figure>`
   - Remove `<strong>` used as highlighting INSIDE code blocks (in WordPress some posts
     mark lines with `<strong>`; drop it). `<strong>` in headings or normal paragraphs
     is kept.

5. **Escape the code.** Inside `<pre><code>…</code></pre>` every `<`, `>`, `&` must be an
   entity (`&lt;`, `&gt;`, `&amp;`). This is CRITICAL: example JSX/HTML (`<div>`,
   `<Module>`, etc.) breaks the page if not escaped. Verify no code block contains
   unescaped tags before considering it done.

6. **Assemble the page** by reusing the `<head>`/header/footer of an existing post
   (`blog/react-con-aws-cognito-para-autenticacion-de-usuario.html` works as a template).
   Change per article:
   - `<title>` → `<Post title> — AJDELGADOS`
   - `<meta name="description">` → post summary
   - `.article-header` `<h1>` → post title
   - `.meta` → `Publicado el <date in Spanish> &middot; por Arturo J. Delgado S.`
     (date taken from the original `datetime`, e.g. "28 de octubre de 2020")
   - `.post-tags` at the end → `<strong>Etiquetado en:</strong> Tag1 &middot; Tag2 …`

7. **Link from `index.html`.** In the `#blog` section ("Lo último del Blog"), add a new
   `<article class="post">` as the **first** card (newest first): an `<h3><a>` with the
   title, a `<p>` summary, and an `<a class="read-more">`. Both links point to
   `blog/<slug>.html`.

   **The section shows exactly the 4 most recent posts** — when you add one, delete the
   oldest card so the count stays at 4. The grid is `repeat(2, 1fr)`, so 4 keeps a full
   2×2 with no orphan card in the last row. Dropping a post from the home page does **not**
   unpublish it: its page, `sitemap.xml` entry, and `llms.txt` bullet all stay (those lists
   are complete, not "latest"), so it remains indexable and reachable by URL.

8. **Add the SEO layer** to the new page (see the SEO section above): canonical, author,
   keywords, robots, full Open Graph + Twitter Card meta, and a `BlogPosting` JSON-LD block.
   Use `og:type` = `article` and fill `datePublished`/`article:published_time` with the
   post date (ISO `YYYY-MM-DD`). Ensure exactly one `<h1>` (the header title stays a
   `<div id="site-title">`).

9. **Generate the share image**: run
   `python3 scripts/make-og-image.py --slug <slug> --title "<Post title>"` (creates the
   branded 1200×630 `assets/<slug>/og.png`), then point `og:image` + `twitter:image` at
   `https://ajdelgados.com/assets/<slug>/og.png` (with `og:image:width`/`height`).

10. **Add the URL to `sitemap.xml`** — a new `<url>` block with `<loc>` (absolute URL),
    `<lastmod>` (post date), `<changefreq>yearly</changefreq>`, `<priority>0.8</priority>`.

11. **Add the post to `llms.txt`** — a new bullet under `## Blog`:
    `- [<title>](https://ajdelgados.com/blog/<slug>.html): <description>`.

12. **Update `README.md`.** The README (GitHub profile, in English) mentions the blog topics
    in the *"Read my blog about …"* line. If the new article introduces a technology/topic
    not yet listed, add it to keep the list current.

13. **Run the SEO evaluation.** Pick the post's **target keyword** (usually the main technology
    or protocol — `RTSP`, `AWS Secrets Manager`, `Mautic`) and check it against the on-page
    budget in the SEO section above. Two commands, run from the repo root:

    ```bash
    # 1. Description length (<= 158) + same text in every place it appears.
    #    Posts expect 4 copies (meta, og, twitter, JSON-LD BlogPosting).
    #    index.html expects 3 — the WebSite schema has no description field.
    python3 - <<'PY'
    import re, glob, html
    for f in sorted(glob.glob('blog/*.html')) + ['index.html']:
        s = open(f).read()
        d = re.search(r'<meta name="description" content="(.*?)">', s)
        if not d: continue
        desc = d.group(1)
        n = len(html.unescape(desc))
        # compare unescaped: og:/twitter: escape a literal & as &amp;
        copies = html.unescape(s).count(html.unescape(desc))
        want = 3 if f == 'index.html' else 4
        print(f"{n:4d} {'OK ' if n <= 158 else 'LONG'}  copies={copies}/{want} "
              f"{'OK' if copies == want else 'MISMATCH'}  {f}")
    PY

    # 2. Keyword coverage in H2 — must be >= 50%
    f=blog/<slug>.html; kw='RTSP'
    echo "$(grep -c "<h2>[^<]*$kw" $f) of $(grep -c '<h2>' $f) H2 mention '$kw'"
    ```

    If coverage is under half, rewrite the headings where the keyword is **genuinely**
    descriptive of that section — and leave the rest alone (see the "Never fake the coverage"
    rule above). Report the final ratio and say explicitly which sections were left without the
    keyword and why.

14. **Verify** before finishing:
    - Every path (`../assets/…`, `../index.html`, the `og.png`) resolves to existing files.
    - `<article>` opens and closes exactly once; exactly one rendered `<h1>`.
    - Zero unescaped tags inside code blocks.
    - The Google Analytics tag is present.
    - Canonical + OG + Twitter + JSON-LD present; JSON-LD parses as valid JSON.
    - **`<meta name="description">` is ≤ 158 chars and identical in all 4 locations.**
    - **At least half the `<h2>`s name the target keyword** (truthfully).
    - The post is listed in both `sitemap.xml` and `llms.txt`.
    - `index.html` has exactly 4 `<article class="post">` cards, newest first.

## Post page structure

```
<head>
  <meta charset="UTF-8">
  <!-- Google tag (gtag.js) -->        ← GA4 G-KFW5JJ3DJT
  <meta viewport>
  <title> … — AJDELGADOS</title>
  <meta description>
  <link rel="canonical" …>                 ← SEO
  <meta author / keywords / robots>        ← SEO
  <!-- Open Graph --> og:type=article, title, description, url, image (1200×630) …
  <!-- Twitter Card --> summary_large_image …
  <link rel="icon" … ../assets/favicon-*>
  <link rel="apple-touch-icon" … ../assets/apple-touch-icon.png>
  <link Font Awesome 4.7.0>
  <style> … (same block on every page) </style>
  <script type="application/ld+json"> … BlogPosting … </script>
</head>
<body>
  <header class="site-header"> … logo + nav (links to ../index.html) </header>
  <div class="article-header"> … <h1> title + .meta date </div>
  <article class="post-content">
    <a class="back-link" href="../index.html#blog">← Volver al blog</a>
    … post content …
    <p class="post-tags"> … </p>
    <a class="back-link"> … </a>
  </article>
  <footer class="site-footer"> … social media + copyright </footer>
</body>
```

## Deployment (GitHub Pages + custom domain)

- 100% static site; served as-is with no build.
- For a custom domain you need a `CNAME` file at the root containing `ajdelgados.com`,
  DNS records (4 `A` records to GitHub Pages IPs + a `CNAME` for `www`), and enabling
  "Enforce HTTPS" under Settings → Pages.

## Notes / decisions made

- Favicons are PNG (not `.ico`), reusing the logo at several sizes — same as the live site.
- The clean gtag.js snippet is used instead of WordPress's MonsterInsights wrapper.
- Shared assets are kept in `assets/` (root) to avoid duplicating logo/favicons per post.
