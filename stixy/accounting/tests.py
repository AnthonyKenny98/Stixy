"""Test Cases for Accounting App."""
from django.test import TestCase

from .models import AccountClass, AccountGroup


# Init Test Instances
asset = AccountClass(name='asset', positive_entry='debit')
current_asset = AccountGroup(name='current asset', account_class=asset)

class AccountClassTests(TestCase):
    """Test AccountClass Model."""

    def test_name(self):
        self.assertEqual(asset.name, 'asset')

    def test_positive_entry(self):
        self.assertEqual(asset.positive_entry, 'debit')


class AssetGroupModelTests(TestCase):
    """Test AssetGroup Model."""

    def test_name(self):
        self.assertEqual(current_asset.name, 'current asset')
