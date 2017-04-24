from django.shortcuts import render, redirect
from django.db import models
from .models import Rejectable
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
# Create your views here.

def HomePage(request):
	pendingRequests = Rejectable.objects.order_by('when').reverse()
	context = {'rejectables': pendingRequests}
	return render(request, 'tracker/rejectables.html', context)	

def goBack():
	return HttpResponseRedirect('/tracker')
def Pending(request,what):
	
	try:
		task = Rejectable.objects.get(pk=what)
		context = {'task': task}
	except (KeyError):
		return HttpResponse("sorry bruh, doesn't seem to exist")
	try:
		obj = Rejectable.objects.get(pk=what)
		print(request.POST)
		if request.POST.get('name',None) != None:
			obj.what = '-'.join(request.POST.get('name',None).split(' '))
			obj.when = timezone.now()
			obj.save()
			oldObj = Rejectable.objects.get(pk=what)
			oldObj.delete()
			print('we just deleted '+what)
			return goBack()
		if request.POST.get('who',None)!= None:
			obj.toWhom = '-'.join(request.POST.get('who',None).split(' '))
			obj.when = timezone.now()
			obj.save()
			return goBack()
		if request.POST.get('delete',None)=='y':	
			obj.delete()
			return goBack()
		if request.POST.get('update',None)=='y':
			obj.accepted=True
			obj.isPending=False
			obj.when = timezone.now()
			obj.save()
			return goBack()
			
		if request.POST.get('update',None)=='n':
			obj.accepted=False
			obj.isPending=False
			obj.when = timezone.now()
			obj.save()
			return goBack()
		if request.POST['back']=='y':
			return goBack()
	except:
		pass
	return render(request, 'tracker/status.html', context)
def NewTask(request):
	context = { 'created':False }
	try:
		if (request.POST.get('what',None) not in [None,'']) and (request.POST.get('who',None) not in [None,'']):
			print(str(request.POST.get('what',None)))
			what = '-'.join(request.POST.get('what',None).split(' '))
			who = '-'.join(request.POST.get('who',None).split(' '))
			newTask = Rejectable()
			newTask.what = what 
			newTask.toWhom = who 
			newTask.when = timezone.now()
			newTask.save()
			context['created']=True
		
		elif request.POST['back']=='y':
			return goBack()
	except:
		pass 
	return render(request, 'tracker/newTask.html', context)