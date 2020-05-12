"""Test Cases for Accounting App."""
from django.test import TestCase

from .models import AccountClass, AccountGroup


class AssetClassModelTests(TestCase):
    """Test AssetClass Model."""

    def test_is_asset(self):
        """is_asset() returns true if assetclass is "asset"."""
        a = AccountClass(name='Asset', positive_entry='debit')
        self.assertIs(a.is_asset(), True)


class AssetGroupModelTests(TestCase):
    """Test AssetGroup Model."""

    def test_asset_is_debit(self):
        g = AccountGroup(
            name='Current Assets',
            account_class=AccountClass(
                name='Asset',
                positive_entry='debit'))
        self.assertIs(g.account_class.positive_entry, 'debit')
