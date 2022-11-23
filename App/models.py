from django.db import models
# from django.contrib.auth.models import






class Profile(models.Model):
    name = models.CharField('Имя', max_length=250)
    Email = models.EmailField()
    password = models.CharField('Пароль', max_length=10)




    def str(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
