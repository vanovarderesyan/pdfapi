from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Contact(models.Model):
    subject = models.TextField()
    message = models.TextField()
    email = models.EmailField()

    
    def __str__(self):
        return self.message
