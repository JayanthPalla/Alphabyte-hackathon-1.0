from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ApplicantUser

class ApplicantUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ApplicantUser
        fields = '__all__'
    #     fields = ('id', 'email', 'password')

    # def create(self, validated_data):
    #     user = ApplicantUser.objects.create_user(
    #         email=validated_data['email'],
    #         password=validated_data['password']
    #     )
    #     return user
    
    
class ApplicantUserRegistrationSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    class Meta:
        model = ApplicantUser
        fields = ('id', 'email', 'password', 'file')

    def create(self, validated_data):
        file = validated_data.pop('file', None)
        user = ApplicantUser.objects.create_user(**validated_data)
        if file:
            # Save the file to a specific folder
            file_path = './resumes/' + file.name
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # Save the file path to the database
            user.file_path = file_path
            user.save()
        return user

class ApplicantUserTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = ApplicantUser.objects.filter(email=email).first()
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
