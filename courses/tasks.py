from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Course

User = get_user_model()

@shared_task
def notify_teacher_enrollment(teacher_id, student_username, course_title):
    teacher = User.objects.get(id=teacher_id)
    send_mail(
        subject=f"New Enrollment: {course_title}",
        message=f"{student_username} has enrolled in your course.",
        from_email=None,
        recipient_list=[teacher.email if teacher.email else 'teacher@test.com'],
    )

@shared_task
def notify_students_new_material(course_id, material_title):
    course = Course.objects.get(id=course_id)
    student_emails = [
        s.student.email if s.student.email else 'student@test.com' 
        for s in course.enrolled_students.all()
    ]
    if student_emails:
        send_mail(
            subject=f"New Material in {course.title}",
            message=f"A new file '{material_title}' was uploaded.",
            from_email=None,
            recipient_list=student_emails,
        )