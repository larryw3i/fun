
from django.urls import path
from wearticle import views
from wearticle.views import HelloView

urlpatterns = [
	path( 'hello/', views.hello_django_bbs ),
	path( '_hello/', HelloView.as_view() ),
]
