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
	return HttpResponse("Here you'll find character %s info." % character_id)

def characters(request):
	return HttpResponse("All characters.")

def items(request):
	items = Item.objects.all()
	return render(request, 'inventory/items.html', {'items': items})
