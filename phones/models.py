from django.db import models

# Create your models here.
class Phone(models.Model):
    model = models.CharField('Модель телефона', max_length=50)
    price = models.CharField('Цена', max_length=30)
    camera = models.FloatField('Разрешение камеры')
    operating_system = models.CharField('Операционная система', max_length=50)
    ram = models.IntegerField('Оперативная память')

class Apple(models.Model):
    wireless_charging = models.BooleanField('Беспроводная зарядка')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

class Samsung(models.Model):
    micro_sd = models.BooleanField('MicroSD')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

class Meizu(models.Model):
    irda = models.BooleanField('Инфракрасный порт')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)