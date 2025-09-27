from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class JobTitle(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100)
    job = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    profile_photo = models.ImageField(upload_to='profile_photo/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name

ROLES =(
    ('SUPER_ADMIN', 'Super_Admin'),
    ('HR_MANAGER', 'HR Manager'),
    ('HR_EXECUTIVE', 'HR Executive'),
    ('EMPLOYEE', 'Employee')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"