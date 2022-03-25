from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'unit_converter_app/index.html')


# request.POST is grabbing the information inside of the from submission
def forms(request):
    form_post = request.POST
    # print(form_post)
    return (request, 'unit_converter_app/result.html', form_post)
