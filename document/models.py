from django.db import models
from django.db.models import Q
from datetime import datetime
# Create your models here.
class DocumentLiveManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        today = datetime.today()
        queryset = queryset.filter(Q(is_enabled=True) & Q(created_date__date=today))
        return queryset


class Document(models.Model):
    title = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/')
    is_enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()  
    live = DocumentLiveManager()  
    
    def __str__(self):
        return f"{self.id}.{self.title}:{self.upload}"
