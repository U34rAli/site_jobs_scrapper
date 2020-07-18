from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Scrapper(models.Model):
    scrapper_name = models.CharField(max_length=200)
    added_by = models.CharField(max_length=200)
    how_to_scrap = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scrapper_name


class Company(models.Model):
    company = models.ForeignKey(Scrapper, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    base_url = models.CharField(max_length=200)
    careers_url = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}\nBase Url: {self.base_url}\nCareers Url: {self.careers_url}'


class Job(models.Model):
    job = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title}\nDescription: {self.description}\nCompany: {self.job.name}'
