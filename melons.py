"""Classes for melon orders."""
class AbstractMelonOrder():
    """Abstract base class that other MelonOrders will inherit from"""
    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax + fees."""
        base_price = 5

        if self.species == "Christmas melon":
            base_price *= 1.5
       
        total = base_price * self.qty * (1 + self.tax)

        if self.order_type == "international" and self.qty < 10:
            total += 3
            
        return total


    def mark_shipped(self):
        """Confirm that an order has been shipped."""
        self.shipped = True


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
