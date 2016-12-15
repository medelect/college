from django.template.context_processors import request

def add_sett(request):
    from django.conf import settings
    return {'mysettings': settings,}

