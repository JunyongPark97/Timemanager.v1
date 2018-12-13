from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from jandi.serializers import JandiSerializer


class JandiAPIView(APIView):

    serializer_class = JandiSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        return Response()
