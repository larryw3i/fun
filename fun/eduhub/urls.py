
from django.urls import path
from . import views
from .apps import EduhubConfig

app_name = EduhubConfig.name
urlpatterns = [
    path('label_list/', views.LabelListView.as_view(), name = 'label_list'),
    path('label_create/', views.LabelCreateView.as_view(), name = 'label_create'),
    path('label_delete/<uuid:pk>', views.LabelDeleteView.as_view(), name = 'label_delete'),
    path('label_update/<uuid:pk>', views.LabelUpdateView.as_view(), name = 'label_update'),

    path('content_list/<uuid:label>', views.ContentListView.as_view(), name = 'content_list'),
    path('content_create/<uuid:label>', views.ContentCreateView.as_view(), name = 'content_create'),
    path('content_detail/<uuid:pk>', views.ContentDetailView.as_view(), name = 'content_detail'),
    path('content_delete/<uuid:pk>', views.ContentDeleteView.as_view(), name = 'content_delete'),
]