from django import template

register = template.Library()

@register.filter(name='split')
def split(value, args):
    return value.split(args)
