"""Classes for melon orders."""

import random
import datetime


class TooManyMelonsError(ValueError):
    
    def __init__(self):
        super().__init__("No more than 100 melons!")


class AbstractMelonOrder():
    """Abstract base class that other MelonOrders will inherit from"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        
        if qty > 100:
            raise TooManyMelonsError

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False
    
    def get_base_price(self):
        base_price = random.randrange(5, 10)
        time = datetime.datetime.now()
        day = time.strftime("%A")
        
        if day != "Saturday" and day != "Sunday":
            if time.hour >= 8 and time.hour <= 11:
                base_price += 4

        return base_price   

    def get_total(self):
        """Calculate price, including tax + fees."""
        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price *= 1.5
       
        total = base_price * self.qty * (1 + self.tax)

        if self.order_type == "international" and self.qty < 10:
            total += 3
            
        return total

    def mark_shipped(self, shipped):
        """Confirm that an order has been shipped."""
        self.shipped = shipped


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0.00)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
