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
