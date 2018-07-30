# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

user_choice = [('librarian','Librarian'),('student','Student')]
class user(models.Model):
	name=models.CharField(max_length=50)
	dob=models.CharField(max_length=50,default='11/11/1997')
	gender=models.CharField(max_length=50,default='Male')
	rollno=models.CharField(max_length=50,default='0000')
	dept=models.CharField(max_length=50,default='EnTC')
	username=models.CharField(max_length=50,blank=False)
	password=models.CharField(max_length=50,blank=False)
	contact=models.CharField(max_length=50)
	user_type=models.CharField(max_length=50, choices=user_choice, default='librarian')

	def __str__(self):
		return self.name
class books(models.Model):
	name=models.CharField(max_length=50)
	author=models.CharField(max_length=50)
	genre=models.CharField(max_length=50)
	summary=models.CharField(max_length=200,default='Summary')
	def __str__(self):
		return self.name


# Create your models here.
