from django.contrib import admin

# Register your models here.
from django.utils.translation import gettext_lazy as _

from .modelforms import FunuserModelForm
from .models import Funuser


@admin.register( Funuser )
class HomestickerAdmin(admin.ModelAdmin):
    
    list_display = ( 'user',  'birth_date', 'address', 'occupation' )
    list_per_page = 10
    ordering = ('-creating_date',)
    fieldsets = (
        ( _("avatar"), {'fields': ['avatar', ]}),
        ( _('Birth date'),  {'fields':['birth_date',    'is_birth_date_outward']}),
        ( _('Address'),     {'fields':['address',       'is_Address_outward']}),
        ( _('Hometown'),    {'fields':['hometown',      'is_hometown_date_outward']}),
        ( _('College'),     {'fields':['college',       'is_college_outward']}),
        ( _('Occupation'),  {'fields':['occupation',    'is_occupation_outward']}),
        ( _('Hobby'),       {'fields':['hobby',         'is_hobby_outward']}),
        ( _('Motto'),       {'fields':['motto',         'is_motto_outward']}), 
    )
 

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)