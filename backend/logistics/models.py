from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer_profile"
    )
    phone_number = models.CharField(max_length=30)
    account_type = models.CharField(
        max_length=30,
        choices=[
            ("individual", "Individual"),
            ("business", "Business"),
        ],
        default="individual"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class DeliveryBooking(models.Model):
    STATUS_CHOICES = [
        ("awaiting_payment", "Awaiting Payment"),
        ("payment_confirmed", "Payment Confirmed"),
        ("awaiting_pickup", "Awaiting Pickup"),
        ("in_transit", "In Transit"),
        ("at_destination", "At Destination"),
        ("delivered", "Delivered"),
        ("delayed", "Delayed"),
        ("cancelled", "Cancelled"),
    ]

    tracking_number = models.CharField(
        max_length=30,
        unique=True
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="delivery_bookings"
    )
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    parcel_description = models.TextField()
    weight_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    estimated_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="awaiting_payment"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_number


class StorageBooking(models.Model):
    STATUS_CHOICES = [
        ("awaiting_payment", "Awaiting Payment"),
        ("payment_confirmed", "Payment Confirmed"),
        ("in_storage", "In Storage"),
        ("ready_for_collection", "Ready for Collection"),
        ("collected", "Collected"),
        ("cancelled", "Cancelled"),
    ]

    booking_number = models.CharField(
        max_length=30,
        unique=True
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="storage_bookings"
    )
    storage_location = models.CharField(max_length=255)
    goods_description = models.TextField()
    number_of_packages = models.PositiveIntegerField()
    duration_days = models.PositiveIntegerField()
    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="awaiting_payment"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_number
