from django.contrib import admin
from .models import Apple, Samsung, Meizu

# Register your models here.
@admin.register(Apple)
class AppleAdmin(admin.ModelAdmin):
    pass

@admin.register(Samsung)
class SamsungAdmin(admin.ModelAdmin):
    pass

@admin.register(Meizu)
class MeizuAdmin(admin.ModelAdmin):
    pass