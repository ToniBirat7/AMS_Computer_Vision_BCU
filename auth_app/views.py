from django.shortcuts import render
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
        login_form = LoginForm(request.POST)
        print("Post Request Form")
        print(login_form)

        if login_form.is_valid():
            print(login_form.cleaned_data)
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is authenticated")
                login(request, user)
            else:
                print("User is not authenticated")
        else:
            print("Form is invalid")

    form = LoginForm()

    print("Get Request Form")

    return render(request, 'auth/login.html', {'form': form})      