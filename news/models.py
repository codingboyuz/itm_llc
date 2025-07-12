from django.db import models
from shared.models import BaseModel
from django.utils.text import slugify
from slugify import slugify


class NewsModel(BaseModel):  # ← Meros olayapti
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
# slug avrtomatik qilindi
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    

class NewsImages(models.Model):
    news = models.ForeignKey(NewsModel,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField("media/news/",blank=True,null=True)


