from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField()
    preview = models.ImageField(upload_to='image', verbose_name='Превью', blank=True, null=True)
    created_at = models.DateField(null=True)
    sign_of_publication = models.BooleanField()
    views_count = models.PositiveIntegerField(verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров", default=0)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ["heading"]

