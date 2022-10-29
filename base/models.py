from django.db import models

# Create your models here.
class Games(models.Model):
    title=models.CharField(max_length=25)
    summary=models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        ordering= ['title',]    
        verbose_name='Games'
        verbose_name_plural='Games'
    