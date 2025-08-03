"""Database models for the garage app."""

from __future__ import annotations

from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


class Service(models.Model):
    """A service offered by the garage, e.g. car wash or tyre change."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/')
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.0'))],
    )
    is_popular = models.BooleanField(
        default=False,
        help_text='Check to display this service on the home page.',
    )

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return self.name


class Testimonial(models.Model):
    """Customer testimonials shown in the footer."""

    customer_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(
        default=5,
        help_text='Optional rating (out of 5).',
    )

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self) -> str:
        return f'{self.customer_name}: {self.content[:50]}'


class ContactInfo(models.Model):
    """Contact information for the garage (only one instance should exist)."""

    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()

    # Optional URL for an external map (e.g. a Google Maps share link).
    map_link = models.URLField(
        blank=True,
        null=True,
        help_text='Paste a map share link here (e.g. https://goo.gl/maps/...).'
    )

    # Optional HTML for embedding a map directly on the contact page.  Paste the full
    # <iframe> embed code from Google Maps or another map provider into this field
    # via the Django admin panel.  When provided, the template will render this
    # content as safe HTML.  You typically only need one of map_link or map_embed.
    map_embed = models.TextField(
        blank=True,
        null=True,
        help_text='Optional: paste a full <iframe> embed code here to display a map directly.'
    )

    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'

    def __str__(self) -> str:
        return 'Contact Information'


class AboutPage(models.Model):
    """A simple model to store the about page content."""

    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'

    def __str__(self) -> str:
        return self.heading


class Booking(models.Model):
    """A booking made by a customer."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    registration_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}-\d{1,3}$',
            message='Registration number must be like ABC-123.',
        )],
    )
    hours = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.0'))],
    )
    services = models.ManyToManyField(Service)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.0'),
    )
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self) -> str:
        return f'{self.name} booking on {self.created_at:%Y-%m-%d}'
