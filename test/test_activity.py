from activitystreams.models.activity import Activity

import unittest
import json


class ActivityTest(unittest.TestCase):
    def test_msg(self):
        msg = """
        {
            "actor": {
                "id": "2792607",
                "objectType": "user"
            },
            "verb": "send",
            "object": {
                "id": "33896",
                "objectType": "msg",
                "content": "fasd"
            },
            "target": {
                "id": "2792617",
                "objectType": "user"
            },
            "provider": {
                "id": "POPP"
            },
            "published": "2016-06-24T15:33:59+08:00",
            "_php_": {
                "class": "MessageEvent",
                "mode": "async"
            }
        }
        """

        obj = Activity(json.loads(msg))
        self.assertEqual(obj.actor.id, '2792607')
        self.assertEqual(obj.actor.object_type, 'user')
        self.assertEqual(obj.verb, 'send')
        self.assertEqual(obj.object.id, '33896')
        self.assertEqual(obj.object.object_type, 'msg')
        self.assertEqual(obj.object.content, 'fasd')
        self.assertEqual(obj.target.id, '2792617')
        self.assertEqual(obj.target.object_type, 'user')
        self.assertEqual(obj.provider.id, 'POPP')
        self.assertEqual(obj.published, '2016-06-24T15:33:59+08:00')
