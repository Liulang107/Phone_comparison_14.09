from django.db import models

# Create your models here.
class Phone(models.Model):
    model = models.CharField('Модель телефона', max_length=50)
    price = models.CharField('Цена', max_length=30)
    camera = models.FloatField('Разрешение камеры')
    operating_system = models.CharField('Операционная система', max_length=50)
    ram = models.IntegerField('Оперативная память')

    class Meta:
        abstract = True

class Apple(Phone):
    wireless_charging = models.BooleanField('Беспроводная зарядка')

class Samsung(Phone):
    micro_sd = models.BooleanField('MicroSD')

class Meizu(Phone):
    irda = models.BooleanField('Инфракрасный порт')
