# sprinkles/decorators.py
from functools import wraps

from . import utils


def check_spinkles(view_func):
    """check if a user can add sprinkles"""
    @wraps(view_func)
    def new_view_func(reques, *args, **kwargs):
        # act on the request object with utils.can.sprinkle()
        request = utils.can_sprinkle(request)
        # call the view function
        response = view_func(request, *args, **kwargs)
        # return the HttpResponse object
        return response
    return new_view_func


# example 9.7
# views.py

from django.shortcuts import get_object_or_404, render

from .decorators import check_spinkles
from .models import Sprinkle


# attach the decorator to the view
@check_spinkles
def sprinkle_detail(request, pk):
    '''standard detail view'''
    sprinkle = get_object_or_404(Sprinkle, pk=pk)
    return render(
        request, "sprinkles/sprinkle_detail.html",
        {"sprinkle": sprinkle})
