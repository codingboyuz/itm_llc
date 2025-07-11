from django.db import models
from shared.models import BaseModel




class AboutModel(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    


class AboutImage(models.Model):
    about = models.ForeignKey(AboutModel,related_name="image",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/about/',null=True,blank=True)

    def __str__(self) -> str:
        return f'Image for {self.about.title}'


class CertificateModel(models.Model):
    image = models.ImageField(upload_to='media/about/',null=True,blank=True)