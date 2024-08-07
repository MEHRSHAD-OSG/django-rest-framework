from rest_framework import serializers
from . import models

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Person
#         fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    # connect a field to special method
    answers = serializers.SerializerMethodField(method_name='all_answers')
    # show client everything I want
    # show every thing in def __str__
    # here user pk is id
    user = serializers.SlugRelatedField(read_only=True,slug_field='email')

    class Meta:
        model = models.Question
        fields = '__all__'

    # obj = all questions in obj because this method in this class(questionserializer)
    def all_answers(self,obj):
        # برای گرفتن جواب ها همان سوال
        result = obj.aquestion.all()
        # we can use anserserializer because set query in result
        return AnswerSerializer(instance=result,many=True).data

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # question is foreign key in answer class model
    question = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Answer
        fields = '__all__'
    def validate_body(self,value):
        if value=='':
            raise serializers.ValidationError("body can't be empty")