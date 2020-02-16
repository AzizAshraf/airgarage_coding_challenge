import unittest
import json
import sys
from parkinglot import ParkingLot
from lot import Lot


class TestParkingLot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.structure = ParkingLot()
        with open("airgarage-data.json") as lotdata:
            jsondata = json.load(lotdata)

        for jsonlot in jsondata:
            lot = Lot(jsonlot)
            cls.structure.addlot(lot)
        cls.structure.parkingstructure.pop('CA') 
        cls.structure.printbyprice()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_greater_than(self):
        print("price higher than all lots")
        self.assertEqual(self.structure._find_price_gt(1000, 'AZ'), [])
        print("test whether it shows equal to prices")
        self.assertEqual(self.structure._find_price_gt(200, 'NY'), ['Goldilocks Pizza'])
        print("test whether it shows greater than prices")
        self.assertEqual(self.structure._find_price_gt(175, 'AZ'), ['Azusa Ramen', 'Safeway'])

    def test_less_than(self):
        print("price lower than all lots")
        self.assertEqual(self.structure._find_price_lte(-10, 'AZ'), [])
        print("test whether it shows equal to prices")
        self.assertEqual(self.structure._find_price_lte(200, 'NY'), ['Goldilocks Pizza'])
        print("test whether it shows less than prices")
        self.assertEqual(self.structure._find_price_lte(750, 'AZ'), ['Tempe Beach Park', 'Safeway'])

    def test_locate(self):
        print("nonexisting state")
        self.assertEqual(self.structure.locate('AA'), '')
        print("lowercase state")
        self.assertEqual(self.structure.locate('ca'), '')
        print("correct state")
        expected = "Tempe Beach Park, Safeway, Azusa Ramen"
        self.assertEqual(self.structure.locate('AZ'), expected)

if __name__ == '__main__':
    unittest.main()
