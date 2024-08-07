from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from home import serializers as home_ser
import string
class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,write_only=True,style={'input_type': 'password'})
    confirm_password = serializers.CharField(required=True,write_only=True)


    def create(self, validated_data):
        del validated_data['confirm_password']
        user = super(UserRegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_password(self,value):
        word = digit = 0
        strength = 1
        if len(value) >= 8:
            for char in value:
                if char in string.ascii_letters:
                    word += 1
                if char in string.digits:
                    digit +=1
            strength +=sum([word>=1,digit>=1])
            if strength >2:
                return value
            raise serializers.ValidationError("password is common")
        raise serializers.ValidationError("password is less than 8")

    def validate_username(self,value):
        if value == 'admin':
            raise serializers.ValidationError("username can't be `admin`")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:

            raise serializers.ValidationError("`confirm_password` is wrong")
        return data

    def validate(self,data):
        email = data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise serializers.ValidationError("this email already exists")
        return data


class ProfileViewSetSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True,max_length=None)
    # user = serializers.CharField(source='user.code',read_only=True)

    class Meta:
        model = models.Profile
        fields = ['bio', 'age', 'image']

    def create(self, validated_data):
        return models.Profile.objects.create(**validated_data)
class UserViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


