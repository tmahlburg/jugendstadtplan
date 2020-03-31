from django.test import TestCase

from map.models import Location


class LocationTestCase(TestCase):
    """
    Checks correct set up of the Location model.
    """
    def setUp(self):
        Location.objects.create(title="Test regular values",
                                latitude=12.3587,
                                longitude=5.1234)
        Location.objects.create(title="Test near zero",
                                latitude=-0.0001,
                                longitude=0.0001)

    def test_objects_properly_created(self):
        regular = Location.objects.get(title="Test regular values")
        zero = Location.objects.get(title="Test near zero")
        self.assertEqual(regular.latitude, 12.3587)
        self.assertEqual(regular.longitude, 5.1234)
        self.assertEqual(zero.latitude, -0.0001)
        self.assertEqual(zero.longitude, 0.0001)
