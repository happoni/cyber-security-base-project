from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
	name = models.CharField(max_length=200)
	level = models.IntegerField(default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=200)
	armor_level = models.IntegerField(default=0)
	characters = models.ManyToManyField(Character, blank=True)

	def __str__(self):
		return self.name

	def rarityLevel(self):
		return self.rarity
