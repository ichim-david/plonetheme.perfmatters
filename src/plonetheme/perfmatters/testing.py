# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.perfmatters


class PlonethemePerfmattersLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plonetheme.perfmatters)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.perfmatters:default')


PLONETHEME_PERFMATTERS_FIXTURE = PlonethemePerfmattersLayer()


PLONETHEME_PERFMATTERS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_PERFMATTERS_FIXTURE,),
    name='PlonethemePerfmattersLayer:IntegrationTesting'
)


PLONETHEME_PERFMATTERS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_PERFMATTERS_FIXTURE,),
    name='PlonethemePerfmattersLayer:FunctionalTesting'
)


PLONETHEME_PERFMATTERS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_PERFMATTERS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemePerfmattersLayer:AcceptanceTesting'
)
