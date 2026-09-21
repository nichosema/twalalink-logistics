from rest_framework import serializers
from .models import DeliveryBooking, StorageBooking


class DeliveryBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBooking
        fields = "__all__"
        read_only_fields = [
            "tracking_number",
            "created_at",
            "updated_at",
        ]


class StorageBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageBooking
        fields = "__all__"
        read_only_fields = [
            "booking_number",
            "created_at",
        ]