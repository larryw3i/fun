
from django.urls import path, include
from .views import HomeView , HomestickerDetailView, HomestickerListView, FunhomestickerListView, FunhomestickerDetailView

urlpatterns = [
	path( '', HomeView.as_view(), name = '#' ),
	path('i18n/', include('django.conf.urls.i18n')),
	path( 'homesticker_detail/<uuid:pk>', HomestickerDetailView.as_view(), name = 'homesticker_detail' ),
	path( 'homesticker_list', HomestickerListView.as_view(), name = 'homesticker_list' ),
	path( 'funhomesticker_detail/<uuid:pk>', FunhomestickerDetailView.as_view(), name = 'funhomesticker_detail' ),
	path( 'funhomesticker_list', FunhomestickerListView.as_view(), name = 'funhomesticker_list' ),
]