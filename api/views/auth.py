from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters

from .user import User


class LoginView(View):
    form_class = AuthenticationForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(sensitive_post_parameters())
    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)

        # Is_vaild already does the authentication.
        if form.is_valid():
            username = form.get("username")
            password = form.get("password")

            user: User = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                return HttpResponse(f"Authentication succeded: {user.id}", status=200)
            else:
                # No backend authenticated the credentials
                return HttpResponse("Authentication Failed", status=404)

        return HttpResponse(status=404)
