# models.py
from django.db import models
	 
	# Create your models here.
	 
	class Message(models.Model):
		content = models.TextField()
	 


# urls.py
from django.urls import path
	 
	from .views import homePageView
	 
	urlpatterns = [
	    path('', homePageView, name='home')
	]



# views.py
from django.http import HttpResponse
	from .models import Message
	 
	 
	def homePageView(request):
		content = ''
		message = Message.objects.get(id=request.GET.get('id'))
		content = str(message.content)
		return HttpResponse(content)