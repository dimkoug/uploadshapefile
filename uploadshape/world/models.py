import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.gis.db import models
from django.urls import reverse


class UploadedFile(models.Model):
    document = models.FileField(upload_to='shapefile/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.document.name)


class Shapefile(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        default_related_name = 'shapefiles'
        verbose_name = 'shapefile'
        verbose_name_plural = 'shapefiles'

    def __str__(self):
        return self.name

class Geometry(models.Model):
    shapefile = models.ForeignKey(Shapefile, on_delete=models.CASCADE)
    geom = models.GeometryField(srid=4326)

    class Meta:
        default_related_name = 'geometries'
        verbose_name = 'geometry'
        verbose_name_plural = 'geometries'

    def __str__(self):
        return self.geom



@receiver(post_delete, sender=UploadedFile)
def submission_delete(sender, instance, **kwargs):
    instance.document.delete(False)
