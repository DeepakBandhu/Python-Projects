from django.db import models

# Create your models here.


class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default="example: 1")
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(max_length=60, default="", blank=True, null=False)