from activitystreams.models.activity import Activity
from activitystreams.models.tags import Tags
from activitystreams.exception import ActivityException

import unittest


class VerbTest(unittest.TestCase):
    def test_valid_verb(self):
        activity = Activity({Tags.VERB: 'send'})
        self.assertEqual(activity.verb, 'send')

    def test_verb_required(self):
        self.assertRaises(ActivityException, Activity, {Tags.VERB: ''})

    def test_verb_needs_to_be_str(self):
        self.assertRaises(ActivityException, Activity, {Tags.VERB: 42})

    def test_verb_cannot_be_none(self):
        self.assertRaises(ActivityException, Activity, {Tags.VERB: None})
