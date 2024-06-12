from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, ' numphase_app/index.html')

def index(request):
    if request.method == 'GET':  
      return render(request, ' numphase_app/index.html')

    elif request.method == 'POST':
        print(request.POST['number'], 'find request data')

        user = request.POST['number']
        user_number = int(user)
        
