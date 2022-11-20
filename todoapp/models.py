from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    compeleted = models.BooleanField(default=False)
    
    #displays title in admin
    def __str__(self):
        return self.title