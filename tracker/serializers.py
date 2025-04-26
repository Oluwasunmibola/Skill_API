from rest_framework import serializers
from .models import Skill, Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    progress_entries = ProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = "__all__"
        read_only_fields = ["created_at", "created_by"]