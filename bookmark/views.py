from django.views.generic import ListView

from .models import Bookmark


class Index(ListView):
    model = Bookmark
