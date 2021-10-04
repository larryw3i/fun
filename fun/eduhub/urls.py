
from django.urls import path

from fun import default_uuid

from . import views
from .apps import EduhubConfig

app_name = EduhubConfig.name
urlpatterns = [
    path('label_list', views.LabelListView.as_view(), name='label_list'),
    path('label_create/', views.LabelCreateView.as_view(),
         name='label_create'),
    path('label_delete/<uuid:pk>',
         views.LabelDeleteView.as_view(), name='label_delete'),
    path('label_update/<uuid:pk>',
         views.LabelUpdateView.as_view(), name='label_update'),

    path('home', views.EduhubhomestickerListView.as_view(), name='home'),
    path('eduhubhomesticker_detail/<uuid:pk>',
         views.EduhubhomestickerDetailView.as_view(),
         name='eduhubhomesticker_detail'),
    path('eduhub_search/', views.EduhubSearch.as_view(),
         name='eduhub_search'),

    path('funcontent_list/', views.FuncontentListView.as_view(),
         name='funcontent_list_all'),
    path('funcontent_list/<uuid:label>',
         views.FuncontentListView.as_view(), name='funcontent_list'),
    path('funcontent_create/<uuid:label>',
         views.FuncontentCreateView.as_view(), name='funcontent_create'),
    path('funcontent_detail/<uuid:pk>',
         views.FuncontentDetailView.as_view(), name='funcontent_detail'),
    path('funcontent_delete/<uuid:pk>',
         views.FuncontentDeleteView.as_view(), name='funcontent_delete'),
    path('funcontent_update/<uuid:pk>',
         views.FuncontentUpdateView.as_view(), name='funcontent_update'),


    path('funtest_create/', views.FuntestCreateView.as_view(),
         name='funtest_create'),

    path('funtest_content_preview/', views.FuntestContentPreview.as_view(),
         name='funtest_content_preview'),

    path('how_to_classification', views.how_to_classification,
         name='how_to_classification'),
]
