from django.db import models

from cloud_project.storage_backends import StaticStorage

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
