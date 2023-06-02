from rest_framework import serializers
from .models import *
class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ques
        fields= ["task", "completed", "timestamp", "updated", "user"]