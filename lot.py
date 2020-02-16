#lot.py

#from collections import defaultdict


# simple Lot class to store each parking lot information in
# this will be used in the ParkingLot class to populate the main
# data structure.
class Lot:
    def __init__(self, lot):
        self.name = lot["name"]
        self.price_hourly = lot["price_hourly"]
        self.daily_max = lot["daily_max"]
        self.address_line1 = lot["address"]["address_line1"]
        self.address_line2 = lot["address"]["address_line2"]
        self.city = lot["address"]["city"]
        self.state = lot["address"]["state"]
        self.zipcode = lot["address"]["zipcode"]
        self.country = lot["address"]["country"]
        self.daily_min = lot["daily_min"]
        self.streetview_url = lot["streetview_url"]
        self.spaceforce_multiplier = lot["spaceforce_multiplier"]
        self.validation_hours = lot["validation_hours"]
        self.organization = lot["organization"]
        self.pk = lot["pk"]

    def getname(self):
        print(self.name)
    def printaddress(self):
        print(self.address_line1)
        if len(self.address_line2) > 0:
            print(self.address_line2)
        print("{0}, {1} {2}".format(self.city, self.state, self.zipcode))
        print(self.country)
        print("\n")


