# -*- coding: utf-8 -*-
from collective.todo import _
from Products.Five.browser import BrowserView
from operator import itemgetter


class DemoView(BrowserView):
    """A demo listing"""

    def title(self):
        return _(u'A list of talks:')

    def for_macros(self):
        return _(u'I can be reused')
