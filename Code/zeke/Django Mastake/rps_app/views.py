from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'rps_app/index.html')

def results(request):
    return render(request, 'rps_app/results.html')
