from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)  
  category = models.CharField(max_length=200)
  likes = models.IntegerField()  
      
  def __str__(self):
    return self.category + " - " +self.title
