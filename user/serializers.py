from .models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=30, required=False)

    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname', '')
        user.save(update_fields=['nickname'])

    # register 요청에 대한 응답 Json 에 nickname 정보를 담기 위한 코드
    # dj_rest_auth 의 RegisterSerializer 에는 to_representation 이 없다.
    # dj_rest_auth 가 상속 받은 rest_framework.serializers 에 이 method 가 있다. 필요시 구현 하도록 하겠다.
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['nickname'] = self.validated_data.get('nickname', '')
        data.update({
            "nickname": self.validated_data.get('nickname', '')
        })
        return data

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            "nickname": self.validated_data.get('nickname', '')
        }
