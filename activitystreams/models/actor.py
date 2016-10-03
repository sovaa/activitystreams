"""
"actor": {
  "url": "http://example.org/martin",
  "objectType" : "person",
  "id": "tag:example.org,2011:martin",
  "image": {
    "url": "http://example.org/martin/image",
    "width": 250,
    "height": 250
  }
}
"""

from activitystreams.models.defobject import DefObject


class Actor(DefObject):
    def __init__(self, raw):
        super(Actor, self).__init__(raw)
