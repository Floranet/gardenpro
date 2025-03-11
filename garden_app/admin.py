from django.contrib import admin
# Register your models here.
from.models import user_reg,Feed_user,Feed_prof,prof_reg,pay,resource
from .models import*

admin.site.register(user_reg)
admin.site.register(Feed_user)
admin.site.register(prof_reg)
admin.site.register(Feed_prof)
admin.site.register(cart)
admin.site.register(pay)
admin.site.register(resource)
admin.site.register(shop)
admin.site.register(Reminder)
admin.site.register(Task)