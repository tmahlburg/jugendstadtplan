from django.test import TestCase

from map.models import Location

from list.views import there_are_public_locations

class ListTestCase(TestCase):
    """
    Checks correct set up of the Location model.
    """
    def setUp(self):
        Location.objects.create(title='Public',
                                latitude=0,
                                longitude=0,
                                tags='tag1',
                                is_on_placem=True,
                                is_public=True)
        Location.objects.create(title='Private',
                                latitude=0,
                                longitude=0,
                                tags='tag2',
                                is_on_placem=False,
                                is_public=False)

    def test_there_are_public_locations(self):
        public = list(Location.objects.filter(title='Public').values())[0]
        private = list(Location.objects.filter(title='Private').values())[0]

        self.assertEqual(there_are_public_locations([public]), True)
        self.assertEqual(there_are_public_locations([private]), False)
        self.assertEqual(there_are_public_locations([private, public]), True)
