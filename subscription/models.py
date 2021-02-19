from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from translated_fields import TranslatedField


# Create your models here.

class Subscription(models.Model):
    price =models.DecimalField(max_digits=19, decimal_places=10)
    name = models.TextField(null=True,blank=True)
    is_free = models.BooleanField(null=True,blank=True,default=False)
    
    # def __str__(self):
    #     return self.name



class SubscriptionText(models.Model):
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE,related_name="subscription_text")
    text = models.TextField()

    # def __str__(self):
    #     return self.text



class SubscriptionNotifications(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

class FAQ(models.Model):
    question = TranslatedField(
        models.CharField(_("question"), max_length=200,null=True),
    )
    answer = TranslatedField(
        models.CharField(_("answer"), max_length=200,null=True),
    )

