from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollment, Material
from .tasks import notify_teacher_enrollment, notify_students_new_material

@receiver(post_save, sender=Enrollment)
def enrollment_created(sender, instance, created, **kwargs):
    if created:
        notify_teacher_enrollment.delay(
            instance.course.teacher.id, 
            instance.student.username, 
            instance.course.title
        )

@receiver(post_save, sender=Material)
def material_created(sender, instance, created, **kwargs):
    if created:
        notify_students_new_material.delay(
            instance.course.id, 
            instance.title
        )