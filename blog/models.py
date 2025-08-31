from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(blank=True, upload_to='photos/', verbose_name='Превью')
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True, blank=False)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['title']
