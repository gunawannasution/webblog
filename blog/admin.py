from django.contrib import admin
from .models import Post
from django.db import models as django_models
from django_ckeditor_5.widgets import CKEditor5Widget

# Register your models here.
# buat slug
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    # Menghubungkan langsung widget CKEditor ke area TextField

    formfield_overrides = {
        django_models.TextField: {"widget": CKEditor5Widget(config_name="default")},
    }
admin.site.register(Post,PostAdmin)
