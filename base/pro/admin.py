from django.contrib import admin
from .models import Post
from .models import info
from .models import UserProfile
admin.site.register(Post)
admin.site.register(info)
admin.site.register(UserProfile)