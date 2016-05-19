# sprinles/views.py

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .utils import check_sprinkles
from .models import Sprinkle


def sprinkle_list(request):
    '''Standard list view'''
    request = check_sprinkles(request)

    return render(
        request, "sprinkles/sprinkle_list.html",
        {"sprinkle": Sprinkle.objects.all()}
    )


def sprinkle_detail(request, pk):
    '''Standard detail view'''
    request = check_sprinkles(request)
    sprinkle = get_object_or_404(Sprinkle, pk=pk)

    return render(
        request, "sprinkles/sprinkle_detail.html",
        {"sprinkle": sprinkle})
