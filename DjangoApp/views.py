from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Tribal App API</h1> <a href='/products'> Click to go to products </a>")