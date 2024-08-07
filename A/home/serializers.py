from rest_framework import serializers
from . import models


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(method_name='all_answers')
    user = serializers.SlugRelatedField(read_only=True,slug_field='email')

    class Meta:
        model = models.Question
        fields = '__all__'

    
    def all_answers(self,obj):
        result = obj.aquestion.all()
        return AnswerSerializer(instance=result,many=True).data

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    question = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Answer
        fields = '__all__'
