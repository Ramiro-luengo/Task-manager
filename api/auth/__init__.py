from functools import wraps

from django.http import JsonResponse


def login_required(view_func):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """

    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"message": "No user authenticated."}, status=404)
        return view_func(request, *args, **kwargs)

    return wraps(view_func)(wrapped_view)
