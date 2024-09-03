from django import template

register = template.Library()

@register.filter(name='get_rooms')
def get_rooms(d,i):
    try:
        return d[i]
    except:
        return []