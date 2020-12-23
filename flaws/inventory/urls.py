from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('characters/<int:character_id>/', views.character_details, name='character_details'),
	path('items/<int:item_id>/', views.item_details, name='item_details'),
	path('characters/', views.characters, name='characters'),
	path('items/', views.items, name='items'),
]
