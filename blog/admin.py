from django.contrib import admin
from .models import blogpost, CommentModel,ProfileModel

# Register your models here.
admin.site.register(blogpost)
admin.site.register(CommentModel)
admin.site.register(ProfileModel)