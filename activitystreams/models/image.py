"""
"image": {
  "url": "http://example.org/martin/image",
  "width": 250,
  "height": 250
}
"""

from activitystreams.models.medialink import MediaLink


class Image(MediaLink):
    def __init__(self, raw):
        super(Image, self).__init__(raw)
