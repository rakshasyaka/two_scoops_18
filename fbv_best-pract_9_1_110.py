# sprinkles/utils.py

from django.core.exceptions import PermissionDenied


def check_sprinkle_rights(request):
    if request.user.can_sprinkle or request.user.is_staff:
        return request
    raise PermissionDenied


def check_sprinkles(request):
    if request.user.can_sprinkle or request.user.is_staff:
        request.can_sprinkle = True
        return request

    raise PermissionDenied
