from django.urls import path
from bus_backend import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('stations/',
         views.StationList.as_view(),
         name="station-list"),
    path('stations/<int:pk>/',
         views.StationDetail.as_view(),
         name="station-detail"),
    path('routes/',
         views.RouteList.as_view(),
         name="route-list"),
    path('routes/<int:pk>/',
         views.RouteDetail.as_view(),
         name="route-detail"),
    path('buses/',
         views.BusList.as_view(),
         name="bus-list"),
    path('buses/<int:pk>/',
         views.BusDetail.as_view(),
         name="bus-detail"),
    path('seats/',
         views.SeatList.as_view(),
         name="seat-list"),
    path('seats/<int:pk>/',
         views.SeatDetail.as_view(),
         name="seat-detail"),
    path('trips/',
         views.TripList.as_view(),
         name="trip-list"),
    path('trips/<int:pk>/',
         views.TripDetail.as_view(),
         name="trip-detail"),
    path('tickets/',
         views.TicketList.as_view(),
         name="ticket-list"),
    path('tickets/<int:pk>/',
         views.TicketDetail.as_view(),
         name="ticket-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
