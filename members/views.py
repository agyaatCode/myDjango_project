# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the members section!")

from django.shortcuts import render

def home(request):
    return render(request, 'myfirst.html')  # Renders the template 'myfirst.html'