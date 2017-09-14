from django.db import models

# Create your models here.
class SeekerReg(models.Model):
  first_name = models.CharField(max_length=200, null=False)
  last_name = models.CharField(max_length=200, default="")
  gender = models.IntegerField(null=False)
  mobile = models.CharField(max_length=14, default="")
  email = models.CharField(max_length=200, default="")
  industry = models.ManyToManyField("jobpost_app.Industry")
  user_name = models.CharField(max_length=20, null=False)
  user_pass = models.CharField(max_length=20, null=False)
  create_by = models.CharField(max_length=20, default="")
  create_date = models.DateTimeField(auto_now_add=True, null=True)
  update_by = models.CharField(max_length=20, default="")
  update_date = models.DateTimeField(auto_now=True, null=True)
  active = models.BooleanField(default=True)