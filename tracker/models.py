from django.db import models
from django.utils import timezone

# Create your models here.
class Rejectable(models.Model):
	what = models.CharField(max_length=200,primary_key=True)
	toWhom = models.CharField(max_length=200)
	accepted = models.BooleanField(default=False)
	isPending = models.BooleanField(default=True,blank=True)
	when = models.DateField(auto_now_add=True,blank=True)
	def readable(self,string):
		return ' '.join(string.split('-'))
	def readableWhat(self):
		return self.readable(self.what)
	def readableWho(self):
		return self.readable(self.toWhom)
	def __str__(self):
		return self.what
	
		
	