# Common Futures Research Collective Website

This is the website of the **Common Futures Research Collective**, a social psychology lab at the University of the Basque Country (UPV/EHU), coordinated by Magdalena Bobowik and Maitane Arnoso. The lab is part of the Consolidated Research Group “Lotuneak: Human Bonds for Change” (IT1797-26), supported by the Basque Government, within the research line Intergroup Relations and Social Participation.

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

- **Team members** → edit `_data/pis.yml` (coordinators), `_data/professors.yml`, `_data/postdocs.yml` or `_data/phd_students.yml`; all are shown together in one Members list, in that order. Add photos to `images/teampic/`
- **International collaborators** → edit `_data/collaborators.yml`
- **News** → edit `_data/news.yml`
- **Publications** → edit `_data/publist.yml`

---

Template originally by the Allan Lab. Code released under the MIT License.
