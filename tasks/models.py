from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ]
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ]
    description = models.CharField(max_length=255)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    
    def is_due_soon(self):
        if self.deadline:
            return (self.deadline - now().date()).days <= 1
        return False
    
    def __str__(self):
        return self.description