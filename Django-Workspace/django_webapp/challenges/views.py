from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,

# Create your views here.

def jan(request):
    return HttpResponse('This is Jan challenge')


def feb(request):
    
    return HttpResponse('This is feb challenge')


def dynamic_month(request, month):
    try:
        print(type(month) == type('int'))
        if (type(month) == 'int'):
            return HttpResponse(f"This is dynamic {month}")
        else:
            return HttpResponseNotFound(f'{month} is not a number')
    except:
        pass
