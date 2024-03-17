from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import RecruiterUser


class RecruiterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = RecruiterUser
        fields = ('id', 'email', 'password')

    def create(self, validated_data):
        user = RecruiterUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class RecruiterUserTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = RecruiterUser.objects.filter(email=email).first()
            if user:
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    return {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                else:
                    raise serializers.ValidationError("Incorrect password.")
            else:
                raise serializers.ValidationError("User does not exist.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")
