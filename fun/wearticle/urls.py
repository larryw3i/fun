
from django.urls import path
from wearticle import views
from wearticle.views import HelloView, MonthConverter
from django.urls import register_converter

register_converter( MonthConverter, 'mth' )



urlpatterns = [
	path( 'hello/', views.hello_django_bbs ),
	path( '_hello/', HelloView.as_view() ),
	path( 'dynamic/<str:year>/<mth:month>/<int:day>', HelloView.dynamic_hello  ),
	path( 'dynamic/<str:year>/<mth:month>/', HelloView.dynamic_hello ),
	# path( 'index/', views.IndexView.as_view() ),
]
