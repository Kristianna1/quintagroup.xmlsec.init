"""Initialize xmlsec bindings."""

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('qg.xmlsec.binding.init')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    from dm.xmlsec.binding import initialize; initialize()
