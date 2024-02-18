from django.shortcuts import render
from .models import query

def msg(request):
    if request.method=="POST":
        n=request.POST.get('name')
        em =request.POST.get('email')
        sub=request.POST.get('subject')
        cont=request.POST.get('contact')
        mssg=request.POST.get('message')
        data=query.objects.create(Name=n,Email=em,Subject=sub,Contact=cont,Message=mssg)
        data.save()
    return render(request,'index.html')
# Create your views here.
