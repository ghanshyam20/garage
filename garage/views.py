"""Views for the garage app."""

from __future__ import annotations

from decimal import Decimal
from typing import Dict, Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Service, ContactInfo, AboutPage, Booking
from .forms import BookingForm

# Hourly labour rate used when calculating total price.  Adjust this value as needed.
LABOR_RATE: Decimal = Decimal('50.0')


def home(request: HttpRequest) -> HttpResponse:
    """Render the home page with popular services."""
    popular_services = Service.objects.filter(is_popular=True)
    return render(request, 'home.html', {'popular_services': popular_services})


def services_list(request: HttpRequest) -> HttpResponse:
    """Render the page listing all available services."""
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def booking(request: HttpRequest) -> HttpResponse:
    """Display and process the booking form."""
    services = Service.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Extract selected service IDs from POST data
            selected_ids = request.POST.getlist('services')
            selected_services = Service.objects.filter(id__in=selected_ids)
            hours = form.cleaned_data['hours']
            # Compute total cost: sum of service prices plus labour hours times rate
            service_total = sum(service.price for service in selected_services)
            total_price = service_total + hours * LABOR_RATE
            booking.total_price = total_price
            booking.save()
            # Associate many-to-many services after saving booking
            booking.services.set(selected_services)
            return redirect('booking_success')
    else:
        form = BookingForm()
    context: Dict[str, Any] = {
        'form': form,
        'services': services,
        'labor_rate': LABOR_RATE,
    }
    return render(request, 'booking.html', context)


def booking_success(request: HttpRequest) -> HttpResponse:
    """Render a simple thank you page after a booking is submitted."""
    return render(request, 'booking_success.html')


def contact(request: HttpRequest) -> HttpResponse:
    """Render the contact page."""
    contact_info = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact_info': contact_info})


def about(request: HttpRequest) -> HttpResponse:
    """Render the about page."""
    about_page = AboutPage.objects.first()
    return render(request, 'about.html', {'about': about_page})
