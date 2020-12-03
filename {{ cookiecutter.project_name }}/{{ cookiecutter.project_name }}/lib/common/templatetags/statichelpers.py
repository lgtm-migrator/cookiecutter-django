from django.template import Library
from django.contrib.staticfiles.storage import staticfiles_storage

register = Library()


@register.simple_tag
def static_path(path):
    """

    Args:
      path:

    Returns:

    """
    return staticfiles_storage.url(path)
