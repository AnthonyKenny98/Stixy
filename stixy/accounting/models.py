"""Models for Accounting App."""
from django.db import models


def defaultforeignkey(model, null=False, related_name=None):
    """
    Default foreign key function.

    This is just to save some lines of code and keep things simple.
    Null attribute can be overridden but defaults to False.
    """
    return models.ForeignKey(
        model,
        verbose_name=model().verbose_class_name(),
        related_name=related_name,
        null=False,
        on_delete=models.PROTECT)


class _Accounting(models.Model):
    """Base Class."""

    class Meta:
        """Define Meta Attributes."""

        abstract = True

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name, getattr(self, field.name)

    def class_name(self):
        """Return name of class."""
        return self.__class__.__name__

    def verbose_class_name(self):
        """Return verbose name of class."""
        return self.__class__._meta.verbose_name

    def verbose_class_name_plural(self):
        return self.__class__._meta.verbose_name_plural


class _Account(_Accounting):
    """Account Base Class."""

    name = models.CharField("Name", max_length=200)

    class Meta:
        """Define Meta Attributes."""

        abstract = True

    def __str__(self):
        """String Representation of Class."""
        return self.name


class AccountClass(_Account):
    """Broad Account Classes - Intended for DAXLIC but can have others."""

    positive_entry = models.CharField("Positive Entry", max_length=200)

    class Meta:
        """Define Meta Attributes."""

        verbose_name = 'Account Class'
        verbose_name_plural = 'Account Classes'


class AccountGroup(_Account):
    """Broad Groups for Accounts."""

    account_class = defaultforeignkey(AccountClass)

    class Meta:
        """Define Meta Attributes."""

        verbose_name = 'Account Group'
        verbose_name_plural = 'Account Groups'


class Account(_Account):
    """Account."""

    code = models.CharField("Account Code", max_length=6, unique=True)
    description = models.CharField("Description", max_length=512, null=True)
    account_group = defaultforeignkey(AccountGroup)

    class Meta:
        """Define Meta Attributes."""

        verbose_name = "Account"
        verbose_name_plural = "Accounts"


class SubAccount(_Account):
    """Sub Account."""

    code = models.CharField("Code", max_length=4, unique=True)
    description = models.CharField("Description", max_length=512, null=True)

    class Meta:
        """Define Meta Attributes."""

        verbose_name = "Sub-Account"
        verbose_name_plural = "Sub-Accounts"


class BankAccount(_Account):
    """Bank Account."""

    number = models.PositiveIntegerField("Bank Account Number", unique=True)

    class Meta:
        """Define Meta Attributes."""

        verbose_name = "Bank Account"
        verbose_name_plural = "Bank Accounts"


class Transaction(_Accounting):
    """A double entry transaction."""

    date = models.DateField("Transaction Date")
    description = models.TextField("Transaction Description")

    class Meta:
        """Define Meta Attributes."""

        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"


class Entry(_Accounting):
    """A Single Accounting Entry."""

    account = defaultforeignkey(Account)

    sub_account = defaultforeignkey(SubAccount)

    debit = models.FloatField("Debit Amount")
    credit = models.FloatField("Credit Amount")

    transaction = defaultforeignkey(
        Transaction,
        related_name='entries')

    class Meta:
        """Define Meta Attributes."""

        verbose_name = "Entry"
        verbose_name_plural = "Entries"
