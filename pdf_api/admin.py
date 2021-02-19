from django.contrib import  admin
from  django.contrib.admin import  AdminSite
from  django.utils.translation import  ungettext_lazy
from authentication.models import User
from subscription.models import Subscription,SubscriptionNotifications,SubscriptionText,FAQ
from utils.models import Contact
from translated_fields import TranslatedFieldAdmin, to_attribute
from django.utils.translation import gettext_lazy as _



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


class FAQAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    # Pack question and answer fields into their own fieldsets:
    fieldsets = [
        (_("question"), {"fields": FAQ.question.fields}),
        (_("answer"), {"fields": FAQ.answer.fields}),
    ]

    # Show all fields in the changelist:
    list_display = [
        *FAQ.question.fields,
        *FAQ.answer.fields
    ]

    # Order by current language's question field:
    def get_ordering(self, request):
        return [to_attribute("question")]

# English, Hindi, Simple-Chinese, Traditional-Chinese,
# German, French, Japanese, Korean, Spanish

myems_admin_site = MyEmsAdminSite()

myems_admin_site.register(User)
myems_admin_site.register(Subscription,SubscriptionAdmin)
myems_admin_site.register(SubscriptionNotifications)
myems_admin_site.register(Contact)



myems_admin_site.register(FAQ,FAQAdmin)

