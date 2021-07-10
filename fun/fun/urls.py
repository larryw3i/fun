"""fun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from fun import settings
from django.views.static import serve as serve_static  

urlpatterns = [

    path('', include('funhome.urls')),

    path('admin/', admin.site.urls),

    path('funfile/', include('funfile.urls')),
    
    path('eduhub/', include('eduhub.urls')),

    path('funuser/', include('funuser.urls')),

    path('ckeditor/', include('fun._ckeditor_uploader_url')),

    # path('django_bfm/', include('django_bfm.urls')),

    path(r'static/<path:path>', serve_static, \
        {'document_root': settings.SERVE_STATIC_ROOT },),

]   #+ static( settings.STATIC_URL, document_root =  settings.STATIC_ROOT  )

if settings.app_env["switch"]["allow_registration"]:
    urlpatterns += [ path('accounts/', include('allauth.urls')) ]