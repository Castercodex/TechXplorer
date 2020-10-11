from django.contrib import admin
from .models import  C, Cpp, JavaScript, Java, Python, Php
from embed_video.admin import  AdminVideoMixin
# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(C, MyModelAdmin)
admin.site.register(Cpp, MyModelAdmin)
admin.site.register(JavaScript, MyModelAdmin)
admin.site.register(Java, MyModelAdmin)
admin.site.register(Php, MyModelAdmin)
admin.site.register(Python, MyModelAdmin)
