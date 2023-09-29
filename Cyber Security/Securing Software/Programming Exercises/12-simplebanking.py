# models.py
from django.db import models
	 
	from django.contrib.auth.models import User
	 
	class Account(models.Model):
		owner = models.ForeignKey(User, on_delete=models.CASCADE)
		iban = models.TextField()



# urls.py
from django.urls import path
	 
	from .views import homePageView, addView
	 
	urlpatterns = [
	    path('', homePageView, name='home'),
	    path('add/', addView, name='add'),
	]
	 


# views.py
from django.http import HttpResponse
	from django.contrib.auth.decorators import login_required
	from django.shortcuts import render, redirect
	from django.contrib.auth.models import User
	from .models import Account
	from django.db.models import Q
	import json
	 
	 
	 
	@login_required
	def addView(request):
		if request.method == 'POST':
			newIban = request.POST['iban']
			currentUser = request.user
			newAccount = Account.objects.create(owner=currentUser, iban=newIban)
	 
		return redirect('/')
	 
	 
	@login_required
	def homePageView(request):
		currentUser = request.user
		accountsList = Account.objects.filter(owner=currentUser)
		accountsIbans = [x.iban for x in accountsList]
		print(accountsIbans)
		return render(request, 'pages/index.html', {'accounts': accountsIbans})



# index.html
<!DOCTYPE html>
	<html xmlns="http://www.w3.org/1999/xhtml">
	 
	<head>
	    <title>Lemon Brothers Bank</title>
	</head>
	 
	 
	<body>
	    <h1>Lemon Brothers Bank</h1>
	 
	    <table>
	        <tr>
	            <th style="text-align:left">Username:
	            <td>{{user.username}}
	    </table>
	 
	 
	    <form action='logout/' method="POST">
	        {% csrf_token %}
	        <input type="submit" value="Logout" />
	    </form>
	 
	    <h2>Your IBAN accounts</h2>
	 
	    <ul>
	        {% for a in accounts %}
	 
	        <li>{{a}}
	        </li>
	 
	        {% endfor %}
	    </ul>
	 
	 
	    <h2>Create a new account</h2>
	 
	    <form action='add/' method="POST">
	        {% csrf_token %}
	 
	        <input type="text" name="iban" /><br />
	        <input type="submit" value="Send" />
	    </form>
	</body>
	 
	 
	</body>
	 
	</html>



# login.html
<h2>Login</h2>
<form method="post">
	{% csrf_token %}
	{{ form.as_p }}
	<button type="submit">Login</button>
</form>
	 