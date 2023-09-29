# models.py
from django.db import models
    
from django.contrib.auth.models import User
    
# Create your models here.
    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.owner.id, filename)
    
class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.FileField(upload_to=user_directory_path)



# urls.py
from django.urls import path
    
from .views import homePageView, addView, deleteView, downloadView
    
urlpatterns = [
    path('', homePageView, name='home'),
    path('add/', addView, name='add'),
    path('download/<int:fileid>', downloadView, name='add'),
    path('delete/', deleteView, name='delete'),
]



# views.py
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import File
    
    
@login_required
def deleteView(request):
    f = File.objects.get(pk=request.POST.get('id'))
    if f.owner == request.user:
        f.delete()
        return redirect('/')
    else:
        return HttpResponse('You are not the owner of this file.')
    
    
@login_required
def downloadView(request, fileid):
    f = File.objects.get(pk=fileid)
    
    if f.owner == request.user:
        filename = f.data.name.split('/')[-1]
        response = HttpResponse(f.data, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
    
        return response
    else:
        return HttpResponse('You are not the owner of this file.')
    
    
@login_required
def addView(request):
    data = request.FILES.get('file')
    f = File(owner=request.user, data=data)
    f.save()
    return redirect('/')
    
    
@login_required
def homePageView(request):
    files = File.objects.filter(owner=request.user)
    uploads = [{'id': f.id, 'name': f.data.name.split('/')[-1]} for f in files]	
    return render(request, 'pages/index.html', {'uploads': uploads})



# index.html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Hihaupload</title>
    </head>
    
    
    <body>
        <h1>Hihaupload</h1>
    
        <table>
        <tr>
        <th style="text-align:left">Username: <td>{{user.username}} 
        </table>
    
    
        <form action='logout/' method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout"/>
        </form>
        
        <h2>Your files</h2>
    
        <table>
        {% for file in uploads %}
        <tr>
        <td>
        {{file.name}}
        <td>
        <a href="download/{{file.id}}">Download</a>
        <td>
        <form action='delete/' method="POST">
            {% csrf_token %}
            <input type="hidden" name="id" value="{{file.id}}" />
            <input type="submit" value="Delete"/>
        </form>
    
        {% endfor %}
        </table>
    
        <h2>Add file</h2>
    
        <form action='add/' method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <input type="file" name="file" id="file"/>
            <input type="submit" value="Add"/>
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