from django.contrib import admin

# Register your models here.
from .models import *


class AccountClassAdmin(admin.ModelAdmin):
    fields = ['name', 'positive_entry']


admin.site.register(AccountClass, AccountClassAdmin)

admin.site.register(AccountGroup)

admin.site.register(Account)

admin.site.register(SubAccount)

admin.site.register(BankAccount)