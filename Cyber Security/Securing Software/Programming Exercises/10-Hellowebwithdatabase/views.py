from django.http import HttpResponse
from .models import Message
    
    
def homePageView(request):
    content = ''
    message = Message.objects.get(id=request.GET.get('id'))
    content = str(message.content)
    return HttpResponse(content)