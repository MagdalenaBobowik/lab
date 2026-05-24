---
title: "Intergroup Dynamics Lab - Outreach"
layout: textlay
excerpt: "Intergroup Dynamics Lab – Outreach & Knowledge Transfer"
sitemap: false
permalink: /outreach/
---

# Outreach & Knowledge Transfer

We are committed to bringing research out of the lab and into society. Below are our knowledge transfer projects — collaborations with public institutions, NGOs, and civil society organisations that translate scientific findings into concrete social tools, programmes, and interventions.

---

<div class="outreach-list">
{% for project in site.data.outreach %}
<div class="outreach-card">
  <div class="outreach-accent"></div>
  <div class="outreach-body">
    <div class="outreach-title">{{ project.title }}</div>
    <div class="outreach-funder">{{ project.funder }}</div>
    {% if project.note %}
    <div class="outreach-note">{{ project.note }}</div>
    {% endif %}
    <div class="outreach-meta">
      <span class="outreach-dates">
        {% if project.end != "" %}
          {{ project.start }} – {{ project.end }}
        {% else %}
          {{ project.start }}{% if project.start != "2021" %} – present{% endif %}
        {% endif %}
      </span>
      {% if project.amount != "" %}
      <span class="outreach-amount">{{ project.amount }}</span>
      {% endif %}
      {% if project.role != "" %}
      <span class="outreach-role">{{ project.role }}</span>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}
</div>

<style>
.outreach-list {
  margin-top: 28px;
}

.outreach-card {
  display: flex;
  align-items: stretch;
  margin-bottom: 18px;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  background: #fff;
  overflow: hidden;
  transition: box-shadow 0.2s;
}

.outreach-card:hover {
  box-shadow: 0 4px 16px rgba(123,50,165,0.13);
}

.outreach-accent {
  width: 6px;
  flex-shrink: 0;
  background: linear-gradient(180deg, #7B32A5 0%, #F29E00 100%);
}

.outreach-body {
  padding: 16px 20px 14px 20px;
  flex: 1;
}

.outreach-title {
  font-weight: bold;
  font-size: 1.01em;
  color: #7B32A5;
  margin-bottom: 4px;
  line-height: 1.4;
}

.outreach-funder {
  font-size: 0.93em;
  color: #555;
  margin-bottom: 6px;
}

.outreach-note {
  font-size: 0.88em;
  color: #777;
  font-style: italic;
  margin-bottom: 6px;
}

.outreach-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  margin-top: 4px;
}

.outreach-dates {
  font-size: 0.85em;
  color: #888;
  background: #f5f5f5;
  padding: 2px 9px;
  border-radius: 20px;
  border: 1px solid #e8e8e8;
}

.outreach-amount {
  font-size: 0.85em;
  font-weight: bold;
  color: #B05A00;
  background: #fff7ed;
  padding: 2px 9px;
  border-radius: 20px;
  border: 1px solid #ffe0b0;
}

.outreach-role {
  font-size: 0.82em;
  color: #7B32A5;
  background: #f3eafc;
  padding: 2px 9px;
  border-radius: 20px;
  border: 1px solid #ddc8f5;
}
</style>
