---
title: "Common Futures Research Collective - Team"
layout: gridlay
excerpt: "Common Futures Research Collective: Team members"
sitemap: false
permalink: /team/
---

# Group Members

 **We are looking for new PhD students and Postdocs to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**


Jump to [members](#members), [international collaborators](#international-collaborators).

## Members
{% assign all_members = site.data.pis | concat: site.data.professors | concat: site.data.postdocs | concat: site.data.phd_students %}
{% assign number_printed = 0 %}
{% for member in all_members %}

{% assign mod3 = number_printed | modulo: 3 %}

{% if mod3 == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive teampic" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}</i>
  <ul style="overflow: hidden">
  {% if member.education1 %}<li> {{ member.education1 | markdownify }} </li>{% endif %}
  {% if member.education2 %}<li> {{ member.education2 | markdownify }} </li>{% endif %}
  {% if member.education3 %}<li> {{ member.education3 | markdownify }} </li>{% endif %}
  {% if member.education4 %}<li> {{ member.education4 | markdownify }} </li>{% endif %}
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if mod3 == 2 %}
</div>
{% endif %}

{% endfor %}

{% assign mod3 = number_printed | modulo: 3 %}
{% if mod3 != 0 %}
</div>
{% endif %}


<hr style="margin: 40px 0;">

## International Collaborators

{% assign number_printed = 0 %}
{% for member in site.data.collaborators %}

{% assign mod3 = number_printed | modulo: 3 %}

{% if mod3 == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive teampic" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}</i>
  <ul style="overflow: hidden">
  <li>{{ member.research }}</li>
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if mod3 == 2 %}
</div>
{% endif %}

{% endfor %}

{% assign mod3 = number_printed | modulo: 3 %}
{% if mod3 != 0 %}
</div>
{% endif %}
