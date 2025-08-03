"""Admin registrations for the garage app."""

from __future__ import annotations


from django.contrib import admin
from .models import Service, Testimonial, ContactInfo, AboutPage, Booking


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_popular')
    list_filter = ('is_popular',)
    search_fields = ('name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'content', 'rating')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')
    exclude = ('map_embed',)


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('heading',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'registration_number')
    filter_horizontal = ('services',)
