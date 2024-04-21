from django.shortcuts import render
from .models import Menu
from django.db.models import Q

def main_page(request):
    return render(request, 'base.html') 

def view_menu_description(request, menu_name, parent_id):
    if parent_id == 'main':
        content = Menu.objects.values('content').get(slug=menu_name)
    else: 
        content = Menu.objects.values('content').get( Q(slug=menu_name) & Q(parent=parent_id))
    return render(request, 'TreeMenu/index.html', {'content':content['content']}) 



