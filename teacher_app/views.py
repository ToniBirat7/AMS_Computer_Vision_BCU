from django.shortcuts import render
from auth_app.models import Teacher, Course
from django.shortcuts import redirect
from .forms import ImageForm

import os 
from django.conf import settings
from django.core.files.storage import default_storage

# Create your views here.

def course_list(request):
    print("Course List")
    print(request.user.id)
    user_id = request.user.id
    teacher = Teacher.objects.get(user=user_id)
    list_of_courses = Course.objects.filter(teacher=teacher).prefetch_related('teacher')
    print(list_of_courses)
    return render(request, 'attendance/course_list.html',{'courses':list_of_courses})

def profile(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user=user_id)
    list_of_courses = Course.objects.filter(teacher=teacher).prefetch_related('teacher')

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            teacher.image = form.cleaned_data['image']
            teacher.save()
        else: 
            print(form.errors)
    else:
        form = ImageForm()
    return render(request, 'attendance/profile.html',{'courses':list_of_courses,'teacher':teacher,'form':form})

def remove_image(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user=user_id)
    if teacher.image and teacher.image.name != 'NA':
        image_path = os.path.join(settings.MEDIA_ROOT, teacher.image.name)
        print("Image Path")
        print(image_path)
        if default_storage.exists(image_path):
            default_storage.delete(image_path)
            teacher.image = 'NA'
            teacher.save()
    return redirect('profile')