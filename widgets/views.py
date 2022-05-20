from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WidgetSerializer
from .models import Widget

class UserWidgetList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = self.request.user
        queryset = Widget.objects.filter(user=user)
        serializer = WidgetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WidgetSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class WidgetDetail(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer
    