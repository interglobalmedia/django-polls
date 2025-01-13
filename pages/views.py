from django.shortcuts import render

from .models import HomePage


# Create your views here.
def index(request):
    pages = HomePage.objects.all()
    return render(request, "pages/index.html", {"pages": pages})
