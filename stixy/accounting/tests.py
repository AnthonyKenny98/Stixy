"""Test Cases for Accounting App."""
# flake8: noqa
from django.test import TestCase, Client

from .models import AccountClass, AccountGroup


# Init Test Instances
asset = AccountClass(name='asset', positive_entry='debit')
current_asset = AccountGroup(name='current asset', account_class=asset)

class AccountClassTests(TestCase):
    """Test AccountClass Model."""

    def test_has_attrs(self):
        self.assertTrue(hasattr(asset, 'name'))
        self.assertTrue(hasattr(asset, 'positive_entry'))

    def test_meta(self):
        self.assertEqual(asset._meta.verbose_name, 'Account Class')
        self.assertEqual(asset._meta.verbose_name_plural, 'Account Classes')

class AccountGroupModelTests(TestCase):
    """Test AssetGroup Model."""

    def test_has_attrs(self):
        self.assertTrue(hasattr(current_asset, 'name'))
        self.assertTrue(hasattr(current_asset, 'account_class'))
        self.assertTrue(hasattr(current_asset.account_class, 'name'))
        self.assertTrue(hasattr(current_asset.account_class, 'positive_entry'))


class AccountingSuperModelTests(TestCase):

    def test_verbose(self):
        self.assertEqual(asset.class_name(), asset.__class__.__name__)
        self.assertEqual(asset.verbose_class_name(), asset.__class__._meta.verbose_name)
        self.assertEqual(asset.verbose_class_name_plural(), asset.__class__._meta.verbose_name_plural)

class ClientTests(TestCase):


    def test_testy(self):
        c = Client()
        response = c.get('AccountClass')