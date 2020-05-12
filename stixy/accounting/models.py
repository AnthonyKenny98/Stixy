"""Models for Accounting App."""
from django.db import models


class _Accounting(models.Model):
    """Base Class."""
    name = models.CharField(max_length=200)

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
                yield attr, value

    def class_name(self):
        """Return name of class."""
        return self.__class__.__name__


class AccountClass(_Accounting):
    """Broad Account Classes - Intended for DAXLIC but can have others."""

    positive_entry = models.CharField("Positive Entry", max_length=200)

    class Meta:
        """Define Meta Attributes."""

        verbose_name_plural = 'Account Classes'

    def is_asset(self):
        """Return True if self.name is "Asset"."""
        return self.name == 'Asset'


class AccountGroup(_Accounting):
    """Broad Groups for Accounts."""

    class Meta:
        """Define Meta Attributes."""

        verbose_name_plural = 'Account Groups'

    account_class = models.ForeignKey(
        AccountClass,
        null=False,
        on_delete=models.CASCADE)


class Account(_Accounting):
    """Account."""

    code = models.CharField(max_length=6, unique=True)
    description = models.CharField(max_length=512, null=True)
    account_group = models.ForeignKey(
        AccountGroup,
        null=False,
        on_delete=models.CASCADE)


class SubAccount(_Accounting):
    """Sub Account."""

    code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=512, null=True)
