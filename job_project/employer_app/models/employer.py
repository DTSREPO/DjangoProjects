from django.db import models


# Create your models here.
class Employer(models.Model):
  #Account Information
  user_name=models.CharField(max_length=20, default="", null = False)
  user_pass=models.CharField(max_length=12, default="", null = False)

  #Company Details
  company_name = models.CharField(max_length=200, default="", null = False)
  contact_person = models.CharField(max_length=200, default="", null = True)
  industry_type	= models.ManyToManyField("jobpost_app.Industry") #Foreign Key
  country = None
  city = None
  company_address = models.CharField(max_length=300, default="", null = False)
  billing_address = models.CharField(max_length=300, default="", null = False)
  contact_phone = models.CharField(max_length=13, default="", null = False)
  contact_email = models.CharField(max_length=100, default="", null = False)
  website = models.CharField(max_length=200, default="", null = True)