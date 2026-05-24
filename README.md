# Intergroup Dynamics Lab Website

This is the website of the **Intergroup Dynamics Lab** — the Culture, Cognition & Emotion research group at the University of the Basque Country (UPV/EHU), led by Dr. Magdalena Bobowik and Dr. Maitane Arnoso.

The site is built with [Jekyll](https://jekyllrb.com/) and Bootstrap, based on the [Allan Lab template](https://www.allanlab.org/aboutwebsite.html).

## Running locally

```bash
jekyll serve
```

Then open `http://localhost:4000` in your browser.

## Structure

- `_pages/` — content pages (home, team, research, publications, teaching, openings)
- `_data/` — YAML data files for team members, students, publications, and news
- `_layouts/` — page layouts
- `_includes/` — shared partials (header, footer, news sidebar)
- `images/` — photos organised into `teampic/`, `logopic/`, `slider7001400/`, `pubpic/`

## Adding content

- **Team members** → edit `_data/team_members.yml`; add photos to `images/teampic/`
- **PhD students** → edit `_data/students.yml`
- **News** → edit `_data/news.yml`
- **Publications** → edit `_data/publist.yml`

---

Template originally by the Allan Lab. Code released under the MIT License.
