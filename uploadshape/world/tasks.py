import json
from osgeo import ogr
from osgeo import osr
from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings
from celery import shared_task

from .models import UploadedFile, Shapefile, Geometry


@shared_task
def save_data(files):
    pks = json.loads(files)
    files = UploadedFile.objects.filter(pk__in=pks)
    for file in files:
        shapefile, created = Shapefile.objects.get_or_create(
            name=file.filename().split('.')[0]
        )
        shapefile_ogr = ogr.Open(settings.PUBLIC_DIR + file.document.url)
        layer = shapefile_ogr.GetLayer(0)
        crs = layer.GetSpatialRef()
        srid = crs.GetAttrValue('AUTHORITY', 1)
        print(srid)
        if srid == '4326':
            for i in range(layer.GetFeatureCount()):
                feature = layer.GetFeature(i)
                geometry = feature.GetGeometryRef()
                data = GEOSGeometry(geometry.ExportToJson())
                saved = Geometry(geom=data, shapefile=shapefile)
                saved.save()
        return 'geometries uploaded with success!'



# @shared_task
# def save_data(files):
#     pks = json.loads(files)
#     files = UploadedFile.objects.filter(pk__in=pks)
#     for file in files:
#         shapefile, created = Shapefile.objects.get_or_create(
#             name=file.filename().split('.')[0]
#         )
#         shapefile_ogr = ogr.Open(settings.PUBLIC_DIR + file.document.url)
#         layer = shapefile_ogr.GetLayer(0)
#         crs = layer.GetSpatialRef()
#         srid = crs.GetAttrValue('AUTHORITY', 1)
#         for i in range(layer.GetFeatureCount()):
#             feature = layer.GetFeature(i)
#             geometry = feature.GetGeometryRef()
#             data = GEOSGeometry(geometry.ExportToJson())
#             saved = Geometry(geom=data, shapefile=shapefile)
#             saved.save()
#         return 'geometries uploaded with success!'
