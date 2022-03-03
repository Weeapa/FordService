from django.contrib import admin
from team.models import Worker

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "contact_phone")
