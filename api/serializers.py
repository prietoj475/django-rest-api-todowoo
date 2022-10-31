from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datacompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id','title','memo','created','datacompleted','important']

class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','memo','created','datacompleted','important']

