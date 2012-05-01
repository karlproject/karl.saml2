import unittest

class IdentityProviderTests(unittest.TestCase):

    def _getTargetClass(self):
        from karl.saml2.identity import IdentityProvider
        return IdentityProvider

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_class_conforms_to_IIdentityProvider(self):
        from zope.interface.verify import verifyClass
        from karl.saml2.interfaces import IIdentityProvider
        verifyClass(IIdentityProvider, self._getTargetClass())

    def test_instance_conforms_to_IIdentityProvider(self):
        from zope.interface.verify import verifyObject
        from karl.saml2.interfaces import IIdentityProvider
        verifyObject(IIdentityProvider, self._makeOne())
