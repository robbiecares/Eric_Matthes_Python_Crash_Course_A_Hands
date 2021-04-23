class Restaurant:
    """a class to define restaurants"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numberServed = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")

    def set_number_served(self, numGuests):
        self.numberServed += numGuests
        print(f"We have served a total of {Restaurant.numberServed} guests")
