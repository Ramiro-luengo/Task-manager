import logging
from typing import Type

from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm

from .user import User

logger = logging.getLogger(__name__)


class LoginView(APIView):
    form_class: Type[AuthenticationForm] = AuthenticationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.data)

        if form.is_valid():
            username = request.data.get("username")
            password = request.data.get("password")

            user: User = authenticate(username=username, password=password)
            if user is not None:
                # Backend authenticated credentials
                login(request, user)
                return JsonResponse(
                    {"message": f"Authentication succeded.", "user_id": user.id},
                    status=200,
                )
            else:
                # No backend authenticated the credentials
                return JsonResponse({"message": "Authentication Failed"}, status=404)
        else:
            error_messages = form.errors.get("__all__")
            logger.debug(f"Login failed: {error_messages}")
            return JsonResponse({"message": form.errors.get("__all__")}, status=404)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        if request.user:
            logout(request)
            return JsonResponse({"message": "Logged out correctly."}, status=200)
        else:
            err_message = "No user currently logged."
            logger.debug(err_message)
            return JsonResponse({"message": err_message}, status=200)
