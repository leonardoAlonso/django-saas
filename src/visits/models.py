from django.db import models

# Create your models here.

class PageVisit(models.Model):
    # db_table = 'page_visit'
    # id -> hidden -> autoField -> primary key -> auto increment
    path = models.TextField(blank=True, null=True) # column
    timestamp =  models.DateTimeField(auto_now_add=True) # column
