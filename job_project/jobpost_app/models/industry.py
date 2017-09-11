from django.db import models

# Create your models here.
class Industry(models.Model):
  name = models.CharField(max_length=200, default="")
  slug = models.CharField(max_length=250, default="", unique=True)
  description = models.CharField(max_length=400, default="")
  create_by = models.CharField(max_length=20, default="")
  create_date = models.DateTimeField(auto_now_add=True, null=True)
  update_by = models.CharField(max_length=20, default="")
  update_date = models.DateTimeField(auto_now=True, null=True)
  active = models.BooleanField(default=True)