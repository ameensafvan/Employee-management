# import random
# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from emp_mngt.models import Employee, country, job
# from faker import Faker
# from django.core.files.base import ContentFile
# import requests

# fake = Faker()

# class command(BaseCommand):
#     help = "Generate fake employee data"
    
#     def add_arguments(self, parser):
#         parser.add_argument('total', type = int, help='Number of fake employee create')
        
#     def handle(self, *args, **kwargs):
#         total = kwargs['total']
        
#         user = User.objects.first()
        
#         if not user:
#             self.stdout.write(self.style.ERROR("Please create a user first."))
#             return
        
#         countries = list(country.objects.all())
#         jobs = list(job.objects.all())
        
        
#         if not countries:
#             countries = [Country.objects.create(name=fake.country()) for _ in range(5)]

#         if not jobs:
#             jobs = [JobTitle.objects.create(title=fake.job()) for _ in range(5)]
            

#         for _ in range(total):
#             employee = Employee.objects.create(
#                 user=user,
#                 name=fake.name(),
#                 mobile=fake.phone_number(),
#                 phone=fake.phone_number(),
#                 country=random.choice(countries),
#                 city=fake.city(),
#                 job=random.choice(jobs),
#                 profile_photo=None  # or use a default placeholder if needed
#             )
#         self.stdout.write(self.style.SUCCESS(f"Successfully created {total} fake employees."))