from django.test import TestCase

from map.models import Location
from map.views import str_to_viewpoint
from map.views import get_locations_from_tags


class LocationTestCase(TestCase):
    """
    Checks correct set up of the Location model.
    """
    def setUp(self):
        Location.objects.create(title="Test regular values",
                                latitude=12.3587,
                                longitude=5.1234,
                                tags="test1 test2 test3",
                                homepage="http://github.com",
                                is_on_placem=True)
        Location.objects.create(title="Test near zero",
                                latitude=-0.0001,
                                longitude=0.0001,
                                tags="ein_test zwei_test drei_test",
                                homepage="http://startpage.com",
                                is_on_placem=False)
        Location.objects.create(title="Test for tags",
                                latitude=1,
                                longitude=-1,
                                tags="ein_test test1 exklusiv",
                                homepage="http://example.com",
                                is_on_placem=False)

    def test_objects_properly_created(self):
        regular = Location.objects.get(title="Test regular values")
        zero = Location.objects.get(title="Test near zero")
        tags = Location.objects.get(title="Test for tags")

        self.assertEqual(regular.latitude, 12.3587)
        self.assertEqual(regular.longitude, 5.1234)
        self.assertEqual(regular.tags, "test1 test2 test3")
        self.assertEqual(regular.homepage, "http://github.com")
        self.assertEqual(regular.is_on_placem, True)
        self.assertEqual(zero.latitude, -0.0001)
        self.assertEqual(zero.longitude, 0.0001)
        self.assertEqual(zero.tags, "ein_test zwei_test drei_test")
        self.assertEqual(zero.homepage, "http://startpage.com")
        self.assertEqual(zero.is_on_placem, False)
        self.assertEqual(tags.latitude, 1)
        self.assertEqual(tags.longitude, -1)
        self.assertEqual(tags.tags, "ein_test test1 exklusiv")
        self.assertEqual(tags.homepage, "http://example.com")
        self.assertEqual(tags.is_on_placem, False)

    def test_get_locations_from_tags(self):
        regular = list(Location.objects.
                       filter(title="Test regular values").values())[0]
        zero = list(Location.objects.
                    filter(title="Test near zero").values())[0]
        tags = list(Location.objects.
                    filter(title="Test for tags").values())[0]
        locations_test1 = [tags, regular]
        self.assertEqual(get_locations_from_tags("test1"), locations_test1)
        locations_test2 = [tags, zero]
        self.assertEqual(get_locations_from_tags("ein_test"), locations_test2)
        locations_test3 = [tags]
        self.assertEqual(get_locations_from_tags("exklusiv"), locations_test3)


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
