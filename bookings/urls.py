from django.urls import path
from .views import BookingCreateView, BookingListView, BookingDetailView

app_name = 'bookings'

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='create'),
    path('list/', BookingListView.as_view(), name='list'),
    path('detail/<int:pk>/', BookingDetailView.as_view(), name='detail'),
]
