# urls.py
from django.urls import path
	 
	from .views import homePageView
	 
	urlpatterns = [
	    path('', homePageView, name='home')
	]



# views.py
from django.http import HttpResponse
	 
	def homePageView(request):
	    return HttpResponse('Hello Web!')
	 