from django.contrib import admin
# Register your models here.
from django.utils.translation import gettext_lazy as _

from .models import Funuser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(Funuser)
class FunuserAdmin(UserAdmin):
    pass
