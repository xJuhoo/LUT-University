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
