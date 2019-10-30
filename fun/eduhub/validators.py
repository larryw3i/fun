
from django.core.exceptions import ValidationError
import magic
from django.utils.translation import ugettext as _
from hurry import filesize

video_max_size = 100*pow(1024,2)
pdf_document_max_size= 5*pow(1024,2)
size_whit_mimetypes = {
        'mp4':video_max_size,
        'mkv':video_max_size,
        'webm':video_max_size,
        'mov':video_max_size,
        'pdf':pdf_document_max_size,
    }

def MediaFileValidator(value):
        try:

            extension =str(value.file.name).rsplit('.',1)[1]
            if extension in size_whit_mimetypes.keys():
                if  value.file.size > size_whit_mimetypes[extension]:
                    raise ValidationError(_('File size must be less than %s') % ( filesize.size(size_whit_mimetypes[extension]) ), code='file-size')
            else:
                raise ValidationError(_('%s is not an acceptable file type') % extension, code='file-type')

        except AttributeError as e:
            raise ValidationError('This %s could not be validated for file type' % value, code='file-type')

        

