"""Admin Settings for Accounting App."""
from django.contrib import admin

# Register your models here.
from .models import AccountClass, AccountGroup, \
    Account, SubAccount, BankAccount


class AccountClassAdmin(admin.ModelAdmin):
    """Admin settings for Account Class."""

    fields = ['name', 'positive_entry']


admin.site.register(AccountClass, AccountClassAdmin)

admin.site.register(AccountGroup)

admin.site.register(Account)

admin.site.register(SubAccount)

admin.site.register(BankAccount)
