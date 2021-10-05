
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


    path('funcontent_list', views.FuncontentListView.as_view(),
         name='funcontent_list_all'),
    path('funcontent_list/<uuid:label_id>',
         views.FuncontentListView.as_view(), name='funcontent_list'),
    path('funcontent_create/<uuid:label_id>',
         views.FuncontentCreateView.as_view(), name='funcontent_create'),
    path('funcontent_detail/<uuid:pk>',
         views.FuncontentDetailView.as_view(), name='funcontent_detail'),
    path('funcontent_delete/<uuid:pk>',
         views.FuncontentDeleteView.as_view(), name='funcontent_delete'),
    path('funcontent_update/<uuid:pk>',
         views.FuncontentUpdateView.as_view(), name='funcontent_update'),


    path('appraising_list',
         views.AppraisingListView.as_view(), name='appraising_list'),
    path('appraising_create/<uuid:appraising_c_id>',
         views.AppraisingCreateView.as_view(), name='appraising_create'),
    path('appraising_detail/<uuid:pk>',
         views.AppraisingDetailView.as_view(), name='appraising_detail'),
    path('appraising_delete/<uuid:pk>',
         views.AppraisingDeleteView.as_view(), name='appraising_delete'),
    path('appraising_update/<uuid:pk>',
         views.AppraisingUpdateView.as_view(), name='appraising_update'),

    path('appraising_c_list',
         views.ASharingCListView.as_view(), name='appraising_c_list'),
    path('appraising_c_create',
         views.ASharingCCreateView.as_view(), name='appraising_c_create'),
    path('appraising_c_detail/<uuid:pk>',
         views.ASharingCDetailView.as_view(), name='appraising_c_detail'),
    path('appraising_c_delete/<uuid:pk>',
         views.ASharingCDeleteView.as_view(), name='appraising_c_delete'),
    path('appraising_c_update/<uuid:pk>',
         views.ASharingCUpdateView.as_view(), name='appraising_c_update'),


    path('funtest_create/', views.FuntestCreateView.as_view(),
         name='funtest_create'),

    path('funtest_content_preview/', views.FuntestContentPreview.as_view(),
         name='funtest_content_preview'),

    path('how_to_classification', views.how_to_classification,
         name='how_to_classification'),
]
