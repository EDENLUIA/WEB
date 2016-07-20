from __future__ import unicode_literals

from django.db import models

class SignUp(models.Model):
	email = models.EmailField()	
	fullname = models.CharField(max_length=120,blank=True, null=True)	
	timestamp = models.DateTimeField(auto_now_add= True, auto_now= False)
	updated = models.DateTimeField(auto_now_add =False, auto_now =True)

	def __unicode__(self): #python 3.3 es __str__
		return self.email

# Create your models here.
