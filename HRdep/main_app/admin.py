from django.contrib import admin

# Register your models here.
from .models import Dep, Medical, Mission, Order, Stafflist, Statement, Vacation, Worker


admin.site.register(Dep)
admin.site.register(Medical)
admin.site.register(Mission)
admin.site.register(Order)
admin.site.register(Stafflist)
admin.site.register(Statement)
admin.site.register(Vacation)
admin.site.register(Worker)
