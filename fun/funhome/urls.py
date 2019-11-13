
from django.urls import path
from .views import HomeView , get_all_bootswatch_themes, get_dropdown_items

urlpatterns = [
	path( '', HomeView.as_view(), name = '#' ),
	path( 'get_all_bootswatch_themes', get_all_bootswatch_themes, name = 'get_all_bootswatch_themes'),
	path( 'get_dropdown_items', get_dropdown_items, name = 'get_dropdown_items'),
]