from django import forms
from .models import Course, Material, Feedback

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'file']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Leave your feedback...'}),
        }