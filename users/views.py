from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import StatusUpdate, User

@login_required
def dashboard(request):
    # Handle submitting a new status update
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            StatusUpdate.objects.create(user=request.user, content=content)
            return redirect('dashboard')

    # Fetch status updates for the feed
    updates = StatusUpdate.objects.all().order_by('-created_at')
    
    context = {
        'updates': updates,
        'user': request.user
    }
    return render(request, 'users/dashboard.html', context)