from django.http import HttpResponse
from django.views import View

from ..models.user import User


class UsersView(View):
    def get(self, request, *args, **kwargs):
        requested_user_id = kwargs.get("id")
        if requested_user_id:
            try:
                user = User.objects.get(id=requested_user_id)
            except User.DoesNotExist:
                return HttpResponse(
                    f"<h1>User with id:{requested_user_id} doesn't exist!</h1>",
                    status=404,
                )

            return HttpResponse(f"<h1>User: {user.username}</h1>", status=200)

        users = User.objects.all()
        users_html = "Users: "
        if users:
            users_html += (
                "<ul>"
                + "".join([f"<li>{user.username}</li>" for user in users])
                + "</ul>"
            )
        else:
            users_html += str(None)

        return HttpResponse(users_html)
