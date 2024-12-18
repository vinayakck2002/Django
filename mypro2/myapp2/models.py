from django.db import models

# Create your models here.
class ImgForm(models.Model):
    main_image=models.ImageField(upload_to='images/')
