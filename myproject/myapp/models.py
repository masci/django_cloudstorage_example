# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def delete(self, *args, **kwargs):
            # You have to prepare what you need before delete the model
            storage, path = self.docfile.storage, self.docfile.path
            # Delete the model before the file
            super(Document, self).delete(*args, **kwargs)
            # Delete the file after the model
            storage.delete(path)
