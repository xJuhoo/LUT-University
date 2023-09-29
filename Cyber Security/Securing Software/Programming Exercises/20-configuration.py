# models.py
from django.db import models
    
from django.contrib.auth.models import User
    
# Create your models here.
    
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()



# urls.py
from django.urls import path
    
from .views import homePageView, transferView
    
urlpatterns = [
    path('', homePageView, name='home'),
    path('transfer/', transferView, name='transfer'),
]



# views.py
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account
    
    
@login_required
@requires_csrf_token
def transferView(request):
    
    if request.method == 'POST':
        userFrom = User.objects.get(username=request.user)
        userTo = User.objects.get(username=request.POST['to'])
        amount = int(request.POST['amount'])
    
        accountFrom = Account.objects.get(user=userFrom)
        accountTo = Account.objects.get(user=userTo)
    
        if accountFrom.balance >= amount and amount >= 0:
            accountFrom.balance -= amount
            accountTo.balance += amount
    
            accountTo.save()
            accountFrom.save()
    
        else:
            return redirect('/')
    
    return redirect('/')
    
    
    
@login_required
def homePageView(request):
    accounts = Account.objects.exclude(user_id=request.user.id)
    return render(request, 'pages/index.html', {'accounts': accounts})



# index.html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    
<head>
    <title>Bank Transfer</title>
</head>
    
    
<body>
    <h1>Your account</h1>
    
    <table>
        <tr>
            <th style="text-align:left">Username:
            <td>{{user.username}}
        <tr>
            <th style="text-align:left">Balance:
            <td>{{user.account.balance}}
    </table>
    
    
    <form action='logout/' method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout" />
    </form>
    
    <h2>Transfer money</h2>
    
    <form id='transfer' action='transfer/' method="POST">
        {% csrf_token %}
        <span>To:</span><br />
        <select name="to">
            {% for account in accounts %}
            <option value="{{account.user.username}}">{{account.user.username}}</option>
            {% endfor %}
        </select><br />
    
        <span>Amount:</span><br />
        <input type="number" name="amount" /><br />
    
        <input type="submit" value="Transfer" />
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