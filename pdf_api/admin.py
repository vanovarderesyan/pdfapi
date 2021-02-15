from django.contrib import  admin
from  django.contrib.admin import  AdminSite
from  django.utils.translation import  ungettext_lazy
from authentication.models import User
from subscription.models import Subscription,SubscriptionNotifications



class MyEmsAdminSite(AdminSite):

    site_title = 'PDF'
    #
    site_header ='PDF'
    #
    index_title = 'PDF'




myems_admin_site = MyEmsAdminSite()

myems_admin_site.register(User)
myems_admin_site.register(Subscription)
myems_admin_site.register(SubscriptionNotifications)

