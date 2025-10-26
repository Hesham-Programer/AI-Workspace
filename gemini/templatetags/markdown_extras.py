from django import template
from django.utils.safestring import mark_safe
from markdown_it import MarkdownIt

register = template.Library()


@register.filter(name="markdown_safe")
def markdown_safe(text):
    md = MarkdownIt()
    return mark_safe(md.render(text))

