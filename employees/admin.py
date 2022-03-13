from django.contrib import admin

from employees.models import Employee

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    search_fields = ('name', 'email', 'department')

admin.site.register(Employee, EmployeeModelAdmin)
