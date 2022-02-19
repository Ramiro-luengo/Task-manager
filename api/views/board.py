from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import User, Folder, TodoItem
from ..serializers import BoardSerializer, FolderSerializer, TodoItemSerializer


class BoardsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        board = user.board
        folder = Folder.objects.filter(board=board)
        todo_items = TodoItem.objects.filter(folder__in=folder)
        return JsonResponse(
            {
                "board": BoardSerializer(board).data,
                "folders": FolderSerializer(folder, many=True).data,
                "todoItems": TodoItemSerializer(todo_items, many=True).data,
            },
            safe=False,
        )

    # def post(self, request, *args, **kwargs):
    #     data = JSONParser().parse(request)
    #     serializer = BoardSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
