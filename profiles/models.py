from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    """
    This model represents profile each user 
    including those registred by OAuth system.
    """
    user = models.OneToOneField(User, verbose_name='Профиль пользователя', on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=200)
    last_name = models.CharField('Фамилия', max_length=200)
    patronymic = models.CharField('Отчество', max_length=200, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m/%d/', verbose_name='Аватар', default='avatar.png')
    bio = models.TextField('Информация о себе', blank=True)

    def __str__(self):
        return f'Пользователь: {self.user} {self.last_name} {self.first_name}' 

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Профиль' 
        verbose_name_plural = 'Профили'
        ordering = ['last_name']