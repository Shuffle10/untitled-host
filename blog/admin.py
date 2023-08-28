from django.contrib import admin
from blog.models import Blog




class BlogAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/admin.js',)


admin.site.register(Blog, BlogAdmin)