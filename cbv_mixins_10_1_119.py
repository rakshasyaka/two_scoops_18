# example 10.1
from django.views.generic import TemplateView


class FreshFruitMixin(object):

    def get_context_data(self, **kwargs):
        context = super(
            FreshFruitMixin, self).get_context_data(**kwargs)
        context["has_fresh_fruit"] = True
        return context


class FruityFlavorView(FreshFruitMixin, TemplateView):
    template_name = "fruity_flavor.html"
