from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, TeacherForm, StudentForm, CourseForm, StudentClassForm
from .models import Teacher, Student, Course, StudentClass, Attendance
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
from django.db.models import Q

def login_page(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Handle remember me functionality
            if not remember_me:
                request.session.set_expiry(0)
            
            if user.is_superuser:
                return redirect('admin-page-name')
            else:
                return redirect('course-list')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'auth/login.html')

@login_required
def admin_view(request):
    teachers = Teacher.objects.select_related('user').all()
    students = Student.objects.all().order_by('-id')
    courses = Course.objects.select_related('teacher', 'teacher__user').all()
    
    context = {
        'teachers': teachers,
        'students': students,
        'courses': courses,
        'teacher_count': teachers.count(),
        'student_count': students.count(),
        'course_count': courses.count(),
    }
    
    return render(request, 'auth/admin.html', context)

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
                form.add_error('username', f'Username with {username} already exists')
                print("Username already exists")
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=pswd1)
                messages.success(request, 'User Registered Successfully')
                form = UserRegistrationForm()
        else: 
            print("Field Errors")
            print(form.errors)
            print("Non-Field Errors")
            print(form.non_field_errors())
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})

@login_required
def teacher(request):
    user_list = User.objects.exclude(is_superuser=True)
    form = TeacherForm()

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():
            print("Cleaned Data")
            print("*************")
            print(form.cleaned_data)
            user = form.cleaned_data['teacher']
            address = form.cleaned_data['address']
            dob = form.cleaned_data['dob']
            primary_number = form.cleaned_data['primary_number']
            secondary_number = form.cleaned_data['secondary_number']
            sex = form.cleaned_data['sex']
            my_image = form.cleaned_data['my_image']

            if Teacher.objects.filter(user=user).exists():
                print("User already exists")
                form.add_error('teacher', f'User with {user.username} already exists')
            else:
                try:
                    Teacher.objects.create(user=user,
                                        address=address, 
                                        dob=dob, 
                                        primary_number=primary_number, 
                                        secondary_number=secondary_number,
                                        sex=sex,
                                        image=my_image)
                    messages.success(request, 'Teacher Created Successfully')
                    form = TeacherForm()
                except Exception as e:
                    print("Error in Creating User")
        else:   
            print("Form is Invalid")
            print(form.errors)

    return render(request, 'auth/PersonRegistration.html', {'teachers': user_list, 'form': form})

def teacher_image(request):
    teacher = Teacher.objects.all()
    for item in teacher:
        print(item.image)
    return render(request, 'auth/teacher_image.html', {'teachers': teacher})

@login_required
def add_student(request):
    print(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)    
        print("Post Request")
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Student Added Successfully')
            form = StudentForm()
        else:
            print(form.errors)
    else: 
        form = StudentForm()
        print("Get Request")
        print(form)
    return render(request, 'auth/addstudent.html', {'form': form})

@login_required
def add_course(request):
    teachers = Teacher.objects.prefetch_related('user').all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Course Added Successfully')
            form = CourseForm()
        else: 
            print(form.errors)
    else:
        form  = CourseForm()
        form.fields['teacher'].choices = [(teacher.id, f'{teacher.user.first_name} {teacher.user.last_name}') for teacher in teachers]
    return render(request, 'auth/addcourse.html', {'form': form})

@login_required
def add_student_class(request):
    if request.method == "POST":
        form = StudentClassForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            for item in form.cleaned_data.get('student'):
                StudentClass.objects.create(course=form.cleaned_data['course'], student=item)
            messages.success(request, 'Student Class Added Successfully')
            form = StudentClassForm()
        else:
            print("Form is Invalid")
            print(form.errors)
    else:
        form = StudentClassForm()
    return render(request, 'auth/addclass.html',{'form': form})

@login_required
def list_students(request):
    students = Student.objects.all()
    return render(request, 'auth/list_students.html', {'students': students})

@login_required
def list_teachers(request):
    teachers = Teacher.objects.all()
    print(teachers[0].image.url)
    return render(request, 'auth/list_teachers.html', {'teachers': teachers})

@login_required
def get_student(request, id):
    student = get_object_or_404(Student, id=id)
    data = {
        'name': student.name,
        'address': student.address,
        'age': student.age,
        'phone_number': student.phone_number
    }
    return JsonResponse(data)

@login_required
def edit_student(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=id)
        try:
            student.name = request.POST.get('name')
            student.address = request.POST.get('address')
            student.age = request.POST.get('age')
            student.phone_number = request.POST.get('phone_number')
            student.save()
            messages.success(request, 'Student updated successfully')
            return JsonResponse({'success': True})
        except Exception as e:
            messages.error(request, 'Error updating student')
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
@require_POST
def update_student(request):
    try:
        student_id = request.POST.get('student_id')
        student = Student.objects.get(id=student_id)
        
        # Update student details
        student.name = request.POST.get('name')
        student.address = request.POST.get('address')
        student.phone_number = request.POST.get('phone_number')
        student.age = request.POST.get('age')
        student.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Student updated successfully'
        })

    except Student.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Student not found'
        }, status=404)
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@login_required
@require_POST
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()

        return JsonResponse({
            'success': True,
            'message': 'Student deleted successfully'
        })
        
    except Student.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Student not found'
        }, status=404)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@login_required
def get_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    data = {
        'address': teacher.address,
        'primary_number': teacher.primary_number,
        'secondary_number': teacher.secondary_number,
        'dob': teacher.dob,
        'image_url': teacher.my_image.url if teacher.my_image else None
    }
    return JsonResponse(data)

@login_required
@require_POST
def update_teacher(request):
    try:
        teacher_id = request.POST.get('teacher_id')
        teacher = Teacher.objects.get(id=teacher_id)
        
        # Update teacher details
        teacher.address = request.POST.get('address')
        teacher.primary_number = request.POST.get('primary_number')
        teacher.secondary_number = request.POST.get('secondary_number', '')
        teacher.dob = request.POST.get('dob')
        teacher.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Teacher updated successfully'
        })

    except Teacher.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Teacher not found'
        }, status=404)
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@login_required
@require_POST
def delete_teacher(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
        
        # Delete associated user
        if teacher.user:
            teacher.user.delete()  # This will cascade delete the teacher due to OneToOne relationship
        else:
            teacher.delete()

        return JsonResponse({
            'success': True,
            'message': 'Teacher deleted successfully'
        })
        
    except Teacher.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Teacher not found'
        }, status=404)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@login_required
def student_report_view(request):
    return render(request, 'auth/student_report.html')

@login_required
def get_student_report(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        
        # Get student's courses through StudentClass
        student_classes = StudentClass.objects.filter(student=student)
        
        # Calculate attendance for each course
        courses_data = []
        total_present = 0
        total_absent = 0
        
        for sc in student_classes:
            course = sc.course
            # Using the correct field name 'stats' instead of 'status'
            present_days = Attendance.objects.filter(
                student=student,
                course=course,
                stats='P'
            ).count()
            
            absent_days = Attendance.objects.filter(
                student=student,
                course=course,
                stats='A'
            ).count()
            
            total_days = present_days + absent_days
            
            attendance_rate = (present_days / total_days * 100) if total_days > 0 else 0
            
            courses_data.append({
                'title': course.title,
                'present_days': present_days,
                'absent_days': absent_days,
                'attendance_rate': round(attendance_rate, 1)
            })
            
            total_present += present_days
            total_absent += absent_days

        # Calculate monthly attendance for the chart using correct field names
        monthly_attendance = (
            Attendance.objects.filter(student=student)
            .annotate(month=TruncMonth('today_date'))  # Using today_date instead of date
            .values('month')
            .annotate(
                present=Count('id', filter=Q(stats='P')),  # Using stats='P' instead of status='present'
                total=Count('id')
            )
            .order_by('month')
        )

        monthly_data = []
        for ma in monthly_attendance:
            rate = (ma['present'] / ma['total'] * 100) if ma['total'] > 0 else 0
            monthly_data.append({
                'month': ma['month'].strftime('%B %Y'),
                'rate': round(rate, 1)
            })

        # Calculate overall attendance rate
        total_days = total_present + total_absent
        overall_rate = (total_present / total_days * 100) if total_days > 0 else 0

        return JsonResponse({
            'id': student.id,
            'name': student.name,
            'courses': courses_data,
            'total_present': total_present,
            'total_absent': total_absent,
            'attendance_rate': round(overall_rate, 1),
            'monthly_attendance': monthly_data
        })

    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)