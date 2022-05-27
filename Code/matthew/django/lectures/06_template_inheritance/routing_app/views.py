from django.shortcuts import render

# Create your views here.

def bio(request):
    
    return render(request, 'routing_app/bio.html')

def animation(request):
    return render(request, 'routing_app/animation.html')

def base(request):
    return render(request, 'routing_app/base.html')

def blog(request):
    return render(request, 'routing_app/blog.html')

def company(request):
    return render(request, 'routing_app/company.html')
