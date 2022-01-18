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
    path('csrf/', views.get_csrf, name='api-csrf'),
    path('session/', views.session_view, name='api-session'),
    path('whoami/', views.whoami_view, name='api-whoami'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
]
