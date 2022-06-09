
from tabnanny import verbose
from attr import field
from django.contrib import admin
from django.forms.models import BaseInlineFormSet, ModelForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['pesel', 'first_name', 'last_name', 'birth_date', 'gender']


class AddressInline(admin.TabularInline):
    model = Address
    verbose_name_plural = 'adresses'
    extra = 1

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (AddressInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)