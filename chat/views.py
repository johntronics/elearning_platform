from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

@login_required
def chat_room(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    
  
    room_name = f"chat_{min(request.user.id, other_user.id)}_{max(request.user.id, other_user.id)}"
    

    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')

    context = {
        'other_user': other_user,
        'chat_messages': messages,
        'room_name': room_name 
    }
    return render(request, 'chat/room.html', context)