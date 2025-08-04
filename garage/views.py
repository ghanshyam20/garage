from __future__ import annotations
from decimal import Decimal
from typing import Dict, Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Service, ContactInfo, AboutPage, Booking
from .forms import BookingForm

# Hourly labour rate for price calculation
LABOR_RATE: Decimal = Decimal('50.0')

def home(request: HttpRequest) -> HttpResponse:
    """Render the home page with popular services."""
    popular_services = Service.objects.filter(is_popular=True)
    return render(request, 'home.html', {'popular_services': popular_services})

def services_list(request: HttpRequest) -> HttpResponse:
    """Render the list of all available services."""
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def booking(request: HttpRequest) -> HttpResponse:
    """Display and handle the booking form."""
    services = Service.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            selected_ids = request.POST.getlist('services')
            selected_services = Service.objects.filter(id__in=selected_ids)
            hours = form.cleaned_data['hours']
            service_total = sum(service.price for service in selected_services)
            total_price = service_total + hours * LABOR_RATE
            booking.total_price = total_price
            booking.save()
            booking.services.set(selected_services)
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {
        'form': form,
        'services': services,
        'labor_rate': LABOR_RATE,
    })

def booking_success(request: HttpRequest) -> HttpResponse:
    """Thank you page after successful booking."""
    return render(request, 'booking_success.html')

def contact(request: HttpRequest) -> HttpResponse:
    """Render the contact page."""
    contact_info = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact_info': contact_info})

def about(request: HttpRequest) -> HttpResponse:
    """Render the about page."""
    about_page = AboutPage.objects.first()
    return render(request, 'about.html', {'about': about_page})
