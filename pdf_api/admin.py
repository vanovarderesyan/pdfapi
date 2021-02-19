from django.contrib import  admin
from  django.contrib.admin import  AdminSite
from  django.utils.translation import  ungettext_lazy
from authentication.models import User
from subscription.models import Subscription,SubscriptionNotifications,SubscriptionText,FAQ
from utils.models import Contact



class MyEmsAdminSite(AdminSite):

    site_title = 'PDF'
    #
    site_header ='PDF'
    #
    index_title = 'PDF'


class SubscriptionTextAdminInline(admin.TabularInline):
    model = SubscriptionText

class SubscriptionAdmin(admin.ModelAdmin):
    inlines = (SubscriptionTextAdminInline, )



myems_admin_site = MyEmsAdminSite()

myems_admin_site.register(User)
myems_admin_site.register(Subscription,SubscriptionAdmin)
myems_admin_site.register(SubscriptionNotifications)
myems_admin_site.register(Contact)
myems_admin_site.register(FAQ)



