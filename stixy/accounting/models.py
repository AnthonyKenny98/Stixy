"""Models for Accounting App."""
from django.db import models


class _Accounting(models.Model):
    """Base Class."""

    class Meta:
        """Define Meta Attributes."""

        abstract = True

    def __str__(self):
        """String Representation of Class."""
        return self.name

    def __iter__(self):
        """Iterate through attributes of Class."""
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                yield self._meta.get_field(attr).verbose_name, value

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


class AccountClass(_Account):
    """Broad Account Classes - Intended for DAXLIC but can have others."""

    positive_entry = models.CharField("Positive Entry", max_length=200)

    class Meta:
        """Define Meta Attributes."""

        verbose_name = 'Account Class'
        verbose_name_plural = 'Account Classes'


class AccountGroup(_Account):
    """Broad Groups for Accounts."""

    account_class = models.ForeignKey(
        AccountClass,
        verbose_name=AccountClass.verbose_class_name,
        null=False,
        on_delete=models.CASCADE)

    class Meta:
        """Define Meta Attributes."""

        verbose_name = 'Account Group'
        verbose_name_plural = 'Account Groups'


class Account(_Account):
    """Account."""

    code = models.CharField("Account Code", max_length=6, unique=True)
    description = models.CharField("Description", max_length=512, null=True)
    account_group = models.ForeignKey(
        AccountGroup,
        verbose_name=AccountGroup.verbose_class_name,
        null=False,
        on_delete=models.CASCADE)

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

# class Transaction(_Accounting):
