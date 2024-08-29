from django import template
from menu.models import MenuItem

import inspect

register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def main_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }