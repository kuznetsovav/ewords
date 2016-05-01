from django.contrib import admin
from .models import MainQuote
from .models import Quote

admin.site.register(MainQuote)
admin.site.register(Quote)
