from activitystreams.models.medialink import MediaLink


class Icon(MediaLink):
    def __init__(self, raw):
        super(Icon, self).__init__(raw)
