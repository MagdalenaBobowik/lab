---
title: "Common Futures Research Collective - Publications"
layout: gridlay
excerpt: "Common Futures Research Collective -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

All pre-registered data and materials are available on our [OSF repository](https://osf.io/6ep39/).

## Group highlights

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p>{{ publi.authors }} ({{ publi.year }}). <em>{{ publi.link.display }}</em>.{% if publi.link.url %} <a href="{{ publi.link.url }}">{{ publi.link.url }}</a>{% endif %}</p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>


## Full List of Publications

{% for publi in site.data.publist %}

  <p>{{ publi.authors }} ({{ publi.year }}). {{ publi.title }}. <em>{{ publi.link.display }}</em>.{% if publi.link.url %} <a href="{{ publi.link.url }}">{{ publi.link.url }}</a>{% endif %}</p>

{% endfor %}
