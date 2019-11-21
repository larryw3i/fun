
from django.urls import path, include
from .views import HomeView , HomestickerDetailView, HomestickerListView

urlpatterns = [
	path( '', HomeView.as_view(), name = '#' ),
	path('i18n/', include('django.conf.urls.i18n')),
	path( 'homesticker_detail/<uuid:pk>', HomestickerDetailView.as_view(), name = 'homesticker_detail' ),
	path( 'homesticker_list', HomestickerListView.as_view(), name = 'homesticker_list' ),
]