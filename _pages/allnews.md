---
title: "News"
layout: textlay
excerpt: "Intergroup Dynamics Lab at Leiden University."
sitemap: false
permalink: /allnews.html
published: false
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br> {{ article.headline | markdownify}}</p>
{% endfor %}
