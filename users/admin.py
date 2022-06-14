
from tabnanny import verbose
from attr import field
from django.contrib import admin
from django.forms.models import BaseInlineFormSet, ModelForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import *
from services.models import Contract

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['pesel', 'first_name', 'last_name', 'birth_date', 'gender']


class AddressInline(admin.TabularInline):
    model = Address
    verbose_name_plural = 'adresses'
    extra = 0

class TelephonesInline(admin.TabularInline):
    model = Telephone
    extra = 0

class ContractInline(admin.StackedInline):
    model = Contract
    extra = 0

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'person'
    fk_name = 'client'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

class ClientAdmin(admin.ModelAdmin):
    inlines = (PersonInline, ContractInline)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (AddressInline,TelephonesInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Employee)
admin.site.register(Client,ClientAdmin)
admin.site.register(Telephone)
admin.site.register(Address)