from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

# 只在自定义 User 未注册时注册
try:
    admin.site.register(User, DefaultUserAdmin)
except admin.sites.AlreadyRegistered:
    pass

admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
