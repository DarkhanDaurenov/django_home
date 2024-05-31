from django.db import models

NULLABLE_FIELDS = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='url_адрес')
    description = models.TextField(verbose_name='содержимое')
    picture = models.ImageField(upload_to='goods_images/', verbose_name='фото товара', **NULLABLE_FIELDS)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='активность')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} - {self.description} - {self.picture}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

