# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from operator import itemgetter
from collective.todo import _


class DemoView(BrowserView):
    """A demo listing"""

    def title(self):
        return _(u'A list of talks:')

    def for_macros(self):
        return _(u'I can be reused')

    def talks(self):
        results = []
        data = [
            {'title': _('Dexterity is the new default!'),
             'subjects': ('content-types', 'dexterity')},
            {'title': _('Mosaic will be the next big thing.'),
             'subjects': ('layout', 'deco', 'views'),
             'url': 'https://www.youtube.com/watch?v=QSNufxaYb1M'},
            {'title': _('The State of Plone'),
             'subjects': ('keynote',)},
            {'title': _('Diazo is a powerful tool for theming!'),
             'subjects': ('design', 'diazo', 'xslt')},
            {'title': _('Magic templates in Plone 5'),
             'subjects': ('templates', 'TAL'),
             'url': 'http://www.starzel.de/blog/magic-templates-in-plone-5'},
        ]
        for item in data:
            try:
                url = item['url']
            except KeyError:
                url = 'https://www.google.com/search?q=%s' % item['title']
            talk = dict(
                title=item['title'],
                subjects=', '.join(item['subjects']),
                url=url
            )
            results.append(talk)
        return sorted(results, key=itemgetter('title'))
