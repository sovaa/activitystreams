from activitystreams.models.tags import Tags
from activitystreams.models.image import Image
from activitystreams.utils import parse_date
from activitystreams.utils import parse_list_of_objects
from activitystreams.utils import parse_string
from activitystreams.utils import parse_object


class DefObject(object):
    def __init__(self, raw):
        if raw is None:
            return

        self.url = parse_string(raw.get(Tags.URL), 'url')
        self.object_type = parse_string(raw.get(Tags.OBJECT_TYPE), 'objectType')
        self.id = parse_string(raw.get(Tags.ID), 'id')
        self.content = parse_string(raw.get(Tags.CONTENT), 'content')
        self.summary = parse_string(raw.get(Tags.SUMMARY), 'summary')
        self.display_name = parse_string(raw.get(Tags.DISPLAY_NAME), 'displayName')
        self.author = parse_object(raw.get(Tags.AUTHOR), 'author')

        # [RFC3339] date-time
        self.published = parse_date(raw.get(Tags.PUBLISHED), 'published')
        self.updated = parse_date(raw.get(Tags.UPDATED), 'updated')

        # TODO: [RFC4627] Array of Strings
        self.downstream_duplicates = raw.get(Tags.DOWNSTREAM_DUPLICATES)
        self.upstream_duplicates = raw.get(Tags.UPSTREAM_DUPLICATES)

        self.attachments = parse_list_of_objects(raw.get(Tags.ATTACHMENTS), 'attachments')

        image = raw.get(Tags.IMAGE)
        if image is not None:
            self.image = Image(image)
        else:
            self.image = None
