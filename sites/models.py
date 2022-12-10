from django.db import models

# Create your models here.

class CustomSite(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    is_html = models.BooleanField(default=False)
    line_brake = models.BooleanField(default=False)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    last_change = models.DateTimeField(null=True, blank=True)

