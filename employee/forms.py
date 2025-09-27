from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee, UserProfile, ROLES, Country, JobTitle

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'mobile', 'phone', 'country', 'city', 'job', 'profile_photo']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-input w-full border-gray-500 rounded-md'}),
            'mobile' : forms.TextInput(attrs={'class':'form-input w-full border-gray-500 rounded-md'}),
            'phone' : forms.TextInput(attrs={'class':'form-input w-full border-gray-500 rounded-md'}),
            'country' : forms.Select(attrs={'class':'form-select w-full border-gray-500 rounded-md'}),
            'city' : forms.TextInput(attrs={'class':'form-input w-full border-gray-500 rounded-md'}),
            'job' : forms.Select(attrs={'class':'form-select w-full border-gray-500 rounded-md'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-input w-full border-gray-500 rounded-md'}),
        }
        
common_input_classes = 'w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:outline-none'

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.EmailInput(attrs={
        'class': common_input_classes
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': common_input_classes
    }))
    role = forms.ChoiceField(choices=ROLES, widget=forms.Select(attrs={
        'class': common_input_classes
    }))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': common_input_classes
    }))
    mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': common_input_classes
    }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': common_input_classes
    }))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={
        'class': common_input_classes
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': common_input_classes
    }))
    job = forms.ModelChoiceField(queryset=JobTitle.objects.all(), widget=forms.Select(attrs={
        'class': common_input_classes
    }))
    profile_photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': common_input_classes + " file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
    }))
    
    password1 = forms.CharField(
    label="Password",
    strip=False,
    widget=forms.PasswordInput(attrs={
        'class': common_input_classes
    }),
    )
    password2 = forms.CharField(
    label="Confirm Password",
    strip=False,
    widget=forms.PasswordInput(attrs={
        'class': common_input_classes
    }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'name', 'mobile', 'phone', 'country', 'city', 'job', 'profile_photo']