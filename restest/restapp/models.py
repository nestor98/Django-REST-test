from django.db import models

# Create your models here.



class Song(models.Model):
    #album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
