from activitystreams.models.target import Target
from activitystreams.models.tags import Tags

import unittest


class TargetTest(unittest.TestCase):
    def test_url(self):
        obj = Target({Tags.URL: 'http://google.com/'})
        self.assertEqual(obj.url, 'http://google.com/')

    def test_url_empty(self):
        obj = Target({Tags.URL: '   '})
        self.assertEqual(obj.url, None)

    def test_url_none(self):
        obj = Target({Tags.URL: None})
        self.assertEqual(obj.url, None)

    def test_object_type(self):
        obj = Target({Tags.OBJECT_TYPE: 'some-type'})
        self.assertEqual(obj.object_type, 'some-type')

    def test_object_type_empty(self):
        obj = Target({Tags.OBJECT_TYPE: '   '})
        self.assertEqual(obj.object_type, None)

    def test_object_type_none(self):
        obj = Target({Tags.OBJECT_TYPE: None})
        self.assertEqual(obj.object_type, None)

    def test_id(self):
        obj = Target({Tags.ID: 'some-id'})
        self.assertEqual(obj.id, 'some-id')

    def test_id_empty(self):
        obj = Target({Tags.ID: '   '})
        self.assertEqual(obj.id, None)

    def test_id_none(self):
        obj = Target({Tags.ID: None})
        self.assertEqual(obj.id, None)

    def test_display_name(self):
        obj = Target({Tags.DISPLAY_NAME: 'some-display-name'})
        self.assertEqual(obj.display_name, 'some-display-name')

    def test_display_name_empty(self):
        obj = Target({Tags.DISPLAY_NAME: '   '})
        self.assertEqual(obj.display_name, None)

    def test_display_name_none(self):
        obj = Target({Tags.DISPLAY_NAME: None})
        self.assertEqual(obj.display_name, None)
