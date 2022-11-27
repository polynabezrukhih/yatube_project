from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text
    }
    return render(request, template)


def group_posts(request):
    template = 'posts/group_list.html'
    template = 'posts/index.html'
    title = 'Лев Толстой – зеркало русской революции.'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text
    }
    return render(request, template)


def group_posts_number(request, slug):
     return HttpResponse(f' Группа № {slug}')

