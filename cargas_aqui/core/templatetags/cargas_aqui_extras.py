from django import template

register = template.Library()

@register.inclusion_tag('tags/navlink.html')
def navlink(label, route):
    return {
        'label': label,
        'route': route
    }