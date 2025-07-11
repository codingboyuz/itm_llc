from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Avtomatik yaratilgan sana
    updated_at = models.DateTimeField(auto_now=True)      # Har safar yangilangan sana
    is_active = models.BooleanField(default=True)         # Soft delete uchun

    deleted_at = models.DateTimeField(null=True, blank=True)  # Yaxshisi default bermaslik




    class Meta:
        abstract = True
        ordering = ['-created_at']


    def delete(self, using=None, keep_parents=False):
        """
        Soft delete — ma'lumotni bazadan o‘chirmaydi, faqat is_active ni False qiladi
        """
        self.is_active = False
        self.save()

    def hard_delete(self, using=None, keep_parents=False):
        """
        Haqiqiy o‘chirish — bazadan butunlay yo‘qotadi
        """
        super().delete(using=using, keep_parents=keep_parents)
    def restore(self):
        self.is_active = True
        self.deleted_at = None
        self.save()

