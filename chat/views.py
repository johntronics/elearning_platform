from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message

# Create your views here.

User = get_user_model()

@login_required
def chat_room(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    
    # So I can fetch previous message history between these two users
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')

    context = {
        'other_user': other_user,
        'chat_messages': messages
    }
    return render(request, 'chat/room.html', context)