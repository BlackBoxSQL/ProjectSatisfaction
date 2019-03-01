from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=False)


class TutorProfiles(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Your_Full_Name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.CharField(max_length=3)
    Date_of_Birth = models.DateField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    address = models.TextField(max_length=150)
    nid_No = models.CharField(max_length=18)
    tution_you_give_to_class = models.CharField(max_length=2)
    subjects_you_teach = models.CharField(max_length=100)
    phone_number = models.CharField("Contact Number", max_length=14)
    need_tution_from = models.DateField()
    fees_per_subject = models.CharField(max_length=5)
    week = models.CharField("How many days you are available?", max_length=1)
    tution_hour = models.CharField(max_length=3)
    description = models.TextField(max_length=250)

    def __str__(self):
        return 'User Name: {}, Tutor Name: {}'.format(self.user, self.Your_Full_Name)

    def get_absolute_url(self):
        return reverse('tutor:tutor_homepage', kwargs={'pk': self.pk})


class GuardianProfiles(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Guardians_name = models.CharField("Guardian's Name", max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    nid_No = models.CharField(max_length=18)
    occupation = models.CharField(max_length=20)
    students_name = models.CharField("Student's Name", max_length=50)
    s_class = models.CharField("Student's Class", max_length=2)
    school = models.CharField("School/College", max_length=60)
    subject = models.CharField(max_length=100)
    payment = models.CharField(max_length=5)
    tution_hour = models.CharField("Tution hours", max_length=3)
    guardian_contact = models.CharField("Guardian's Contact Number", max_length=14)
    need_tutor_from = models.DateField()
    description = models.TextField(max_length=250)
    address = models.TextField(max_length=150)

    def __str__(self):
        return 'User Name: {}, Guardian Name: {}'.format(self.user, self.Guardians_name)

    def get_absolute_url(self):
        return reverse('guardian:guardian_homepage', kwargs={'pk': self.pk})
