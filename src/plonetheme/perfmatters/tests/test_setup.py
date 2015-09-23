# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.perfmatters.testing import PLONETHEME_PERFMATTERS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.perfmatters is properly installed."""

    layer = PLONETHEME_PERFMATTERS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.perfmatters is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('plonetheme.perfmatters'))

    def test_browserlayer(self):
        """Test that IPlonethemePerfmattersLayer is registered."""
        from plonetheme.perfmatters.interfaces import IPlonethemePerfmattersLayer
        from plone.browserlayer import utils
        self.assertIn(IPlonethemePerfmattersLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_PERFMATTERS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.perfmatters'])

    def test_product_uninstalled(self):
        """Test if plonetheme.perfmatters is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('plonetheme.perfmatters'))
