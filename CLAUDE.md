# CLAUDE.md

Las convenciones de este proyecto (estructura, estilo, assets, Google Analytics y el
proceso paso a paso para crear un nuevo artículo de blog) están documentadas en
**[AGENT.md](./AGENT.md)**.

`AGENT.md` es la única fuente de verdad — léelo antes de crear o modificar páginas.

## Resumen rápido

- Sitio estático (portafolio + blog) de Arturo J. Delgado S. para GitHub Pages con dominio propio.
- Un artículo = `blog/<slug>.html`; sus imágenes en `assets/<slug>/`.
- Assets compartidos (logo, favicons) en `assets/`.
- Color de acento `#80abc8`, contenido en español, Font Awesome 4.7.0.
- Google Analytics GA4: `G-KFW5JJ3DJT` en `<head>` de todas las páginas.
- Para un post nuevo: reutiliza el `<head>`/header/footer de un post existente como plantilla,
  escapa el código dentro de `<pre><code>`, y enlázalo desde la sección `#blog` de `index.html`.

## Presupuesto SEO on-page (los 2 límites que siempre se escapan)

- **`<meta name="description">` ≤ 158 caracteres** (ideal 145–155). Google corta el snippet
  alrededor de los 155–160. Debe ser **idéntica** en los 4 sitios: `meta description`,
  `og:description`, `twitter:description` y el `description` del JSON-LD.
- **≥ 50% de los `<h2>` mencionan la keyword objetivo.** Un post con 2 de 17 `<h2>` nombrando
  la keyword se lee como fuera de tema para un crawler.
- **Nunca falsear la cobertura:** un heading solo lleva la keyword si esa sección habla de verdad
  del tema. Headings verídicos en ~70% de las secciones valen más que 100% con etiquetas falsas.
- `llms.txt` y la tarjeta de `index.html` están **exentos** del límite de 158 — no son snippets
  de buscador.

Detalles, comandos de verificación y el paso 13 del proceso están en **[AGENT.md](./AGENT.md)**.
