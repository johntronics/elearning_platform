from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import StatusUpdate, User
from chat.models import Message  

@login_required
def dashboard(request):
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            StatusUpdate.objects.create(user=request.user, content=content)
            return redirect('dashboard')

    
    updates = StatusUpdate.objects.all().order_by('-created_at')
    
    
    
    chat_history = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('-timestamp')
    
    
    recent_chats = []
    seen_users = set()
    for msg in chat_history:
        other_user = msg.sender if msg.receiver == request.user else msg.receiver
        if other_user not in seen_users:
            seen_users.add(other_user)
            recent_chats.append(other_user)
            
    context = {
        'updates': updates,
        'user': request.user,
        'recent_chats': recent_chats  
    }
    return render(request, 'users/dashboard.html', context)