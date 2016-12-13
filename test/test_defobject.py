from activitystreams.models.defobject import DefObject
from activitystreams.models.tags import Tags
from activitystreams.exception import ActivityException

import unittest


class DefObjectTest(unittest.TestCase):
    def test_url_empty_ok(self):
        obj = DefObject({Tags.URL: '   '})
        self.assertEqual(obj.url, None)

    def test_object_type(self):
        obj = DefObject({Tags.OBJECT_TYPE: 'some-type'})
        self.assertEqual(obj.object_type, 'some-type')

    def test_id(self):
        obj = DefObject({Tags.ID: 'some-id'})
        self.assertEqual(obj.id, 'some-id')

    def test_content(self):
        obj = DefObject({Tags.CONTENT: 'some-content'})
        self.assertEqual(obj.content, 'some-content')

    def test_summary(self):
        obj = DefObject({Tags.SUMMARY: 'some-summary'})
        self.assertEqual(obj.summary, 'some-summary')

    def test_author(self):
        obj = DefObject({Tags.AUTHOR: {Tags.DISPLAY_NAME: 'some-name'}})
        self.assertEqual(obj.author.display_name, 'some-name')

    def test_published(self):
        obj = DefObject({Tags.PUBLISHED: '2016-06-24T15:33:59+08:00'})
        self.assertEqual(obj.published, '2016-06-24T15:33:59+08:00')

    def test_published_invalid_timezone(self):
        self.assertRaises(ActivityException, DefObject, {Tags.PUBLISHED: '2016-06-24T15:33:59+0800'})

    def test_published_no_timezone(self):
        self.assertRaises(ActivityException, DefObject, {Tags.PUBLISHED: '2016-06-24T15:33:59'})

    def test_published_no_time_separator(self):
        self.assertRaises(ActivityException, DefObject, {Tags.PUBLISHED: '2016-06-24 15:33:59+08:00'})

    def test_updated(self):
        obj = DefObject({Tags.UPDATED: '2016-06-24T15:33:59+08:00'})
        self.assertEqual(obj.updated, '2016-06-24T15:33:59+08:00')

    def test_updated_invalid_timezone(self):
        self.assertRaises(ActivityException, DefObject, {Tags.UPDATED: '2016-06-24T15:33:59+0800'})

    def test_updated_no_timezone(self):
        self.assertRaises(ActivityException, DefObject, {Tags.UPDATED: '2016-06-24T15:33:59'})

    def test_updated_no_time_separator(self):
        self.assertRaises(ActivityException, DefObject, {Tags.UPDATED: '2016-06-24 15:33:59+08:00'})

    def test_image_not_none(self):
        obj = DefObject({Tags.IMAGE: {Tags.DURATION: '5'}})
        self.assertIsNotNone(obj.image)

    def test_image_duration_is_set(self):
        obj = DefObject({Tags.IMAGE: {Tags.DURATION: '5'}})
        self.assertEqual(obj.image.duration, 5)
