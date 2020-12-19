from django import template

register = template.Library()


@register.filter
def in_category(menu_items, category):
    return menu_items.filter(category=category)
