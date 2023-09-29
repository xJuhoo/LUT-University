# urls.py
from django.urls import path
	 
	from .views import homePageView, addPageView, erasePageView
	 
	urlpatterns = [
	    path('', homePageView, name='home'),
	    path('add', addPageView, name='add'),
	    path('erase', erasePageView, name='erase')
	]



# views.py
from django.shortcuts import render
	 
	def addPageView(request):
		items = request.session.get('items', [])
	 
		# handling post request
		if request.method == 'POST':
			note = request.POST.get('content', '').strip()
			if len(note) > 0:
				if len(items) >= 10:
					# If the list contains more than 10 notes we remove the earliest one
					items.pop(0)
				items.append(note)
			request.session['items'] = items
	 
	 
		return render(request, 'pages/index.html', {'items' : items})
	 
	 
	def erasePageView(request):
		items = request.session.get('items', [])
	 
		# Handling the POST request to erase all notes
		if request.method == 'POST':
			items = [] # Erase all notes
	 
			request.session['items'] = items # Update the session
	 
		return render(request, 'pages/index.html', {'items' : items})
	 
	 
	def homePageView(request):
		# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
		items = request.session.get('items', [])
		request.session['items'] = items
	 
		# shorter way of writing instead of loader
		return render(request, 'pages/index.html', {'items' : items})



# index.html
<!DOCTYPE html>
	<html xmlns="http://www.w3.org/1999/xhtml">
	    <head>
	        <title>Hello Notes!</title>
	    </head>
	 
	    <body>
	        <h1>Hello Notes!</h1>
	 
	        <ul>
	            {% for note in items %}
	            {{ note }}
	            {% endfor %}
	        </ul>
	 
	        <h2>Add content to list</h2>
	        <form action="/" method="POST">
	            {% csrf_token %}
	            <input type="text" name="content" />
	            <input type="submit" />
	        </form>
	 
	        <h2>Clear everything</h2>
	        <form action="/erase" method="POST">
	            {% csrf_token %}
	            <input type="submit" value="Clear notes" />
	        </form>
	    </body>
	</html>

