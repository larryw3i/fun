
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='#'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('homesticker_detail/<uuid:pk>',
         views.HomestickerDetailView.as_view(), name='homesticker_detail'),
    path('homesticker_list', views.HomestickerListView.as_view(),
         name='homesticker_list'),

    path('funhomesticker_detail/<uuid:pk>',
         views.FunhomestickerDetailView.as_view(),
         name='funhomesticker_detail'),
    path('funhomesticker_list', views.FunhomestickerListView.as_view(),
         name='funhomesticker_list'),

    path('data_privacy', views.data_privacy, name='data_privacy'),
    path('legal_information', views.legal_information,
         name='legal_information'),

    path('favicon.ico', views.get_favicon_ico,  name='favicon.ico'),
]
