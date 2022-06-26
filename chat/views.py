from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Message
from django.db.models import Q
from .forms import MessageForm

User = get_user_model()

def chat(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'chat.html',context)

def chat_detail(request,username):
    users = User.objects.all()
    user = User.objects.get(username=username)
    messages = Message.objects.filter(Q(sender=user,receiver=request.user ) | Q(sender=request.user, receiver=user))
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.sender = request.user
            obj.receiver = user
            obj.save()
    context = {
        'users':users,
        'user':user,
        'messages':messages,
        'form':form,
    }
    return render(request,'chat_detail.html',context)