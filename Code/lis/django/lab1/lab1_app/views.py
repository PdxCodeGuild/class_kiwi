from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'lab1_app/index.html')


def results(request):
    if request.method == 'POST':
        cipher = request.POST["cipher"].upper()
        rotation = int(request.POST["rotation"])
        ciphered_results = ""
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for x in cipher:
            ciphered_results += (letters[(letters.index(x) + rotation) % 26])

        dict = {
            'cipher': cipher,
            'rotation': rotation,
            'ciphered_results': ciphered_results
        }
        return render(request, 'lab1_app/results.html', dict)
