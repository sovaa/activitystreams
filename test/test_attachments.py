from activitystreams.models.defobject import DefObject
from activitystreams.models.tags import Tags
from activitystreams.exception import ActivityException

import unittest


class AttachmentsTest(unittest.TestCase):
    def test_empty_attachments_ok(self):
        obj = DefObject({Tags.ATTACHMENTS: None})
        self.assertEqual(obj.attachments, None)

    def test_attachments_not_list_raises_exception(self):
        self.assertRaises(ActivityException, DefObject, {Tags.ATTACHMENTS: 'not a list'})

    def test_attachments_is_list_ok(self):
        obj = DefObject({Tags.ATTACHMENTS: []})
        self.assertEqual(obj.attachments, None)

    def test_attachments_are_parsed(self):
        obj = DefObject({Tags.ATTACHMENTS: [{Tags.CONTENT: 'content'}]})
        self.assertEqual(obj.attachments[0].content, 'content')

    def test_multiple_attachments(self):
        obj = DefObject({Tags.ATTACHMENTS: [{Tags.CONTENT: 'content'}, {Tags.CONTENT: 'content'}]})
        self.assertEqual(2, len(obj.attachments))
        self.assertEqual(obj.attachments[0].content, 'content')
        self.assertEqual(obj.attachments[1].content, 'content')
