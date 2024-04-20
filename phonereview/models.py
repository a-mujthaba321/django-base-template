from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon_url = models.URLField(max_length=200, blank=True)


class Phone(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(max_length=150, default='null')

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model_name)
        super().save(*args, **kwargs)


class PhoneReview(models.Model):
    review_title = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, default='null')
    phone = models.ForeignKey(
        Phone, on_delete=models.CASCADE, related_name="reviews")

    def save(self, *args, **kwargs):
        super(PhoneReview, self).save()
        self.slug = '%i-%s' % (self.id, slugify(self.review_title))
        super().save(*args, **kwargs)
