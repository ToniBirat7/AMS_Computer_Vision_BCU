from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

Gender = [
    ('M', 'Male'),
    ('F', 'Female')
]

def file_upload(self, filename):
    return f'{self.user.username}_{filename}'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    primary_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)],unique=True) 
    secondary_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)],unique=True) 
    dob = models.DateField(null=True,blank=True)
    sex = models.CharField(max_length=1, choices=Gender)
    image = models.ImageField(upload_to=file_upload, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'teacher'
        ordering = ['user']
        verbose_name = 'Teacher'
        constraints = [
            models.UniqueConstraint(fields=['primary_number','secondary_number'], name='unique_primary_number')
        ] 