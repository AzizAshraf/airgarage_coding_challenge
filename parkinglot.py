#parkinglot.py

from collections import defaultdict


# this ParkingLot class holds the main data structure where the information from the
# json is stored. it comprises of a dictionary where the key is the state of the 
# parking lot and the value is a list of all the parking lots in the state. The list
# of states is ordered by the hourly price so that retreiving the query from hourly
# price is quick. This class also processes and returns the results of the query to 
# be displayed.

class ParkingLot:
    # the init doesn't take any arguments but creates an empty dictionary that will 
    # be populated later by the addlot function with each parkinglot individually
    def __init__(self):
        self.parkingstructure = defaultdict(list)
    
    # Helper function to the printquery function. It returns the parking lots of a 
    # given state that has an hourly rate LESS THAN OR EQUUAL to what is queried.
    # since the values are ordered from least to greatest, it will start iterating
    # from the beginning, adding parking lots less than the queried price until 
    # a price is found that is greater. The loop will then break and a list of the 
    # lot names will be returned. This way, the functio nwill only use the amount of 
    # operations as the number of matching lots and no more.
    def _find_price_lte(self, pricelimit, state):
        matching_lots = []
        index = 0;
        while (index < len(self.parkingstructure[state]) and
                self.parkingstructure[state][index].price_hourly <= pricelimit):
            matching_lots.append(self.parkingstructure[state][index].name)
            index += 1

        return matching_lots
    
    # helper function to the printquery function. It returns the parking lots of a given
    # state that has an hourly rate GREATER THAN OR EQUAL to what is queried. Since the 
    # list of lots is ordered by increasing hourly price, this function will iterate 
    # backwards through the list, adding lot names to be returned until a lot is found 
    # that is less than the queried price. The loop will then break. This way, the function
    # will only use the amount of operations as number of matching lots and no more.
    def _find_price_gt(self, pricelimit, state):
        matching_lots = []
        index = len(self.parkingstructure[state]) - 1
        while index >=0 and self.parkingstructure[state][index].price_hourly >= pricelimit:
            matching_lots.append(self.parkingstructure[state][index].name)
            index -= 1
        return matching_lots
    
    # print function to assist with debugging. It prints out all the states that there
    # are parking lots in
    def printstates(self):
        print(self.parkingstructure.keys())
    
    # print function to assist with debugging. It prints out all the parking lots but
    # orders them by state
    def printbystates(self):
        for state in self.parkingstructure.keys():
            for lot in self.parkingstructure[state]:
                print(lot.state, lot.name)
        print("\n\n\n")

    # print function to assist with debugging. It prints out all the parking lots in order 
    # of increasing hourly price
    def printbyprice(self):
        lots = []
        for state in self.parkingstructure.keys():
            for lot in self.parkingstructure[state]:
                lots.append((lot.name, lot.price_hourly, lot.state))
        lotsordered = sorted(lots, key = lambda x: x[1])
        for i in lotsordered:
            print(i[0], i[1], i[2])
        print("\n\n\n")

    # each parking lot is passed through here and this function adds the parking lot to the 
    # self.parkingstructure data structure. It uses the state as the key and adds it to the
    # list of lots in the state as a part of the array. Keeping it ordered. 
    def addlot(self, newlot):
        if newlot.state not in self.parkingstructure.keys():
            self.parkingstructure[newlot.state].append(newlot)
        else:
            price = newlot.price_hourly
            index = 0
            while (index < len(self.parkingstructure[newlot.state]) and
                    price > self.parkingstructure[newlot.state][index].price_hourly):
                index += 1
            self.parkingstructure[newlot.state].insert(index, newlot)

    # locate deals with the query that asks for lots in a given state. Since the parking
    # lots are stored in a dictionary with state as keys and a list of lots as its values,
    # this just gets the list associated with the state and returns a string of all the 
    # matching lot names
    def locate(self, state):
        matching_lots = []
        for lot in self.parkingstructure[state]:
            matching_lots.append(lot.name)
        return ', '.join(matching_lots)


    # pricequery uses the one of the 2 helper functions depending on whether the search query 
    # was a less than or greater than a given price. It iterates through each state, of which
    # there will be at most 50 and finds all the lots in each state to add to the "matching_lots"
    # list. once all states are looked through, it returns a string of names from the 
    # "matching_lots" list. This will handle the query for "find_price_hourly_xx"
    def pricequery(self, pricelimit, query):
        matching_lots = []
        if query == "find_price_hourly_lte":
            for state in self.parkingstructure.keys():
                matching_lots += self._find_price_lte(pricelimit, state)
        elif query == "find_price_hourly_gt":
            for state in self.parkingstructure.keys():
                matching_lots += self._find_price_gt(pricelimit, state)
        return ", ".join(matching_lots)


