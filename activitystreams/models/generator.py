from activitystreams.models.defobject import DefObject


class Generator(DefObject):
    def __init__(self, raw):
        super(Generator, self).__init__(raw)
