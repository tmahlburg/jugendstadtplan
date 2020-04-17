from django.test import TestCase

from map.models import Location
from map.views import str_to_viewpoint


class LocationTestCase(TestCase):
    """
    Checks correct set up of the Location model.
    """
    def setUp(self):
        Location.objects.create(title="Test regular values",
                                latitude=12.3587,
                                longitude=5.1234,
                                category="Test",
                                homepage="http://github.com")
        Location.objects.create(title="Test near zero",
                                latitude=-0.0001,
                                longitude=0.0001,
                                category="Test",
                                homepage="http://startpage.com")

    def test_objects_properly_created(self):
        regular = Location.objects.get(title="Test regular values")
        zero = Location.objects.get(title="Test near zero")
        self.assertEqual(regular.latitude, 12.3587)
        self.assertEqual(regular.longitude, 5.1234)
        self.assertEqual(regular.category, "Test")
        self.assertEqual(regular.homepage, "http://github.com")
        self.assertEqual(zero.latitude, -0.0001)
        self.assertEqual(zero.longitude, 0.0001)
        self.assertEqual(zero.category, "Test")
        self.assertEqual(zero.homepage, "http://startpage.com")


class TestMap(TestCase):
    """
    Checks helper functions of the map app.
    """
    def test_str_to_viewpoint(self):
        self.assertEqual(str_to_viewpoint('5.12,0.14'), [5.12, 0.14])
        self.assertEqual(str_to_viewpoint('-10.11,-9.3'), [-10.11, -9.3])
        self.assertEqual(str_to_viewpoint('2,-9'), [2, -9])
        with self.assertRaises(ValueError):
            str_to_viewpoint('100.34,1')
        with self.assertRaises(ValueError):
            str_to_viewpoint('1,-90.01')
