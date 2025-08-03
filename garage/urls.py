from django.urls import path
from .views_dashboard import (
    DashboardHomeView,
    ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView,
    TestimonialListView, TestimonialCreateView, TestimonialUpdateView, TestimonialDeleteView,
    ContactInfoUpdateView, AboutPageUpdateView, BookingListView,
)

urlpatterns = [
    path('dashboard/', DashboardHomeView.as_view(), name='dashboard_home'),

    # Services
    path('dashboard/services/', ServiceListView.as_view(), name='dashboard_service_list'),
    path('dashboard/services/create/', ServiceCreateView.as_view(), name='dashboard_service_create'),
    path('dashboard/services/<int:pk>/edit/', ServiceUpdateView.as_view(), name='dashboard_service_update'),
    path('dashboard/services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='dashboard_service_delete'),

    # Testimonials
    path('dashboard/testimonials/', TestimonialListView.as_view(), name='dashboard_testimonial_list'),
    path('dashboard/testimonials/create/', TestimonialCreateView.as_view(), name='dashboard_testimonial_create'),
    path('dashboard/testimonials/<int:pk>/edit/', TestimonialUpdateView.as_view(), name='dashboard_testimonial_update'),
    path('dashboard/testimonials/<int:pk>/delete/', TestimonialDeleteView.as_view(), name='dashboard_testimonial_delete'),

    # Contact and About
    path('dashboard/contact/', ContactInfoUpdateView.as_view(), name='dashboard_contact'),
    path('dashboard/about/', AboutPageUpdateView.as_view(), name='dashboard_about'),

    # Bookings
    path('dashboard/bookings/', BookingListView.as_view(), name='dashboard_bookings'),
]
