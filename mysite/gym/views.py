from django.shortcuts import render

# Create your views here.
def shalom(request):

    return render(request, 'shalom.html')