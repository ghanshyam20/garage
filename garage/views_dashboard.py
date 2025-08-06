from __future__ import annotations
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Service, Testimonial, ContactInfo, AboutPage, Booking
from .forms_dashboard import ServiceForm, TestimonialForm, ContactInfoForm, AboutPageForm


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin that restricts access to staff or superusers."""

    def test_func(self) -> bool:
        user = self.request.user
        return user.is_authenticated and (user.is_staff or user.is_superuser)


class DashboardHomeView(StaffRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['service_count'] = Service.objects.count()
        context['testimonial_count'] = Testimonial.objects.count()
        context['booking_count'] = Booking.objects.count()
        return context


# Service views
class ServiceListView(StaffRequiredMixin, ListView):
    model = Service
    template_name = 'dashboard/service_list.html'
    context_object_name = 'services'


class ServiceCreateView(StaffRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/service_form.html'
    success_url = reverse_lazy('dashboard_service_list')


class ServiceUpdateView(StaffRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/service_form.html'
    success_url = reverse_lazy('dashboard_service_list')


class ServiceDeleteView(StaffRequiredMixin, DeleteView):
    model = Service
    template_name = 'dashboard/service_confirm_delete.html'
    success_url = reverse_lazy('dashboard_service_list')


# Testimonial views
class TestimonialListView(StaffRequiredMixin, ListView):
    model = Testimonial
    template_name = 'dashboard/testimonial_list.html'
    context_object_name = 'testimonials'


class TestimonialCreateView(StaffRequiredMixin, CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'dashboard/testimonial_form.html'
    success_url = reverse_lazy('dashboard_testimonial_list')


class TestimonialUpdateView(StaffRequiredMixin, UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'dashboard/testimonial_form.html'
    success_url = reverse_lazy('dashboard_testimonial_list')


class TestimonialDeleteView(StaffRequiredMixin, DeleteView):
    model = Testimonial
    template_name = 'dashboard/testimonial_confirm_delete.html'
    success_url = reverse_lazy('dashboard_testimonial_list')


# Contact info and about page
class ContactInfoUpdateView(StaffRequiredMixin, UpdateView):
    model = ContactInfo
    form_class = ContactInfoForm
    template_name = 'dashboard/contact_form.html'
    success_url = reverse_lazy('dashboard_home')

    def get_object(self, queryset=None) -> ContactInfo:
        obj, _ = ContactInfo.objects.get_or_create(id=1)
        return obj


class AboutPageUpdateView(StaffRequiredMixin, UpdateView):
    model = AboutPage
    form_class = AboutPageForm
    template_name = 'dashboard/about_form.html'
    success_url = reverse_lazy('dashboard_home')

    def get_object(self, queryset=None) -> AboutPage:
        obj, _ = AboutPage.objects.get_or_create(id=1)
        return obj


# Booking list (read-only)
class BookingListView(StaffRequiredMixin, ListView):
    model = Booking
    template_name = 'dashboard/booking_list.html'
    context_object_name = 'bookings'
    paginate_by = 20