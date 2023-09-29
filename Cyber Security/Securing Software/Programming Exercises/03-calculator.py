# urls.py
from django.urls import path
	 
	from .views import addPageView
	from .views import multiplyPageView
	 
	urlpatterns = [
	    path('add/', addPageView, name='add'),
	    path('multiply/', multiplyPageView, name='multiply'),
	]



# views.py
from django.http import HttpResponse
	 
	 
	def addPageView(request):
		first_value = int(request.GET.get('first'))
		second_value = int(request.GET.get('second'))
		result = first_value + second_value
		return HttpResponse(result)
		
	 
	def multiplyPageView(request):
		first_value = int(request.GET.get('first'))
		second_value = int(request.GET.get('second'))
		result = first_value * second_value
		return HttpResponse(result)