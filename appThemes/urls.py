from django.urls import path
from appThemes.views import index, themes_list, theme_detail, add_theme, edit_theme, delete_theme

urlpatterns = [
    path('', index, name='index'),
    path('themes/', themes_list, name='themes_list'),
    path('<int:id>', theme_detail, name='theme_detail'),
    path('addtheme/', add_theme, name='add_theme'),
    path('edit/<int:id>', edit_theme, name='edit_theme'),
    path('delete/<int:pk>', delete_theme, name='delete_theme'),
]