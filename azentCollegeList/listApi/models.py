from django.db import models

# Create your models here.


class CollegeList (models.Model):
    alpha_two_code = models.CharField(max_length=10, blank=False, default='')
    country = models.CharField(max_length=200, blank=False, default='')
    domain = models.CharField(max_length=10, blank=False, default='')
    name = models.CharField(max_length=100, blank=False, default='')
    web_page = models.CharField(max_length=300, blank=False, default='')
