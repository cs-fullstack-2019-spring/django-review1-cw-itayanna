from django.shortcuts import render

# Create your views here.

def index(request, ):
    context = {'originPage' : originPage}
    return render(request, 'classworkApp/home.html', context)