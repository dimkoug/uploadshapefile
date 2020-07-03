from django.conf import settings


def get_data(request):
    return {
        'google_maps_key': settings.GOOGLE_MAPS_KEY
    }
