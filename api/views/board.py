from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..auth import login_required

from ..models import User, Folder, TodoItem


class BoardSerializer(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def serialize(self, board):
        folder = Folder.objects.get(board=board)
        todo_items = TodoItem.objects.filter(folder=folder)

        return JsonResponse(
            {
                "board": board.serialize(),
                "folder": folder.serialize(),
                "todo_items": list(map(lambda item: item.serialize(), todo_items)),
            },
            status=200,
        )


class BoardsView(BoardSerializer):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        user_object: User = User.objects.get(id=user.id)
        board = user_object.board
        return self.serialize(board)
