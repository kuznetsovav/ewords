from django.contrib import admin
from .models import Quote
from .models import Video
from .models import UserProfile

admin.site.register(Quote)
admin.site.register(Video)
admin.site.register(UserProfile)
