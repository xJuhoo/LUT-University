# models.py
from django.db import models
	 
	# Create your models here.
	 
	class Account(models.Model):
		iban = models.TextField()
		balance = models.IntegerField()



# urls.py
from django.urls import path
	 
	from .views import homePageView
	 
	urlpatterns = [
	    path('', homePageView, name='home'),
	]



# views.py
from django.shortcuts import render
	from django.template import loader
	from django.db import transaction
	from .models import Account
	 
	def transfer(sender, receiver, amount):
		# Atomic portion first
		with transaction.atomic():
			if sender == receiver:
				return
			
			acc1 = Account.objects.get(iban=sender)
			acc2 = Account.objects.get(iban=receiver)
	 
			if acc1.balance >= amount and amount >= 0:
				acc1.balance -= amount
				acc2.balance += amount
	 
			acc1.save()
			acc2.save()
	 
	 
	def homePageView(request):
		if request.method == 'POST':
			sender = request.POST.get('from')
			receiver = request.POST.get('to')
			amount = int(request.POST.get('amount'))
			transfer(sender, receiver, amount)
	 
		accounts = Account.objects.all()
		context = {'accounts': accounts}
		return render(request, 'pages/index.html', context)



# index.html
<!DOCTYPE html>
	<html xmlns="http://www.w3.org/1999/xhtml">
	    <head>
	        <title>Bank Transfer</title>
	    </head>
	 
	    <body>
			<h1>Accounts and balances</h1>
	 
	        <table>
	            <tr>
	                <th style="text-align:left">Account name</th>
	                <th style="text-align:right">Balance</th>
	            </tr>
				{% for account in accounts %}
				<tr>
					<td style="text-align:left">{{account.iban}}</td>
					<td style="text-align:right">{{account.balance}}</td>
				</tr>	
				{% endfor %}
	        </table>
	 
	        <h2>Transfer money</h2>
	 
	        <form method="POST">
				{% csrf_token %}
	            <span>From:</span><br/>
	            <select name="from">
				{% for account in accounts %}
	                <option value="{{account.iban}}">{{account.iban}}</option>
				{% endfor %}
	            </select><br/>
	 
	            <span>To:</span><br/>
	            <select name="to">
				{% for account in accounts %}
	                <option value="{{account.iban}}">{{account.iban}}</option>
				{% endfor %}
	            </select><br/>
	 
	            <span>Amount:</span><br/>
	            <input type="number" name="amount"/><br/>
	 
	            <input type="submit" value="Add!"/>
	        </form>
	    </body>
	 
	 
	    </body>
	</html>

