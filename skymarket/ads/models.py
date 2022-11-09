from django.db import models

from users.models import User


class Ad(models.Model):
    image = models.ImageField(upload_to='ad_photo/', null=True)
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField(max_length=600, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def author_first_name(self):
        return self.author.first_name

    @property
    def author_last_name(self):
        return self.author.last_name

    @property
    def phone(self):
        return self.author.phone


class Comment(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='comments')
    created_at = models.DateTimeField(auto_now=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments', blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.text

