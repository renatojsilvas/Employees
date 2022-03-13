from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=255)
    department = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'employees'
        verbose_name = 'empregado'
        verbose_name_plural = 'empregados'
    
    def __str__(self):
        return self.name
