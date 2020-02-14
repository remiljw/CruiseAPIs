from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField #This is a custom field that requires mysql

# Create your models here.
class Excursion(models.Model):
  Active = 'active'
  Inactive = 'inactive'
  Excursion_status = [
    (Active, 'active'),
    (Inactive, 'inactive'),
  ]
  id = models.BigIntegerField(primary_key=True,unique=True)
  name = models.CharField(max_length=200)
  detailPageName = models.CharField(max_length=400)
  portID = models.CharField(max_length=10)
  types = models.CharField(max_length=10)
  topology = ListCharField(base_field= CharField(max_length=10),size=6,max_length=(6*11)) # * 10 inputs plus comma. This is a custom field that requires mysql
  activityLevel = models.CharField(max_length=20)
  collectionType = models.CharField(max_length=30)
  duration = models.CharField(max_length=100)
  language = ListCharField(base_field= CharField(max_length=10),size=6,max_length=(6*11)) # * 10 inputs plus comma, This is a custom field that requires mysql
  priceLevel = models.IntegerField(null=True)
  currency = models.CharField(max_length=10)
  mealInfo = models.CharField(max_length=100,blank=True)
  status = models.CharField(max_length=10, choices = Excursion_status,default=Active)
  shortDescription = models.CharField(max_length=200,blank=True)
  longDescription = models.TextField()
  externalContent = models.BooleanField(default=False)
  minimumAge = models.CharField(max_length=10,blank=True)
  wheelChairAccecsible = models.BooleanField(default=False)
  featured = models.BooleanField(default=True)

  def __str__(self):
    return self.name