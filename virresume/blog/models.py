from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=225)
    pub_data = models.DateTimeField()
    image = models.ImageField(upload_to='')
    body = models.TextField()
