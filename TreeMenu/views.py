from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from .models import Menu
from django.db.models import Q
from django.views.generic import DetailView

def main_page(request):
    """ 
    Функция представление отображающая главную страницу
    """
    return render(request, 'base.html') 

def view_menu_description(request, menu_name, parent_id):
    """ 
    Функция представление  отображающая информацию о 
    конкретном меню или подменю
    """
    if parent_id == 'main':
        content = get_object_or_404(Menu, slug=menu_name).content
    else: 
        content = get_object_or_404(Menu, slug=menu_name,parent=parent_id).content
    return render(request, 'TreeMenu/index.html', {'content' : content, 'title' : menu_name}) 


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
