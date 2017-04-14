from django.views.generic import ListView

from .models import Tag


class Index(ListView):
    model = Tag
