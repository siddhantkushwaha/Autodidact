from django.contrib import admin
from .models import *

admin.site.register(ForumUser)
admin.site.register(Tag)
admin.site.register(Thread)
admin.site.register(Answer)
admin.site.register(Comment)
