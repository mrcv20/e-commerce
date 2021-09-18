from django.template import Library
from utils import utils

register = Library()

@register.filter
def price_format(val):
    return utils.price_format(val)