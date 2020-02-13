
# COMMON

import bleach
from fun import settings


def default_bleach_clean(content):
    return bleach.clean(
        content,
        tags=settings.BLEACH_TAGS,
        attributes=settings.BLEACH_ATTRIBUTES,
        styles=settings.BLEACH_STYLES)
