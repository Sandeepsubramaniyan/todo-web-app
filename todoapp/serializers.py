from rest_framework import serializers
from .models import Todo

#Converting the model instances to JSON to work with frontend
class TodoSerializer(serializers.ModelSerializers):
    class Meta:
        model = Todo
        fields = '__all__'