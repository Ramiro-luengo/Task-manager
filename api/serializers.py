from rest_framework import serializers

# from rest_framework.utils import field_mapping
from .models import Board, Folder, Tags, TodoItem


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["name"]


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ["name", "created_at", "description"]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["name"]


class TodoItemSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = TodoItem
        fields = ["name", "created_at", "description", "tags"]
