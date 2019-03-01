from django.contrib import admin
from .models import User, TutorProfiles, GuardianProfiles

# Register your models here.
admin.site.register(User)
admin.site.register(TutorProfiles)
admin.site.register(GuardianProfiles)
