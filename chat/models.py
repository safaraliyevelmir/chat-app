from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_sender')    
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_reciever')
    message = models.TextField()
    was_read = models.BooleanField(default=False)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.sender} to {self.receiver}"
    
    
    class Meta:
        ordering = ['created_at']
    