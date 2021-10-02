from django.contrib import admin
# Register your models here.
from django.utils.translation import gettext_lazy as _

from .models import Funuser


@admin.register(Funuser)
class HomestickerAdmin(admin.ModelAdmin):

    list_display = ('user', 'birth_date', 'address', 'occupation')
    list_per_page = 10
    ordering = ('-creating_date',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)
