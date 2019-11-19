
from django.urls import path, include
from .views import HomeView , change_language

urlpatterns = [
	path( '', HomeView.as_view(), name = '#' ),
	path('change_language', change_language , name='change_language'),
	path('i18n/', include('django.conf.urls.i18n')),
]