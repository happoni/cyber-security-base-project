from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('characters/<int:character_id>/', views.character_details, name='character_details'),
	path('items/', views.items, name='items'),
]
