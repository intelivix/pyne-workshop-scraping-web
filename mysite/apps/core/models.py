from django.db import models


class Exemplo(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        verbose_name = "Exemplo"
        verbose_name_plural = "Exemplos"

    def __str__(self):
        return f'{self.name} {self.age}'
