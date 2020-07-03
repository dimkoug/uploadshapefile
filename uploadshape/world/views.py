import json
from django.core.serializers import serialize
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy

from .models import UploadedFile, Shapefile, Geometry

from .tasks import save_data

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['geometries'] = Geometry.objects.all().count()
        context['shapefiles'] = Shapefile.objects.all().count()
        return context


def upload_shape(request):
    files_pk = []
    UploadedFile.objects.all().delete()
    if 'shape' in request.FILES:
        files = request.FILES.getlist('shape')
        for f in files:
            uploaded = UploadedFile(document=f)
            uploaded.save()
            files_pk.append(uploaded.pk)
        save_data.delay(files=json.dumps(files_pk))
    return HttpResponseRedirect(reverse_lazy('home'))


def get_geo(request):
    data_list = Geometry.objects.all().order_by('id').last()
    data = serialize('geojson',
                     [data_list], geometry_field='geom')
    print(data)
    return HttpResponse(data, content_type='application/json')
