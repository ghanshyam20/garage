from django.urls import path
from . import views_dashboard as dashboard

urlpatterns = [
    path('', dashboard.DashboardHomeView.as_view(), name='dashboard_home'),

    path('services/', dashboard.ServiceListView.as_view(), name='dashboard_service_list'),
    path('services/create/', dashboard.ServiceCreateView.as_view(), name='dashboard_service_create'),
    path('services/<int:pk>/edit/', dashboard.ServiceUpdateView.as_view(), name='dashboard_service_update'),
    path('services/<int:pk>/delete/', dashboard.ServiceDeleteView.as_view(), name='dashboard_service_delete'),

    path('testimonials/', dashboard.TestimonialListView.as_view(), name='dashboard_testimonial_list'),
    path('testimonials/create/', dashboard.TestimonialCreateView.as_view(), name='dashboard_testimonial_create'),
    path('testimonials/<int:pk>/edit/', dashboard.TestimonialUpdateView.as_view(), name='dashboard_testimonial_update'),
    path('testimonials/<int:pk>/delete/', dashboard.TestimonialDeleteView.as_view(), name='dashboard_testimonial_delete'),

    path('contact/', dashboard.ContactInfoUpdateView.as_view(), name='dashboard_contact'),
    path('about/', dashboard.AboutPageUpdateView.as_view(), name='dashboard_about'),
    path('bookings/', dashboard.BookingListView.as_view(), name='dashboard_bookings'),
]
