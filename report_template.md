# Research Report

## Topic:
{{ topic }}

## Executive Summary
{{ summary }}

## Key Findings
{% for finding in findings %}
- **{{ finding.question }}**  
  {{ finding.answer }}  
  {% endfor %}

## Sources
{% for source in sources %}
- {{ source }}
  {% endfor %}
