from django.shortcuts import redirect
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('table_employee', views.employee_table, name='table_employee'),
    path('add/', views.add_employee, name='add_employee'),
    path('register/', views.register, name='register'),
    path('import_excel/', views.import_excel, name='import_excel'),
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('search/', views.search_emp, name='search_emp')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)