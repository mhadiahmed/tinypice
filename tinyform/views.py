from django.shortcuts import render
from .forms import tinyFormTest
from django.http import JsonResponse
from .models import tinytest

def home(request):
	form = tinyFormTest()
	if request.is_ajax():
		form = tinyFormTest(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			data = {
			'message':'form is saved'
			}
			return JsonResponse(data)
	context = {
	'form':form,
	}
	return render(request,'form.html',context)



