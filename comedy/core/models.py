from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


CITIES_CHOICES = (
	('DL', 'Delhi'),
	('MB', 'Mumbai'),
	('KL', 'Kolkata'),
	('GU', 'Guwahati'),
	('CH', 'Chennai'),
	('PB', 'Punjab'),
	('KA', 'Kanpur'),
	('BA', 'Bangalore'),
	('OD', 'Odisha'),
	)

class Comedian(models.Model):
	name = models.CharField(max_length=200)
	bio = models.CharField(max_length=1000, blank=True)
	tagLine = models.CharField(max_length=1000, blank=True)
	imgUrl = models.URLField(max_length=1000, blank=True)
	cityOfOrigin = models.CharField(max_length=50)
	youtubeUrl = models.URLField(max_length=1000)
	linkedinUrl = models.URLField(max_length=1000, blank=True)
	websiteUrl = models.URLField(max_length=1000, blank=True)

	def __str__(self):
		return f'{self.name}'

class Show(models.Model):



	comedian = models.ForeignKey(Comedian, on_delete = models.CASCADE)
	imgUrl = models.URLField(max_length=1000, blank=True)
	city = models.CharField(max_length=100, default="Delhi")
	venue = models.CharField(max_length=100)
	date = models.DateField(auto_now=False, auto_now_add=False)
	startTime = models.TimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return f'{self.comedian}-({self.city}) Show'

class Person(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='person')
	isCritic = models.BooleanField(default=True)
    

class Review(models.Model):
	user = models.ForeignKey(Person, on_delete=models.CASCADE)
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)],null=True)
	comment = models.CharField(max_length=2000)




