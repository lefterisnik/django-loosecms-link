from django.http import Http404, HttpResponseRedirect
from .models import Link


def link(request, category_slug, slug):
    try:
        obj = Link.objects.get(category__slug=category_slug, slug=slug)
        return HttpResponseRedirect(obj.url)
    except Link.DoesNotExist:
        raise Http404


