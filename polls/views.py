from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello,world. Ypu are at the polls index")
