from django.shortcuts import render

# Create your views here.
def bio(request):
    return render(request, 'routing_app/bio.html')

def blog(request):
    return render(request, 'routing_app/blog.html')

def company(request):
    return render(request, 'routing_app/company.html')

def animations(request):
    return render(request, 'routing_app/animations.html')

def base(request):
    return render(request, 'routing_app/base.html')

# def test(request):
#     return render(request, 'routing_app/test.html')






'''
MODEL
class Gage(models.Model):
    deleted = models.BooleanField()

TEMPLATE
<form>
    <label for="">
        Is Cool
        <input 'name=yes_no' type='checkbox>
    </label>
</form>

when radio button is clicked, should return a value of 'on'
data is passed to request.POST 
in a QueryDict -> {'yes_no':['on']}

VIEW
def test(request):
    gage = Gage()
    form = request.POST
    
    if form['yes_no'] == 'on':
        gage.deleted = True
    else:
        gage.deleted = False

    gage.save()
'''