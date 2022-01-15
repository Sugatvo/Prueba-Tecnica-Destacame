from django.urls import path, include

from rest_framework.routers import DefaultRouter

from bus_backend import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'passengers', views.PassengerViewSet, basename='passenger')
router.register(r'drivers', views.DriverViewSet, basename='driver')
router.register(r'stations', views.StationViewSet)
router.register(r'routes', views.RouteViewSet)
router.register(r'buses', views.BusViewSet)
router.register(r'trips', views.TripViewSet)
router.register(r'tickets', views.TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
