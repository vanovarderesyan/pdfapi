from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Subscription(models.Model):
    price =models.DecimalField(max_digits=19, decimal_places=10)
    body = RichTextField()
    is_free = models.BooleanField(null=True,blank=True,default=False)
    
    def __str__(self):
        return self.body


class SubscriptionNotifications(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email