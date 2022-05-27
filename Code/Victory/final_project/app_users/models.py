from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

hospital_departments = [ 
    ('Primary Care', 'Primary Care'),
    ('Billing', 'Billing'),
    ('Human Resources', 'Human Resources'),
]
# occupation = [ 
#     'Administration', 'Administration'
# ]

class Occupation(models.Model):
    title = models.CharField(max_length=40)
    def __str__(self):
        return self.title

class Physician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img/PhysicianImg', null=True, blank=True)
    department = models.CharField(max_length=100, choices=hospital_departments, default='Primary Care')
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    @property
    def name_info(self):
        self.user.first_name+' '+self.user.last_name

    @property
    def id_info(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.hospital_departments)

class CodeSpecialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img/CoderImg', null=True, blank=True)
    department = models.CharField(max_length=100, choices=hospital_departments, default='Billing')
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    @property
    def name_info(self):
        self.user.first_name+' '+self.user.last_name

    @property
    def id_info(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.hospital_departments)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img/PatientImg', null=True, blank=True)
    pt_address=models.CharField(max_length=50, default=False)
    city=models.CharField(max_length=30, default="San Diego")
    state =models.CharField(max_length=2, default='CA')
    zip_code=models.IntegerField(max_length=6, default='92109')
    phone=models.IntegerField(max_length=50,default=False)
    email=models.EmailField(max_length=50,default=False)
    notes = models.TextField()
    assessment = models.CharField(max_length=50)  #this is what the api will be fetching data for
    status = models.BooleanField(default=False)

    @property
    def name_info(self):
        self.user.first_name+' '+self.user.last_name

    @property
    def id_info(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+"("+self.assessment+")"


# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_img = models.ImageField(upload_to='profile_img/PatientImg', null=True, blank=True)
#     date_seen = models.DateTimeField(auto_now_add=True)
#     notes = models.TextField()
#     assessment = models.CharField(max_length=50)  #this is what the api will be fetching data for
#     status = models.BooleanField(default=False)

#     @property
#     def name_info(self):
#         self.user.first_name+' '+self.user.last_name

#     @property
#     def id_info(self):
#         return self.user.id
#     def __str__(self):
#         return self.user.first_name+"("+self.assessment+")"



# class MedicalRecord(models.Model):
