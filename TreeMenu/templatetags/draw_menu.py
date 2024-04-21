from django import template
from TreeMenu.models import Menu
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('TreeMenu/draw_menu.html')
def draw_menu(menu, all_items=[]):
    if all_items!= []:
        items = []
        for i in all_items[:]:
            if str(i.parent_id) == menu:
                items.append(i)
                all_items.remove(i)
        return {'items': items, 'all_items':all_items}
    else:    
        items = Menu.objects.filter( Q(main_menu = menu) | Q(title = menu)) 
        main_menu = [ item for item in items if str(item.pk) == menu ]
        all_items = [ item for item in items if str(item.main_menu_id)==menu ]
        return {'items': main_menu, 'all_items':all_items}


@register.simple_tag()
def has_children(menu, all_items):
    for i in all_items:
        if str(i.parent_id) == menu.title:
            return {'has_children':True, 'id': str(menu.slug)+str(menu.parent_id)}
    return {'has_children':False,'id': str(menu.slug)+str(menu.parent_id)}