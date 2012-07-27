from django.db import models

class Function(models.Model):
    name = models.TextField(primary_key=True)
    

class Manual(models.Model):
    name = models.TextField(primary_key=True)
    content = models.TextField()
    date = models.DateField()
    section = models.SmallIntegerField( default=2)
    whatis = models.TextField()
    header = models.ForeignKey('Header')
    
class Header(models.Model):
    name = models.TextField(primary_key=True)
