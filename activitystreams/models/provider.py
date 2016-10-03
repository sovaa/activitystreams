from activitystreams.models.defobject import DefObject


class Provider(DefObject):
    def __init__(self, raw):
        super(Provider, self).__init__(raw)
