from django.contrib import admin
from .models import profiles
from.models import skills
from.models import accounts
# Register your models here.

admin.site.register(profiles)
admin.site.register(skills)
admin.site.register(accounts)