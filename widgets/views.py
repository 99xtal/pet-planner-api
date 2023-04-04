from rest_framework import permissions, generics
from .serializers import WidgetSerializer
from .models import Widget


class UserWidgetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WidgetSerializer

    def get_queryset(self):
        user = self.request.user
        return Widget.objects.filter(user=user)


class WidgetDetail(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer
