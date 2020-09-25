from django.db import models

# Create your models here.
from django.db import models


class Attendnce(models.Model):
    student_name = models.CharField(max_length=200, default="", null=True)
    student_id = models.CharField(max_length=200, default="", null=True)




    def __str__(self):
        return self.student_name
