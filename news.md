---
title: "Common Futures Research Collective - News"
layout: gridlay
excerpt: "Common Futures Research Collective – News"
sitemap: false
permalink: /news/
---

# News

{% assign number_printed = 0 %}
{% for article in site.data.news %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ article.image }}" class="img-responsive" width="33%" style="float: left" />
  <pubtit>{{ article.date }} &mdash; {{ article.category }}</pubtit>
  <div>{{ article.headline | markdownify }}</div>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
