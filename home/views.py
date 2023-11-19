from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render( request,'index.html')

#def about(request):
    return render(request,'index.html')

#def skills(request):
    return render(request,'index.html')

#def education(request):
    return render(request,'index.html')

#def work(request):
    return render(request,'index.html')

#def experience(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        number=request.POST.get('number')
        contact= Contact(name=name, email=email, number=number, desc=desc, date=datetime.today())
        contact.save()
    return render(request,'index.html')