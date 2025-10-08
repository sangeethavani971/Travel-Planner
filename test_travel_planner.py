import unittest
from travel_planner import TravelPlanner


class TestTravelPlanner(unittest.TestCase):
    def setUp(self):
        self.planner = TravelPlanner()

    def test_generate_itinerary_basic(self):
        res = self.planner.generate_itinerary(
            destination_topic="Sri Lanka",
            duration=3,
            budget_level="low",
            preferred_transport=["Bus"],
            preferred_stay=["Lodge"],
            interests=["Monuments"],
            start_date="01-Sep-2024"
        )
        self.assertIsInstance(res, dict)
        self.assertIn('summary', res)
        self.assertIn('itinerary_details', res)
        self.assertEqual(len(res['itinerary_details']), 3)

    def test_invalid_destination(self):
        res = self.planner.generate_itinerary(
            destination_topic="Mars",
            duration=2,
            budget_level="low"
        )
        self.assertIn('error', res)


if __name__ == '__main__':
    unittest.main()
