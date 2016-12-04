from django.contrib import admin
from .models import Quote
from .models import Video
from .models import UserProfile
from .models import MapUserQuote

admin.site.register(Quote)
admin.site.register(Video)
admin.site.register(UserProfile)
admin.site.register(MapUserQuote)
