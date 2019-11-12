
import hashlib
import os

from django.core.files.storage import FileSystemStorage

from fun import settings


def upload_to(
    instance, 
    filename):
    return  os.path.join( settings.MEDIA_ROOT , filename )

class FunFileStorage(FileSystemStorage):
    def _save(self, name, content):
        sha256 = hashlib.sha256()
        for chunk in content.chunks():
            sha256.update(chunk)
        name =  sha256.hexdigest() 

        full_path = super().path(name)

        if( os.path.exists( full_path )):
            return name

        return super()._save(name, content)
