"""
actor  	Object
Describes the entity that performed the activity. An activity MUST contain one actor property whose value is a single
Object.

content  	JSON [RFC4627] String
Natural-language description of the activity encoded as a single JSON String containing HTML markup. Visual elements
such as thumbnail images MAY be included. An activity MAY contain a content property.

generator  	Object
Describes the application that generated the activity. An activity MAY contain a generator property whose value is a
single Object.

icon  	Media Link
Description of a resource providing a visual representation of the object, intended for human consumption. The image
SHOULD have an aspect ratio of one (horizontal) to one (vertical) and SHOULD be suitable for presentation at a small
size. An activity MAY have an icon property.

id  	JSON [RFC4627] String
Provides a permanent, universally unique identifier for the activity in the form of an absolute IRI [RFC3987]. An
activity SHOULD contain a single id property. If an activity does not contain an id property, consumers MAY use the
value of the url property as a less-reliable, non-unique identifier.

object  	Object
Describes the primary object of the activity. For instance, in the activity, "John saved a movie to his wishlist", the
object of the activity is "movie". An activity SHOULD contain an object property whose value is a single Object. If the
object property is not contained, the primary object of the activity MAY be implied by context.

published  	[RFC3339] date-time
The date and time at which the activity was published. An activity MUST contain a published property.

provider  	Object
Describes the application that published the activity. Note that this is not necessarily the same entity that generated
the activity. An activity MAY contain a provider property whose value is a single Object.

target  	Object
Describes the target of the activity. The precise meaning of the activity's target is dependent on the activities verb,
but will often be the object the English preposition "to". For instance, in the activity, "John saved a movie to his
wishlist", the target of the activity is "wishlist". The activity target MUST NOT be used to identity an indirect object
that is not a target of the activity. An activity MAY contain a target property whose value is a single Object.

title  	JSON [RFC4627] String
Natural-language title or headline for the activity encoded as a single JSON String containing HTML markup. An activity
MAY contain a title property.

updated  	[RFC3339] date-time
The date and time at which a previously published activity has been modified. An Activity MAY contain an updated
property.

url  	JSON [RFC4627] String
An IRI [RFC3987] identifying a resource providing an HTML representation of the activity. An activity MAY contain a url
property.

verb  	JSON [RFC4627] String
Identifies the action that the activity describes. An activity SHOULD contain a verb property whose value is a JSON
String that is non-empty and matches either the "isegment-nz-nc" or the "IRI" production in [RFC3339]. Note that the
use of a relative reference other than a simple name is not allowed. If the verb is not specified, or if the value is
null, the verb is assumed to be "post".
"""

from activitystreams.models.tags import Tags
from activitystreams.models.actor import Actor
from activitystreams.models.generator import Generator
from activitystreams.models.icon import Icon
from activitystreams.models.defobject import DefObject
from activitystreams.models.provider import Provider
from activitystreams.models.target import Target

from activitystreams.utils import parse_date
from activitystreams.utils import parse_string


class Activity(object):
    def __init__(self, raw):
        self.actor = Actor(raw.get(Tags.ACTOR))
        self.generator = Generator(raw.get(Tags.GENERATOR))
        self.icon = Icon(raw.get(Tags.ICON))
        self.object = DefObject(raw.get(Tags.OBJECT))
        self.provider = Provider(raw.get(Tags.PROVIDER))
        self.target = Target(raw.get(Tags.TARGET))

        self.verb = parse_string(raw.get(Tags.VERB), 'verb', required=True)
        self.content = parse_string(raw.get(Tags.CONTENT), 'content')
        self.id = parse_string(raw.get(Tags.ID), 'id')
        self.title = parse_string(raw.get(Tags.TITLE), 'title')
        self.url = parse_string(raw.get(Tags.URL), 'url')

        # [RFC3339] date-time
        self.published = parse_date(raw.get(Tags.PUBLISHED), 'published')
        self.updated = parse_date(raw.get(Tags.UPDATED), 'updated')
