from django.shortcuts import render
from .models import Worker


def index(request):
    return render(request, "main_app/index.html")


def dismiss(request):
    return render(request, "main_app/dismiss.html")


def workers(request):
    workers = Worker.objects.all()
    return render(request, "main_app/workers.html", {'title': 'Список сотрудников', 'workers': workers})
