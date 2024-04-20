from django.contrib import admin
from .models import Brand, Phone, PhoneReview

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'brand')


class PhoneReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'review_title', 'review_text')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneReview, PhoneReviewAdmin)
