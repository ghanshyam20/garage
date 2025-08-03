"""Forms for the garage app."""

from __future__ import annotations

from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for booking a service.  Excludes the services field so we can render it manually."""

    class Meta:
        model = Booking
        # We exclude services and total_price; total_price is computed in the view.
        fields = [
            'name',
            'email',
            'contact',
            'registration_number',
            'hours',
            'message',
        ]
        widgets = {
            'hours': forms.NumberInput(attrs={'step': 0.5, 'min': 0}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
