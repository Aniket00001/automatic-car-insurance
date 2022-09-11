from django.db import models
import os, uuid
from django.utils.deconstruct import deconstructible

@deconstructible
class file_prefix(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1] # PDF if you want
        filename = "%s.%s" % (self.prefix, ext)
        return os.path.join('documents',filename)


class Documents(models.Model):
    
    document  = models.FileField(upload_to=file_prefix('doc'))
    document1 = models.FileField(upload_to=file_prefix('doc1'))
    document2 = models.FileField(upload_to=file_prefix('doc2'))
    document3 = models.FileField(upload_to=file_prefix('doc3'))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.timestamp