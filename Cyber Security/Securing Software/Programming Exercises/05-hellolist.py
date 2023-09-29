# urls.py
from django.urls import path
	 
	from .views import homePageView
	 
	urlpatterns = [
	    path('', homePageView, name='home'),
	]



# views.py
from django.shortcuts import render
	 
	# Create your views here.
	 
	def homePageView(request):
		# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
		items = request.session.get('items', [])
	 
		# handling post request
		if request.method == 'POST':
			item = request.POST.get('content', '').strip()
			if len(item) > 0:
				items.append(item)
			request.session['items'] = items
	 
		# shorter way of writing instead of loader
		return render(request, 'pages/index.html', {'items' : items})



# index.html
<!DOCTYPE html>
	<html xmlns="http://www.w3.org/1999/xhtml">
	    <head>
	        <title>Hello List!</title>
	    </head>
	 
	    <body>
	        <h1>Hello List!</h1>
	 
	        <ul>
	            {% for item in items %}
	            {{ item }}
	            {% endfor %}
	        </ul>
	 
	        <form action="/" method="POST">
	            {% csrf_token %}
	            <input type="text" name="content" />
	            <input type="submit" />
	        </form>
	    </body>
	</html>