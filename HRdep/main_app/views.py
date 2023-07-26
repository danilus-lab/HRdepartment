from django.shortcuts import render
from .models import Worker, Dep, Stafflist


def index(request):
    return render(request, "main_app/index.html")


def dismiss(request):
    return render(request, "main_app/dismiss.html")


def workers(request):
    workers = Worker.objects.all()
    return render(request, "main_app/workers.html", {'title': 'Список сотрудников', 'workers': workers})


def staff_list(request):
    notes = Stafflist.objects.all()
    return render(request, "main_app/staff_list.html", {'title': 'Штатное расписание', 'notes': notes})
