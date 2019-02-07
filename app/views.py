from rest_framework.response import Response
from rest_framework.views import APIView


class TestApiView(APIView):
    def get(self, request, *args, **kwargs):
        return Response("API response GET 200 OK")

    def post(self, request, *args, **kwargs):
        return Response("API response POST 200 OK")