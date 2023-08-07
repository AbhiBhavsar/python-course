from django.contrib import admin
import blog.models as blog_models
# Register your models here.

admin.site.register(blog_models.Post)
admin.site.register(blog_models.Author)
admin.site.register(blog_models.Tag)
