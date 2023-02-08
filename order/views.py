from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'request': self.request,
            'user': self.request.user
        }

