import unittest

from example.parking_system import ParkingSystem


# test using unittest
class TestParkingSystem(unittest.TestCase):
  def test_addCar(self) -> None:
    # instance of ParkingSystem named ps / object created from constructor
    ps = ParkingSystem(1, 1, 0)
    # 1. Big car parked
    self.assertEqual(ps.addCar(1), True)
    # 2. Medium car parked
    self.assertEqual(ps.addCar(2), True)
    # 4. Small car can't be parked
    self.assertEqual(ps.addCar(3), False)
    print(ps.spots)
    # 5. Big car can't be parked
    self.assertEqual(ps.addCar(1), False)


# test using pytest
def test_addCar() -> None:
  ps = ParkingSystem(1, 1, 0)
  assert ps.addCar(1)
  assert ps.addCar(2)
  assert not ps.addCar(3)
  assert not ps.addCar(1)
