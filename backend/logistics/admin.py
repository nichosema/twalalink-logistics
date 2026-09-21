from django.contrib import admin
from .models import (
    CustomerProfile,
    DeliveryBooking,
    StorageBooking,
)


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
        "account_type",
        "created_at",
    )


@admin.register(DeliveryBooking)
class DeliveryBookingAdmin(admin.ModelAdmin):
    list_display = (
        "tracking_number",
        "customer",
        "origin",
        "destination",
        "estimated_price",
        "status",
        "created_at",
    )

    list_filter = ("status", "created_at")
    search_fields = (
        "tracking_number",
        "origin",
        "destination",
    )


@admin.register(StorageBooking)
class StorageBookingAdmin(admin.ModelAdmin):
    list_display = (
        "booking_number",
        "customer",
        "storage_location",
        "total_price",
        "status",
        "created_at",
    )

    list_filter = ("status", "created_at")
    search_fields = (
        "booking_number",
        "storage_location",
    )
