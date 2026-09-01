from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment, Material, Feedback
from .forms import CourseForm, MaterialForm, FeedbackForm

# Create your views here.

@login_required
def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    # this is to handle course creation by teachers
    if request.method == 'POST' and request.user.is_teacher:
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            messages.success(request, "Course created successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()

    context = {
        'courses': courses,
        'form': form
    }
    return render(request, 'courses/course_list.html', context)

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    
    # this is to handle student enrollment in the course
    if request.method == 'POST' and 'enroll' in request.POST:
        if request.user.is_student and not is_enrolled:
            Enrollment.objects.create(student=request.user, course=course)
            messages.success(request, "Successfully enrolled!")
            return redirect('course_detail', course_id=course.id)

    context = {
        'course': course,
        'is_enrolled': is_enrolled,
        'materials': course.materials.all(),
        'feedbacks': course.feedback.all(),
    }
    return render(request, 'courses/course_detail.html', context)