from django.contrib import admin
from .models import Country, Province, Area, City


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
