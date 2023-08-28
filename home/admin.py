from django.contrib import admin
from home.models import Release, Subscriber, Quote, Event, Video, Artist






admin.site.site_header= "untitled.np"
admin.site.register(Release)
admin.site.register(Subscriber)
admin.site.register(Quote)
admin.site.register(Event)
admin.site.register(Video)
admin.site.register(Artist)