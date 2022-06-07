
from attr import field
from django.contrib import admin
from django.forms.models import BaseInlineFormSet, ModelForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Employee,Person

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['pesel', 'first_name', 'last_name', 'birth_date', 'gender']


class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    fk_name = 'person'


class EmployeeInline(admin.options.InlineModelAdmin):
    model = Employee
    fk_name = 'user'
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)