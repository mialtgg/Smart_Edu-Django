
from django.db import models

# ,
class Course (models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name="Kurs Adı",help_text="Kurs adını yazınız")
    description = models.TextField(blank=True ,null=True)
    image =models.ImageField(upload_to="courses/%Y/%m%d/")
    avaliable = models.BooleanField(default=True)
