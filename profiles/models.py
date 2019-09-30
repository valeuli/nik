from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


MALE = 'male'
FEMALE = 'female'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female')
)

FULL_TIME = 'full-time'
PART_TIME = 'part-time'
SELF_EMPLOYED = 'self-employed'
FREELANCE = 'freelance'
CONTRACT = 'contract'
INTERNSHIP = 'internship'
APPRENTICESHIP = 'apprenticeship'


EMPLOYMENT_TYPE_CHOICES = (
    (FULL_TIME, 'Full-Time'),
    (PART_TIME, 'Part-Time'),
    (SELF_EMPLOYED, 'Self-employed'),
    (FREELANCE, 'Freelance'),
    (CONTRACT, 'Contract'),
    (INTERNSHIP, 'Internship'),
    (APPRENTICESHIP, 'Apprenticeship')
)


class UserProfile(models.Model):
    phone_number = PhoneNumberField(
        null=True,
        unique=True,
        verbose_name="phone",
    )
    title = models.CharField(
        max_length=50,
        null=True,
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        null=True
    )
    country = CountryField()
    user = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name='profile',
      related_query_name='profile'
    )


class Experience(models.Model):
    title = models.CharField(
        max_length=100
    )
    employment_type = models.CharField(
        max_length=14,
        choices=EMPLOYMENT_TYPE_CHOICES
    )
    company = models.CharField(
        max_length=100
    )
    country = CountryField()
    start_date = models.DateField()
    end_date = models.DateField(
        null=True
    )
    current_work = models.BooleanField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='experience',
        related_query_name='experience'
    )
   

class Education(models.Model):
    school = models.CharField(
        max_length=100)
    degree = models.CharField(
        max_length=50)
    field_of_study = models.CharField(
        max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()  # type: IntegerField
    grade = models.DecimalField(
        null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='education',
        related_query_name='education'
    )
