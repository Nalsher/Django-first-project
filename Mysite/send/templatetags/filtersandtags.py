import datetime
import time

from django import template
from django.template.defaultfilters import stringfilter
from datetime import *


register = template.Library()


@register.simple_tag(name='cur')
def currency():
    return datetime.now()


@register.inclusion_tag('tags/ulist.html')
def ulist(*args):
    return {'items':args}
