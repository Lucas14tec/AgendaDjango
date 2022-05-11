from django.db import models
from django.conf import settings

class Event(models.Model):
    priorities_list = (
        ('0' , 'Sem Problemas') ,
        ('1' , 'Normal')  ,
        ('2' , 'Urgente') ,
        ('3' , 'Muito Urgente') ,

    )
    autor    = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    date     = models.DateTimeField('Data')
    event    = models.CharField('Evento',max_length=80)
    priority = models.CharField('Prioridade' , max_length=1 , choices = priorities_list)
    resume   = models.CharField('Descrição do Evento', max_length = 1000)

    def __str__(self):
        return self.event

