from builder import SedanCarBuilder, HatchbackCarBuilder
import unittest


class SetTest(unittest.TestCase):
    def setUp(self):
        self.sedan_car = SedanCarBuilder()
        self.hatchback_car = HatchbackCarBuilder()

    def test_setEngine_Sedan(self):
        self.sedan_car.setEngine()
        self.assertEqual(self.sedan_car.car.list_parts(), [
                         'VR38DETT'], "Should be VR38DETT")

    def test_setAirConditioning_Hatchback(self):
        self.hatchback_car.setCruiseControl()
        self.hatchback_car.setAirConditioning()
        self.assertEqual(self.hatchback_car.car.list_parts(), [
                         'Cruise Control', 'Air Conditioning'], "Should be Air Conditioning")


if __name__ == "__main__":
    unittest.main()
