from django.http import HttpResponse
    
    
def addPageView(request):
    first_value = int(request.GET.get('first'))
    second_value = int(request.GET.get('second'))
    result = first_value + second_value
    return HttpResponse(result)
    
    
def multiplyPageView(request):
    first_value = int(request.GET.get('first'))
    second_value = int(request.GET.get('second'))
    result = first_value * second_value
    return HttpResponse(result)