from __future__ import print_function
from activitystreams.models.activity import Activity


def parse(string):
    return Activity(string)
