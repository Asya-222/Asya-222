from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "news/index.html", {"form": userform})