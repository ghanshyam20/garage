"""Custom forms for the garage dashboard.

These forms are used in the custom admin-like dashboard to allow the garage
owner to manage data without using the default Django admin interface.  They
mirror the models defined in `models.py` but can be customized further if
needed (e.g. ordering of fields or adding widgets).
"""

from __future__ import annotations

from django import forms
from .models import Service, Testimonial, ContactInfo, AboutPage


class ServiceForm(forms.ModelForm):
    """Form for creating and updating services."""

    class Meta:
        model = Service
        fields = ['name', 'description', 'image', 'price', 'is_popular']


class TestimonialForm(forms.ModelForm):
    """Form for creating and updating testimonials."""

    class Meta:
        model = Testimonial
        fields = ['customer_name', 'content', 'rating']


class ContactInfoForm(forms.ModelForm):
    """Form for updating the single ContactInfo instance."""

    class Meta:
        model = ContactInfo
        fields = ['phone_number', 'email', 'address', 'map_link']


class AboutPageForm(forms.ModelForm):
    """Form for updating the about page."""

    class Meta:
        model = AboutPage
        fields = ['heading', 'content', 'image']
