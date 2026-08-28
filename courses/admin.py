from django.contrib import admin

# Register your models here.
from .models import Course, Enrollment, Material, Feedback

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Material)
admin.site.register(Feedback)