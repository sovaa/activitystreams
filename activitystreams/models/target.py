"""
"target" : {
  "url": "http://example.org/blog/",
  "objectType": "blog",
  "id": "tag:example.org,2011:abc123",
  "displayName": "Martin's Blog"
}
"""

from activitystreams.models.defobject import DefObject


class Target(DefObject):
    def __init__(self, raw):
        super(Target, self).__init__(raw)
