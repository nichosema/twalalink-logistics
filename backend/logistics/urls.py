from rest_framework.routers import DefaultRouter

from .views import (
    DeliveryBookingViewSet,
    StorageBookingViewSet,
)

router = DefaultRouter()

router.register(
    r"bookings",
    DeliveryBookingViewSet,
    basename="bookings",
)

router.register(
    r"storage",
    StorageBookingViewSet,
    basename="storage",
)

urlpatterns = router.urls