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
                                tags="test1, test2, test3",
                                homepage="http://github.com",
                                is_on_placem=True)
        Location.objects.create(title="Test near zero",
                                latitude=-0.0001,
                                longitude=0.0001,
                                tags="ein_test zwei_test drei_test",
                                homepage="http://startpage.com",
                                is_on_placem=False)

    def test_objects_properly_created(self):
        regular = Location.objects.get(title="Test regular values")
        zero = Location.objects.get(title="Test near zero")
        self.assertEqual(regular.latitude, 12.3587)
        self.assertEqual(regular.longitude, 5.1234)
        self.assertEqual(regular.tags, "test1, test2, test3")
        self.assertEqual(regular.homepage, "http://github.com")
        self.assertEqual(regular.is_on_placem, True)
        self.assertEqual(zero.latitude, -0.0001)
        self.assertEqual(zero.longitude, 0.0001)
        self.assertEqual(zero.tags, "ein_test zwei_test drei_test")
        self.assertEqual(zero.homepage, "http://startpage.com")
        self.assertEqual(zero.is_on_placem, False)


class TestMap(TestCase):
    """
    Checks helper functions of the map app.
    """
    def test_str_to_viewpoint(self):
        self.assertEqual(str_to_viewpoint('5.12,0.14,20'), ([5.12, 0.14], 20))
        self.assertEqual(str_to_viewpoint('-10.11,-9.3,1'),
                         ([-10.11, -9.3], 1))
        self.assertEqual(str_to_viewpoint('2,-9,10.99'), ([2, -9], 10))
        with self.assertRaises(ValueError):
            str_to_viewpoint('100.34,1,9')
        with self.assertRaises(ValueError):
            str_to_viewpoint('1,-90.01,14')
