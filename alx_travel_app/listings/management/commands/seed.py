from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        locations = ['New York', 'London', 'Paris', 'Tokyo', 'Cairo']
        titles = ['Luxury Apartment', 'Cozy Cabin', 'Beach House', 'City Studio', 'Mountain Retreat']
        descriptions = ['Very nice place.', 'Perfect for your vacation.', 'Quiet and cozy.']

        for i in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description=random.choice(descriptions),
                price_per_night=random.uniform(50, 300),
                location=random.choice(locations)
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded Listings"))
