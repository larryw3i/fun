import pytz
from django.utils import timezone

from fun.settings import TIME_ZONE


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.COOKIES.get('timezone', TIME_ZONE)
        if tzname and len(str(tzname)) < 20:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
