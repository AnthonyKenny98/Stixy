"""Models for Accounting App."""
from django.db import models


class Accounting(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        """Define Meta Attributes."""

        abstract = True

    def __str__(self):
        """String Representation of Class."""
        return self.name

    def __iter__(self):
        """Iterate through attributes of Class."""
        for attr, value in self.__dict__.iteritems():
            if "__" not in attr:
                yield attr, value

    def get_cname(self):
        return self.__class__.__name__


class AccountClass(Accounting):
    """Broad Account Classes - Intended for DAXLIC but can have others."""

    positive_entry = models.CharField("Positive Entry", max_length=200)

    class Meta:
        """Define Meta Attributes."""

        verbose_name_plural = 'Account Classes'

    def is_asset(self):
        """Return True if self.name is "Asset"."""
        return self.name == 'Asset'


class AccountGroup(Accounting):
    """Broad Groups for Accounts."""

    class Meta:
        """Define Meta Attributes."""

        verbose_name_plural = 'Account Groups'

    account_class = models.ForeignKey(
        AccountClass,
        null=True,
        on_delete=models.SET_NULL)
