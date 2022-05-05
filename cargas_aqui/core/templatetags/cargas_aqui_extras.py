from django import template

register = template.Library()

@register.inclusion_tag('tags/navlink.html')
def navlink(label, route):
    return {
        'label': label,
        'route': route
    }

@register.simple_tag
def admin_row_classes(cl, index):
    if not hasattr(cl.model_admin, 'get_row_classes'):
        return u''
    return cl.model_admin.get_row_classes(cl.result_list[index], index)