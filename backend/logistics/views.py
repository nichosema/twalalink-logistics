import uuid

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import DeliveryBooking, StorageBooking
from .serializers import (
    DeliveryBookingSerializer,
    StorageBookingSerializer,
)


class DeliveryBookingViewSet(viewsets.ModelViewSet):
    queryset = DeliveryBooking.objects.all().order_by("-created_at")
    serializer_class = DeliveryBookingSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        tracking_number = f"TW-{uuid.uuid4().hex[:8].upper()}"

        serializer.save(
            tracking_number=tracking_number,
            status="payment_confirmed",
        )


class StorageBookingViewSet(viewsets.ModelViewSet):
    queryset = StorageBooking.objects.all().order_by("-created_at")
    serializer_class = StorageBookingSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        booking_number = f"ST-{uuid.uuid4().hex[:8].upper()}"

        serializer.save(
            booking_number=booking_number,
            status="payment_confirmed",
        )