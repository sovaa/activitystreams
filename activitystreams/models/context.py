from activitystreams.exception import ActivityException
from activitystreams.utils import parse_string


class Context:
    """
        '@context': [
            'https://www.w3.org/ns/activitystreams',
            {
                'yhat': 'https://services.ideawisegroup.com/activitystreams-yhat'
            }
        ]
    """

    def __init__(self, raw):
        if raw is None:
            return

        if type(raw) == str:
            self.url = parse_string(raw, 'url')
            return

        if type(raw) != list:
            raise ActivityException('param @context is neither a str nor list, but a "{}"'.format(type(raw)))

        self.url = parse_string(raw[0], 'url')
        extensions = raw[1]

        if type(extensions) != dict:
            raise ActivityException('second value of param @context is not a dict, but a "{}"'.format(type(extensions)))

        self.extensions = extensions.keys()
