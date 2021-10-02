from django.shortcuts import render

# Create your views here.

import os
from fun import settings
from django.http import FileResponse, Http404

from funfile.models import Checkup

import magic


def get_file(request, file_id):
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_id))

    if os.path.exists(file_path):
        content_type = magic.from_file(file_path, mime=True)
        return FileResponse(open(file_path, 'rb'), content_type=content_type)
    else:
        raise Http404()
