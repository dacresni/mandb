# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Function(models.Model):
    name = models.TextField(primary_key=True)
    header = models.TextField()
    class Meta:
        db_table = u'function'

class Manual(models.Model):
    name = models.TextField(primary_key=True)
    content = models.TextField()
    date = models.DateField()
    section = models.SmallIntegerField()
    whatis = models.TextField()
    class Meta:
        db_table = u'manual'
class Header(db.Model):
    name = models.TextField(required = True)
    #manuals = models.
