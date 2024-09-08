from django.urls import path
from . import views
urlpatterns = [
    path('course-list/', views.course_list, name='course-list'),
    path('profile/', views.profile, name='profile'),
    path('remove-image/', views.remove_image, name='remove-image'),
]