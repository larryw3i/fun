
from django.core.exceptions import ValidationError
import magic
from django.utils.translation import ugettext as _
from hurry import filesize

video_max_size = 100*pow(1024,2)
pdf_document_max_size = 5*pow(1024,2)

size_whit_mimetypes = {
        'video/*':video_max_size,
        'application/pdf':pdf_document_max_size,
    }

def MediaFileValidator(value):
        try:
            content_type = value.file.content_type
            content_type = 'video/*' if content_type.startswith('video/') else content_type

            if content_type in size_whit_mimetypes.keys():
                if  value.file.size > size_whit_mimetypes[content_type]:
                    raise ValidationError(_('File size must be less than %s') % ( filesize.size(size_whit_mimetypes[content_type]) ), code='file-size')
            else:
                raise ValidationError(_('%s is not an acceptable file type') % content_type, code='file-type')

        except AttributeError as e:
            raise ValidationError('This %s could not be validated for file type' % value.file.name, code='file-type')

        

