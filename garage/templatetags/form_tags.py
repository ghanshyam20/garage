"""Template tags to help with form rendering."""

from __future__ import annotations


from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class: str):
    """Add a CSS class to a form field widget.  Usage: {{ form.field|add_class:'my-class' }}"""
    return field.as_widget(attrs={'class': css_class})