from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Character, Item

@login_required
def index(request):
	characters = Character.objects.filter(user = request.user)
	latest_added_item = Item.objects.last()
	return render(request, 'inventory/index.html', {'characters': characters, 'latest_item': latest_added_item})

def character_details(request, character_id):
	character = Character.objects.get(pk=character_id)
	items = Item.objects.filter(characters__id=character_id)
	return render(request, 'inventory/character.html', {'character': character, 'items': items})

def items(request):
	items = Item.objects.all()
	return render(request, 'inventory/items.html', {'items': items})

def add_item(request):
	if request.method == 'POST':
		item_name = request.POST.get('name')
		item_armor_level = request.POST.get('armor_level')
		item = Item.objects.create(name=item_name, armor_level=item_armor_level)

	return redirect('/items/')