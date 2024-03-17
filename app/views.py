from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ApplicantUserSerializer, ApplicantUserTokenSerializer,ApplicantUserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsApplicantUser

class ApplicantUserRegisterAPIView(APIView):
    def post(self, request):
        print('-->',request.data)
        request.data['resume_file_path'] = request.data['resume_file_path'].replace('//','\\')
        serializer = ApplicantUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicantUserLoginAPIView(APIView):
    def post(self, request):
        serializer = ApplicantUserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    

class DoSomething(APIView):
    permission_classes = [IsAuthenticated, IsApplicantUser]
