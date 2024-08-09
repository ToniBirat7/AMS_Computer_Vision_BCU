from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
# def login_page(request):
#     if request.method == 'POST':
#         print(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print("*******")
#         print(username,password)
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is None:
#             messages.warning(request, 'Invalid Username or Password')
#             messages.warning(request, 'Please try again')
#         else: 
#             login(request, user)

#     return render(request, 'auth/login.html')

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("Post Request Form")
        print(form)

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is authenticated")
                login(request, user)
                return redirect('admin-page-name')
            else:
                print("User is not authenticated")
        else:
            print("Form is invalid")
            print(form.non_field_errors())
    else: 
        form = LoginForm()

    print("Get Request Form")

    return render(request, 'auth/login.html', {'form': form})      

def admin_view(request):
    return render(request, 'auth/admin.html')