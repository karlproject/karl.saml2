#from zope.interface import implementer
from zope.interface import implements

from karl.saml2.interfaces import IIdentityProvider


# WTF?  How can we bw using a version of zope.interface which doesn't support
# class decorators?
#@implementer(IIdentityProvider) 
class IdentityProvider(object):
    implements(IIdentityProvider)
