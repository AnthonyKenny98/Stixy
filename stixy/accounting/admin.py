"""Admin Settings for Accounting App."""
from django.contrib import admin
from django.forms.models import BaseInlineFormSet

# Register your models here.
from .models import AccountClass, AccountGroup, \
    Account, SubAccount, BankAccount, Transaction, Entry

from django.core.exceptions import ValidationError


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


class EntryInlineFormSet(BaseInlineFormSet):
    """."""

    def clean(self):
        """Clean."""
        super(EntryInlineFormSet, self).clean()
        debits, credits = 0, 0
        entries = 0
        for form in self.forms:
            if not form.is_valid():
                return  # other errors exist, so don't bother.
                # Shouldnt this do something other than return though?
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                debits += form.cleaned_data['debit']
                credits += form.cleaned_data['credit']
                entries += 1

                if debits != 0 or credits != 0:
                    raise ValidationError((
                        'One of credits or debits must be equal to 0.'))
        # DO TOTAL INLINES CHECK
        if entries < 2:
            raise ValidationError(
                ('Each transaction requires a minimum of 2 entries'))
        if debits != credits:
            raise ValidationError((
                'Transaction Debits and Credits must balance.'))
        if debits != self.instance.amount:
            raise ValidationError((
                'Transaction amount must equal total debits and credits.'))


class EntryInline(admin.TabularInline):
    """Inline class for entry."""

    model = Entry
    min_num = 2
    extra = 0
    formset = EntryInlineFormSet


class TransactionAdmin(admin.ModelAdmin):
    """Admin settings for Transaction Class."""

    list_display = ['id', 'date', 'description']

    inlines = [EntryInline]


admin.site.register(AccountClass, AccountClassAdmin)
admin.site.register(AccountGroup, AccountGroupAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(SubAccount, SubAccountAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Entry)
