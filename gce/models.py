from django.db import models

# Create your models here.
class songs(models.Model) :
    name = models.CharField(max_length = 100, default= 'NULL')
    artist = models.CharField(max_length = 100, default= 'NULL')
    img = models.ImageField(upload_to = 'pics', default = 'JAAN NISAAR.jpg')
    genre = models.CharField(max_length = 100, default= 'NULL')
    song = models.FileField(upload_to='audios', default= 'zaalima lofi.mp3')
    
    