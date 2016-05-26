# example 10.2
# example 10.3
# example 10.4
from django.views.generic import DetailView
from django.views.generic import CreateView

from braces.views import LoginRequiredMixin

from .models import Flavor


class FlavorDetailView(LoginRequiredMixin, DetailView):
    model = Flavor


class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

    def form_valid(self, form):
        # Do custom logic here
        return super(FlavorCreateView, self).form_valid(form)

    def form_invalid(self, form):
        # Do custom logic here
        return super(FlavorCreateView, self).form_invalid(form)
