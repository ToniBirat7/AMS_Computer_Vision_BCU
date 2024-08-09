from django.urls import path
from auth_app import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('admin-page/', views.admin_view, name='admin-page-name'),
]
