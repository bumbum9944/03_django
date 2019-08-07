from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    return render(request, 'create.html')