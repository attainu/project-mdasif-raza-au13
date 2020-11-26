import unittest
from parkinglot import Parking_lot


class TestParkingLot(unittest.TestCase):

    def test_create_parking_lot(self):
        parkingLot = Parking_lot()
        res = parkingLot.create_parking_space(6)
        self.assertEqual(6, res)

    def test_park(self):
        parkingLot = Parking_lot()
        res = parkingLot.create_parking_space(6)
        res = parkingLot.parking_of_vehicle("KA-01-HH-1234", "White")
        self.assertNotEqual(-1, res)

    def test_leave(self):
        parkingLot = Parking_lot()
        res = parkingLot.create_parking_space(6)
        res = parkingLot.parking_of_vehicle("KA-01-HH-1234", "White")
        res = parkingLot.leave_parking(1)
        self.assertEqual(True, res)

    def test_getRegNoFromColor(self):
        parkingLot = Parking_lot()
        parkingLot.create_parking_space(6)
        parkingLot.parking_of_vehicle("KA-01-HH-1234", "White")
        parkingLot.parking_of_vehicle("KA-01-HH-9999", "White")
        regnos = parkingLot.get_regno_of_all_car_by_colour("White")
        self.assertIn("KA-01-HH-1234 ", regnos)
        self.assertIn("KA-01-HH-9999 ", regnos)

    def test_getSlotNoFromRegNo(self):
        parkingLot = Parking_lot()
        parkingLot.create_parking_space(6)
        parkingLot.parking_of_vehicle("KA-01-HH-1234", "White")
        parkingLot.parking_of_vehicle("KA-01-HH-9999", "White")
        slotno = parkingLot.get_slot_no_by_registration_no("KA-01-HH-9999")
        self.assertEqual(2, slotno)

    def test_getSlotNoFromColor(self):
        parkingLot = Parking_lot()
        parkingLot.create_parking_space(6)
        parkingLot.parking_of_vehicle("KA-01-HH-1234", "White")
        parkingLot.parking_of_vehicle("KA-01-HH-9999", "White")
        slotnos = parkingLot.get_slot_no_of_all_car_by_colour("White")
        self.assertIn('1', slotnos)
        self.assertIn('2', slotnos)


if __name__ == '__main__':
    unittest.main()
