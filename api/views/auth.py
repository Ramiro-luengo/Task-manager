from typing import Type

from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, logout, login
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters

from .user import User


class LoginView(View):
    form_class: Type[AuthenticationForm] = AuthenticationForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(sensitive_post_parameters())
    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        # Is_vaild already does the authentication.
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user: User = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return JsonResponse(
                    {"message": f"Authentication succeded.", "user_id": user.id},
                    status=200,
                )
            else:
                # No backend authenticated the credentials
                return JsonResponse({"message": "Authentication Failed"}, status=404)
        else:
            return JsonResponse({"message": form.errors}, status=404)


class LogoutView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(sensitive_post_parameters())
    def post(self, request, *args, **kwargs):
        if request.user:
            logout(request)
            return JsonResponse({"message": "Logged out correctly."}, status=200)
        else:
            return JsonResponse({"message": "No user currently logged."}, status=200)
