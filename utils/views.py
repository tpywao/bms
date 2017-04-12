from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils.decorators import classonlymethod


class LoginRequiredViewMixin(object):
    """
    ログインが必要なViewのMixin
    """
    @classonlymethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        view = login_required(view)
        return view


class AuthedView(LoginRequiredViewMixin, View):
    pass


class AuthedTemplateView(LoginRequiredViewMixin, TemplateView):
    pass


class AuthedListView(LoginRequiredViewMixin, ListView):
    pass


class AuthedCreateView(LoginRequiredViewMixin, CreateView):
    pass


class AuthedUpdateView(LoginRequiredViewMixin, UpdateView):
    pass


class AuthedDeleteView(LoginRequiredViewMixin, DeleteView):
    pass


class AuthedDetailView(LoginRequiredViewMixin, DetailView):
    pass
