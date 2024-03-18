from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from .models import Themes, Category


# Create your views here.


def index(request):
    return render(request, 'index.html')


def themes_list(request):
    themes = Themes.objects.all()
    return render(request, 'themes.html', {'themes': themes})

def theme_detail(request, id):
    theme = Themes.objects.get(id=id)
    return render(request, 'themes_detail.html', {'theme': theme})


def add_theme(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        cat_id = Category.objects.get(id=int(request.POST['cat']))
        themes = Themes(name=title, plan=text, category_theme=cat_id)
        themes.save()
        return redirect('theme_detail', id=themes.pk)
    else:
        categories = Category.objects.all()
        return render(request, 'add_theme.html', {'categories': categories})


def edit_theme(request, id):
    themes = Themes.objects.get(id=id)
    if request.method == 'POST':
        themes.name = request.POST['title']
        themes.plan = request.POST['text']
        themes.category_theme = Category.objects.get(id=int(request.POST['cat']))
        themes.save()
        return redirect('theme_detail', id=themes.pk)
    else:
        categories = Category.objects.all()
        return render(request, 'edit_theme.html', {'categories': categories, 'themes': themes})


def delete_theme(request, pk):
    themes = Themes.objects.get(id=pk)
    themes.delete()
    return redirect('themes_list')