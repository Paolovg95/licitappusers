from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def panel(request):
    return render(request, "panel.html", {})
