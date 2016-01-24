from django.db import models


class Page(models.Model):
    slug = models.CharField(max_length=128)
    name = models.TextField()
    content = models.TextField()
    is_main_page = models.BooleanField(default=False)
