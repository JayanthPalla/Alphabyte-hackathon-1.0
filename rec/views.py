from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecruiterUserSerializer, RecruiterUserTokenSerializer
from .ml_code.main import get_job_desc_and_similarity

class RecruiterUserRegisterAPIView(APIView):
    def post(self, request):
        serializer = RecruiterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecruiterUserLoginAPIView(APIView):
    def post(self, request):
        serializer = RecruiterUserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    


