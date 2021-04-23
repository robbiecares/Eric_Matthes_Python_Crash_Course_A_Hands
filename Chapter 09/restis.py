import robspp

"""
myResti = Restaurant("Dori's Diner","American diner")

print(myResti.restaurant_name)
print((myResti.cuisine_type))

myResti.describe_restaurant()
myResti.open_restaurant()

restis = [("Waffle Haus","American diner"),("Burger King","fast food"),("Barefoot Deli","casual dining")]


for name,cuisine in restis:
    resti = Restaurant(name,cuisine)
    resti.describe_restaurant()

restaurant = Restaurant("Steak n Shake","American diner")

restaurant.set_number_served(4)

restaurant.set_number_served(10)

restaurant.set_number_served(-1)
"""

class IceCreamStand(Restaurant):
    """a subclass of restaurants"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        message = robspp.pretty_print('We currently serve',flavors)
        print(message)

flavors = ["cherry","zimt","vanilla","chocolate","mango"]

myies = IceCreamStand("Rita's", "gelato", flavors)

myies.describe_flavors()

