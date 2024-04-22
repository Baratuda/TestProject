from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.main_page, name = 'main_page'),
    # path("__debug__/", include("debug_toolbar.urls")),
    path('<str:parent_id>/<slug:menu_name>/', views.view_menu_description, name = 'view_menu_description'),
]
