---
title: "Intergroup Dynamics Lab - Team"
layout: gridlay
excerpt: "Intergroup Dynamics Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

 **We are looking for new PhD students and Postdocs to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**


Jump to [principal investigators](#principal-investigators), [postdoctoral researchers](#postdoctoral-researchers), [phd candidates](#phd-candidates), [professors](#professors), [international collaborators](#international-collaborators).

## Principal Investigators
{% assign number_printed = 0 %}
{% for member in site.data.pis %}

{% assign mod3 = number_printed | modulo: 3 %}

{% if mod3 == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive teampic" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  <li> {{ member.education4 | markdownify}} </li>
  {% endif %}

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


## Postdoctoral Researchers
{% assign number_printed = 0 %}
{% for member in site.data.postdocs %}

{% assign mod3 = number_printed | modulo: 3 %}

{% if mod3 == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive teampic" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  {% endif %}

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


## PhD Candidates
{% assign number_printed = 0 %}
{% for member in site.data.phd_students %}

{% assign mod4 = number_printed | modulo: 4 %}

{% if mod4 == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-3 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive teampic" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if mod4 == 3 %}
</div>
{% endif %}

{% endfor %}

{% assign mod4 = number_printed | modulo: 4 %}
{% if mod4 != 0 %}
</div>
{% endif %}


## Professors
{% assign number_printed = 0 %}
{% for member in site.data.professors %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive teampic" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  </ul>
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
