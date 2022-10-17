from django.shortcuts import render
from .forms import CreateForm

# Create your views here.
def create(request):
    if request.method == "POST":
        # 이미지를 받아올 때는 request.FILES 객체도 같이 받아올 것
        forms = CreateForm(request.POST, request.FILES)
        if forms.is_valid:
            forms.save()
            return render(request, 'base.html')
    
    else:
        forms = CreateForm()
    context = {
        "forms" : forms,
    }
    return render(request, "uploads/create.html", context)