"""Admin Settings for Accounting App."""
from django.contrib import admin

# Register your models here.
from .models import AccountClass, AccountGroup, \
    Account, SubAccount, BankAccount, Transaction, Entry


class AccountClassAdmin(admin.ModelAdmin):
    """Admin settings for Account Class."""

    list_display = ['name', 'positive_entry']


class AccountGroupAdmin(admin.ModelAdmin):
    """Admin Settings for Account Group."""

    list_display = ['name', 'get_account_class']

    def get_account_class(self, obj):
        """Get name of associated account clas."""
        return obj.account_class.name


class AccountAdmin(admin.ModelAdmin):
    """Admin Settings for Account."""

    list_display = ['code', 'name', 'get_account_group']

    def get_account_group(self, obj):
        """Get name of associated account group."""
        return obj.account_group.name


class SubAccountAdmin(admin.ModelAdmin):
    """Admin Settings for SubAccount."""

    list_display = ['code', 'name']


class BankAccountAdmin(admin.ModelAdmin):
    """Admin Settings for Bank Account."""

    list_display = ['number', 'name']


class EntryInline(admin.TabularInline):
    """Inline class for entry."""

    model = Entry
    extra = 2


class TransactionAdmin(admin.ModelAdmin):
    """Admin settings for Transaction Class."""

    inlines = [EntryInline]


admin.site.register(AccountClass, AccountClassAdmin)
admin.site.register(AccountGroup, AccountGroupAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(SubAccount, SubAccountAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
