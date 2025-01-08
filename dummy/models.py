from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
 
class Dummies(models.Model):
    
    CATEGORY = [
        ('store_display', 'store_display'),
        ('fashion', 'fashion'),
        ('customizable', 'customizable'),
        ('men', 'men'),
        ('women', 'women'),
        ('kids', 'kids'),
        ('full', 'full'),
        ('half', 'half'),
    ]

    STATUS = [
        
        ('available', 'available'),
        ('out', 'out'),
    ]

    category = models.CharField(max_length=40, choices=CATEGORY)
    status = models.CharField(max_length=40, choices=STATUS)
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='content/',blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=10000)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
 