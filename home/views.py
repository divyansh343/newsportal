from django.shortcuts import render
# from home.models import Contact
# Create your views here.
from django.shortcuts import render



def index(request):
    return render(request, 'home/index.html')
def about(request):
    return render(request, 'home/about.html')
def contact(request):
    return render(request, 'home/contact.html')

# def contact(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         phone=request.POST['phone']
#         message=request.POST['message']
#         contact=Contact(name=name, email=email, phone=phone, message=message)
#         contact.save()
#     return render(request, "home/contact.html")