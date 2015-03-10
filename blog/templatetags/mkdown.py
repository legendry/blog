# -*- coding: utf-8 -*-

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='mkdown')
@stringfilter
def mkkdown(value):
    print 111
    return mark_safe(markdown.markdown(force_unicode(value), extras=["code-friendly"]))