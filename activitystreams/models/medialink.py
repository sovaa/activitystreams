from activitystreams.models.tags import Tags
from activitystreams.utils import parse_int
from activitystreams.utils import parse_string


class MediaLink(object):
    def __init__(self, raw):
        if raw is None:
            return

        self.url = parse_string(raw.get(Tags.URL), 'url')
        self.duration = parse_int(raw.get(Tags.DURATION), 'duration')
        self.width = parse_int(raw.get(Tags.WIDTH), 'width')
        self.height = parse_int(raw.get(Tags.HEIGHT), 'height')
