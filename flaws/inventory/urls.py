from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('create_character/', views.create_character, name='create_character'),
	path('characters/<int:character_id>/', views.character_details, name='character_details'),
	path('items/', views.items, name='items'),
	path('add_item/', views.add_item, name='add_item'),
	path('add_to_character/', views.add_to_character, name='add_to_character'),
]
