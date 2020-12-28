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

def create_character(request):
	if request.method == 'GET':
		currentUser = request.user
		character_name = request.GET.get('name')
		character_level = request.GET.get('level')
		character = Character.objects.create(name=character_name, level=character_level, user=currentUser)

	return redirect('/')

def character_details(request, character_id):
	character = Character.objects.get(pk=character_id)
	items = Item.objects.filter(characters__id=character_id)
	other_items = Item.objects.exclude(characters__id=character_id)
	return render(request, 'inventory/character.html', {'character': character, 'items': items, 'other_items': other_items})

def items(request):
	items = Item.objects.all()
	return render(request, 'inventory/items.html', {'items': items})

def add_item(request):
	if request.method == 'GET':
		item_name = request.GET.get('name')
		item_armor_level = request.GET.get('armor_level')
		item = Item.objects.create(name=item_name, armor_level=item_armor_level)

	return redirect('/items/')

def add_to_character(request):
	if request.method == 'GET':
		character = Character.objects.get(pk=request.GET.get('character_id'))
		item = request.GET.get('item')
		i = Item.objects.get(name=item)
		i.characters.add(character)

	return redirect('/characters/%s' % character.id)

