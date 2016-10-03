"""
"target" : {
  "url": "http://example.org/blog/",
  "objectType": "blog",
  "id": "tag:example.org,2011:abc123",
  "displayName": "Martin's Blog"
}
"""

from activitystreams.models.tags import Tags
from activitystreams.utils import parse_string


class Target(object):
    def __init__(self, raw):
        if raw is None:
            return

        self.url = parse_string(raw.get(Tags.URL), 'url')
        self.object_type = parse_string(raw.get(Tags.OBJECT_TYPE), 'objectType')
        self.id = parse_string(raw.get(Tags.ID), 'id')
        self.display_name = parse_string(raw.get(Tags.DISPLAY_NAME), 'displayName')
