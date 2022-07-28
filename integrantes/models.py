from datetime import datetime
from unittest.main import MODULE_EXAMPLES
from django.db import models
from django.forms import CharField
from datetime import datetime


class integrantes(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    daily_work_hours = models.FloatField()
    pets = models.CharField(max_length= 20, null = True, blank = True)
    data_creation_date = models.DateField(auto_now_add = True)