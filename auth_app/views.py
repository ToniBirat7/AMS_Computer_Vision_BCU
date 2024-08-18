from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm

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
    next = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        print("Post Request Form")
        # print(form)

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is authenticated")
                login(request, user)
                if user.is_superuser:
                    return redirect('admin-page-name')
                # return redirect(next if next else 'admin-page-name')
                print("Not Admin")
            else:
                print("User is not authenticated")
        else:
            print("Form is invalid")
    else: 
        form = LoginForm()
        print(f"Get Request Form")
        # print(form)

    return render(request, 'auth/login.html', {'form': form})   

@login_required
def admin_view(request):
    return render(request, 'auth/admin.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def register_user(request):
    print("Register User")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pswd1 = form.cleaned_data.get('password1')
            pswd2 = form.cleaned_data.get('password2')

            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                print("Username already exists")
                return redirect('register')

            User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=pswd1)
            messages.success(request, 'User Registered Successfully')
        else: 
            print(form.errors)
            print(form.non_field_errors())
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})

def person(request):
    user_list = User.objects.exclude(is_superuser=True)
    print(user_list)
    return render(request, 'auth/PersonRegistration.html', {'teachers': user_list})