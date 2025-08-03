"""Context processors used by the garage app."""
from __future__ import annotations

from datetime import date
from .models import Testimonial


def footer_data(request):
    """Return data used by the footer: all testimonials and current year."""
    return {
        'testimonials': Testimonial.objects.all(),
        'current_year': date.today().year,
    }
