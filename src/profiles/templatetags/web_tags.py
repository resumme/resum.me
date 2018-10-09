from django import template

register = template.Library()

@register.filter
def define_column(num, val):
    return num % val